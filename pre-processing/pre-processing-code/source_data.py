import os
import boto3
import urllib.request

def source_dataset(new_filename, s3_bucket, new_s3_key):

	source_dataset_url = "https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv"

	# Download the file from `url` and save it locally under `file_name`:
	urllib.request.urlretrieve(source_dataset_url, '/tmp/' + new_filename)

	#uploading new s3 dataset
	s3 = boto3.client('s3')
	s3.upload_file('/tmp/' + new_filename, s3_bucket, new_s3_key)
