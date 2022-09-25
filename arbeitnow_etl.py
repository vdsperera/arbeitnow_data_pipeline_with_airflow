"""
* here we have created a ETL process to extract jobs data from arbeitnow api,
transform and load them into S3 bucket
"""

# import os
# from dotenv import load_dotenv
# load_dotenv()

import requests
import sys
import json
import pandas


def start_etl():
	# extract data from arbeitnow api
	endpoint = "https://arbeitnow.com/api/job-board-api"
	response = requests.get(endpoint, timeout=10)

	if not response.status_code == 200:
		print("request failed")
		sys.exit()

	content = json.loads(response.content)
	content_data = content["data"]

	# transform extracted data
	job_info_list = []
	for data_item in content_data:
		job_info = {
			"title": data_item["title"],
			"company_name": data_item["company_name"],
			"created_at": data_item["created_at"]
		}
		job_info_list.append(job_info)
	df = pandas.DataFrame(job_info_list)
	
	# load data into s3 bucket
	df.to_csv("s3://sample-buck-de/result.csv")
	print("completed by saving results to csv")

# start_etl()