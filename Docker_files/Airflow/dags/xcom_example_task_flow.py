from airflow.decorators import dag, task
from datetime import datetime

default_args = {
    'owner': 'data_engineer',
    'depends_on_past': False,
}

@dag(
    dag_id='xcom_example_dag_taskflow',
    default_args=default_args,
    schedule_interval='@daily',
    start_date=datetime(2025, 5, 5),
    catchup=False,
    tags=['DE_course'],
)
def process_dag():
    @task
    def push_data():
       return 'Hello, Airflow!'

    @task
    def process_data(my_data: str):
        print(my_data)

    data = push_data()
    print_data = process_data(data)

    data >> print_data


process_dag()
