from ansiblemetrics.import_metrics import general_metrics, playbook_metrics


def extract_all(script: str):
    if script is None:
        raise TypeError('Expected a string')

    # TODO: Add support for pre-tasks
    metrics = general_metrics
    metrics.update(playbook_metrics)

    results = dict()

    # Execute metrics
    for name in metrics:
        results[name] = metrics[name](script).count()

    return results

