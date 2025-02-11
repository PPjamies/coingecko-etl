from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator

from src.etl import extract, transform, load

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2025, 2, 10),
    'retries': 1,
    'retries_delay': timedelta(minutes=5)
}

dag = DAG(
    'coingecko_etl_job',
    default_args=default_args,
    description='Automated ETL job using Apache Airflow',
    schedule_interval='@daily',
)

extract_task = PythonOperator(
    task_id='extract_task',
    python_callable=extract,
    dag=dag
)

transform_task = PythonOperator(
    task_id='transform_task',
    python_callable=transform,
    op_args=["{{ task_instance.xcom_pull(task_ids='extract_task') }}"],  # Get data from extract_task
    dag=dag
)

load_task = PythonOperator(
    task_id='load_task',
    python_callable=load,
    op_args=["{{ task_instance.xcom_pull(task_ids='transform_task') }}"],
    dag=dag
)

extract_task >> transform_task >> load_task
