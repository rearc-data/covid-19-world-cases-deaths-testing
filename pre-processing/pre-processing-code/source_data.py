import os
import boto3
from urllib.request import urlopen
from urllib.error import URLError, HTTPError
from multiprocessing.dummy import Pool
import time
from .s3_md5_compare import md5_compare


def data_to_s3(frmt):

    # throws error occured if there was a problem accessing data
    # otherwise downloads and uploads to s3

    source_dataset_url = 'https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data'

    response = None
    retries = 5
    for attempt in range(retries):
        try:
            response = urlopen(source_dataset_url + frmt)
        except HTTPError as e:
            if attempt == retries:
                raise Exception('HTTPError: ', e.code, frmt)
            time.sleep(0.2 * attempt)
        except URLError as e:
            if attempt == retries:
                raise Exception('URLError: ', e.reason, frmt)
            time.sleep(0.2 * attempt)
        else:
            break

    if response is None:
        raise Exception('There was an issue downloading the dataset')

    data_set_name = os.environ['DATA_SET_NAME']
    filename = data_set_name + frmt
    file_location = '/tmp/' + filename

    with open(file_location, 'wb') as f:
        f.write(response.read())

    return True


def source_dataset(s3_bucket, new_s3_key):

    # list of enpoints to be used to access data included with product
    data_endpoints = [
        '.csv'
    ]

    # multithreading speed up accessing data, making lambda run quicker
    with (Pool(2)) as p:
        p.map(data_to_s3, data_endpoints)

    s3_uploads = []
    s3 = boto3.client('s3')

    for filename in os.listdir('/tmp'):
        file_location = '/tmp/' + filename
        has_changes = md5_compare(
            s3, s3_bucket, new_s3_key + filename, file_location)
        if has_changes:
            s3.upload_file(file_location, s3_bucket, new_s3_key + filename)
            print('Uploaded: ' + filename)
        else:
            print('No changes in: ' + filename)
        asset_source = {'Bucket': s3_bucket, 'Key': new_s3_key + filename}
        s3_uploads.append({'has_changes': has_changes,
                           'asset_source': asset_source})

    count_updated_data = sum(
        upload['has_changes'] == True for upload in s3_uploads)
    asset_list = []
    if count_updated_data > 0:
        asset_list = list(
            map(lambda upload: upload['asset_source'], s3_uploads))
        if len(asset_list) == 0:
            raise Exception('Something went wrong when uploading files to s3')

    # asset_list is returned to be used in lamdba_handler function
    return asset_list
