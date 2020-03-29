from airflow.contrib.operators.kubernetes_pod_operator import KubernetesPodOperator
from datetime import datetime, timedelta
from airflow import DAG


default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": datetime(2015, 6, 1),
    "retries": 1,
    "retry_delay": timedelta(minutes=5)
}

dag = DAG(
    dag_id="kubernetes-tutorial",
    schedule_interval=None,
    default_args=default_args,
    catchup=False
)

# https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/
k = KubernetesPodOperator(
    name="my-kubernetes-test",
    task_id="kubernetes-1",
    dag=dag,
    # context='docker-desktop',
    namespace='default',
    image="alpine:3.11.5",
    cmds=["/bin/sh"],
    arguments=["-c", "echo \"Hello human, I'm running in a container with: $(uname -r)\"; sleep 10"],
    is_delete_operator_pod=False,
    in_cluster=False
)
