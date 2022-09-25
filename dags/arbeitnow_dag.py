"""

"""

import sys
import os
sys.path.insert(1, "/mnt/92D26AE0D26AC7D5/Python/data_pipeline_with_airflow")

from airflow import DAG
from airflow.operators.python import PythonOperator
from arbeitnow_etl import start_etl
from datetime import datetime
from datetime import timedelta

default_args = {
	"owner": "airflow",
	"depends_on_past": False,
	"start_date": datetime(2020, 9, 24),
	"email": ["samp@gmail.com"],
	"email_on_failure": False,
	"email_on_retry": False,
	"retries": 1,
	"retry_delay": timedelta(minutes=1)
}

def dag_function_call():
	print("dag function is called successfully")

airbeitnow_dag = DAG("arbeitnow_dag", default_args=default_args, description='arbeitnow jobs dag description')
run_arbeitnow_etl = PythonOperator(
	task_id="complete_arbeitnow_etl",
	python_callable=dag_function_call,
	dag=airbeitnow_dag
	)

run_arbeitnow_etl
