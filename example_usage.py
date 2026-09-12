from client import AutonomousTaskDagDecomposerClient

def main():
    client = AutonomousTaskDagDecomposerClient()
    res = client.decompose_task()
    print('Task DAG Decomposer: ' + res['plan_id'])
    print('Topological Path: ' + ' -> '.join(res['topological_order']))
    print('Total Subtasks: ' + str(res['total_subtasks']) + ' | Critical Latency: ' + str(res['critical_path_latency_sec']) + 's')
    print('Plan URL: ' + res['plan_manifest_url'])

if __name__ == '__main__':
    main()
