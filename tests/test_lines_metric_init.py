import pytest
from enum import Enum

from ansiblemetrics.lines_metric import LinesMetric

yaml_invalid_1 = '---\n\t\thosts: localhost\n\ttasks:\n\t\t\t-name: a name\n\t\tdebug:\n\t\tmsg: "This is an invalid ' \
                 'yaml file. Wrong indentation!" '

yaml_valid_1 = '---\n- hosts: localhost\n\n\ttasks:\n\t- name: task 1    # This is the first ' \
               'task\n\t\tinclude_vars:\n\t\t\tfile: username_info.yml\n\n# This is the second task\n\t- name: task ' \
               '2\n\t\tinclude_vars:\n\t\t\tfile: username_info.yml '


class Raised(Enum):
    TRUE = 'exception raised',
    FALSE = 'exception not raised'


TEST_DATA = [
    (yaml_invalid_1, Raised.TRUE),
    (yaml_valid_1, Raised.FALSE)
]


@pytest.mark.parametrize('script, expected', TEST_DATA)
def test(script, expected):
    script = script.expandtabs(2)
    raised = Raised.FALSE

    try:
        LinesMetric(script)
    except TypeError:
        raised = Raised.TRUE

    assert raised == expected
