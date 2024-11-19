from datetime import timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
from datetime import datetime,date
from youtube_comments import run_yt_comments_pipeline

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': date.today(),
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1)
}

dag = DAG(
    'yt_comments_dag',
    default_args=default_args,
    description='Our first DAG with ETL process!',
    schedule_interval=timedelta(days=1),
)

run_etl = PythonOperator(
    task_id='complete_youtube_comments',
    python_callable=run_yt_comments_pipeline,
    dag=dag, 
)

run_etl