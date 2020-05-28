import pytest
from io import StringIO
from ansiblemetrics.general.num_tokens import NumTokens

#script_tokens
script_9 = '- name: INCLUDE UNIQUE USERNAME FROM REGISTER.YML\n\tinclude_vars:\n\t\tfile: username_info.yml'

TEST_DATA = [
    (script_9, 9)
]

@pytest.mark.parametrize('script, expected', TEST_DATA)
def test(script, expected):
    script = StringIO(script.expandtabs(2))
    count = NumTokens(script).count()
    script.close()
    assert count == expected