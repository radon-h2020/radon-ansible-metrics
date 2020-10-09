from io import StringIO
from ansiblemetrics.import_metrics import general_metrics, playbook_metrics


def extract_all(script: StringIO):
    if script is None:
        raise TypeError('Expected a StringIO object')

    # TODO: Add support for pre-tasks
    metrics = general_metrics
    metrics.update(playbook_metrics)

    results = dict()

    # Execute metrics
    for name in metrics:
        results[name] = metrics[name](script).count()

    script.close()

    return results
