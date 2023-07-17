from airflow import DAG
from airflow.operators.bash import BashOperator 

from datetime import datetime,timedelta

default_args = {
    'owner':'Neha Pipada',
    'retries':5,
    'retry_delay':timedelta(minutes=2)
}

with DAG( 
    dag_id="Our_first_dag_version2",
    default_args=default_args,
    description="This is our first DAG",
    start_date=datetime(2023,7,13,2),
    schedule_interval='@daily') as dag:
    task1= BashOperator(
        task_id='first_task',
        bash_command="echo hello world,this is the first task",
 )
    
    task2= BashOperator(
        task_id="Second_task",
        bash_command="echo hello world, this is our second task",
    )

    task3= BashOperator(
        task_id="third_task",
        bash_command="echo hello world this is our third task"
    )
    task1.set_downstream(task2)
    task1.set_downstream(task3)