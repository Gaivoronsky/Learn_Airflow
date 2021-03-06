from datetime import timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    'owner': 'Alex',
    'depends_on_past': False,
    'email': ['lifami40@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'pipeline',
    default_args=default_args,
    description='VERY HARD SUPER PIPELINE',
    schedule_interval=timedelta(days=1),
    template_searchpath='~/Learn_Airflow'
)

download_audio = BashOperator(
    task_id='download audio file',
    bash_command='wget -O data/Sobol.wav https://storage.yandexcloud.net/speechkittest/%D0%A2%D0%B5%D1%81%D1%82%D1%8B/Sobol.wav',
    dag=dag,
)

length_audio = BashOperator(
    task_id='count length audio',
    bash_command='python3 scripts/len_audio.py',
)

download_audio >> length_audio
