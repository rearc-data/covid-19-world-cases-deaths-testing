<a href="https://www.rearc.io/data/">
    <img src="./rearc_logo_rgb.png" alt="Rearc Logo" title="Rearc Logo" height="52" />
</a>

# COVID-19 - World Confirmed Cases, Deaths, and Testing

You can subscribe to the AWS Data Exchange product utilizing the automation featured in this repository by visiting [https://aws.amazon.com/marketplace/pp/prodview-3b32sjummof5s](https://aws.amazon.com/marketplace/pp/prodview-3b32sjummof5s). 

## Main Overview
This dataset is a collection of the COVID-19 data maintained by "Our World in Data" which collects it from John Hopkins University. It is updated daily and includes data on confirmed cases, deaths, and testing. It is an up-to-date data on confirmed cases, deaths, and testing, throughout the duration of the COVID-19 pandemic.
#### Data Sources  
- Confirmed cases and deaths: This data comes from the European Centre for Disease Prevention and Control (ECDC)
- Testing for COVID-19: This data is collected by the "Our World in Data" team from official reports

The dataset follows a format of 1 row per location and date. The other columns represent all of the main variables related to confirmed cases, deaths, and testing. The columns are:  

`iso_code,location,date,total_cases,new_cases,total_deaths,new_deaths,total_cases_per_million,new_cases_per_million,total_deaths_per_million,new_deaths_per_million,total_tests,new_tests,total_tests_per_thousand,new_tests_per_thousand,tests_units,population,population_density,median_age,aged_65_older,aged_70_older,gdp_per_capita,extreme_poverty,cvd_death_rate,diabetes_prevalence,female_smokers,male_smokers,handwashing_facilities,hospital_beds_per_100k`

## More Information
- [Source: Data on COVID-19 by Our World in Data](https://github.com/owid/covid-19-data/tree/master/public/data/)
- [Original Data Source: John Hopkins University](https://github.com/CSSEGISandData/COVID-19)
- [Homepage: Our World in Data](https://ourworldindata.org/coronavirus)
- [Terms of Use](https://creativecommons.org/licenses/by/4.0/)
- Frequency: Daily
- Formats: CSV, XLSX

## Contact Details
- If you find any issues with or have enhancement ideas for this product, open up a GitHub [issue](https://github.com/rearc/aws-data-exchange-covid-19-world-cases-deaths-testing/issues) and we will gladly take a look at it. Better yet, submit a pull request. Any contributions you make are greatly appreciated :heart:.
- If you are looking for specific open datasets currently not available on ADX, please submit a request on our project board [here](https://github.com/rearc-data/covid-datasets-aws-data-exchange/projects/1).
- If you have questions about the source data, please contact "Our World in Data".
- If you have any other questions or feedback, send us an email at data@rearc.io.

## About Rearc
Rearc is a cloud, software and services company. We believe that empowering engineers drives innovation. Cloud-native architectures, modern software and data practices, and the ability to safely experiment can enable engineers to realize their full potential. We have partnered with several enterprises and startups to help them achieve agility. Our approach is simple — empower engineers with the best tools possible to make an impact within their industry.
