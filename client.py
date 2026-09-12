class AutonomousTaskDagDecomposerClient:
    def decompose_task(self, goal_prompt='Design, benchmark, and publish an e-commerce landing page with live Stripe payments', max_parallel_workers=4):
        steps = [
            {'step_id': 'T1', 'title': 'Scrape product catalog metadata', 'deps': []},
            {'step_id': 'T2', 'title': 'Generate 5-style product hero images', 'deps': ['T1']},
            {'step_id': 'T3', 'title': 'Compose marketing copy with 5 tone variants', 'deps': ['T1']},
            {'step_id': 'T4', 'title': 'Assemble glassmorphism responsive HTML', 'deps': ['T2', 'T3']},
            {'step_id': 'T5', 'title': 'Inject Stripe single-use token payment link', 'deps': ['T4']}
        ]
        return {
            'plan_id': 'dag_pln_5523',
            'goal_prompt': goal_prompt,
            'topological_order': ['T1', 'T2', 'T3', 'T4', 'T5'],
            'total_subtasks': len(steps),
            'critical_path_latency_sec': 4.8,
            'concurrency_factor': 2.0,
            'execution_dag': steps,
            'plan_manifest_url': 'https://planner.dag.genpark.ai/plans/5523.json'
        }
