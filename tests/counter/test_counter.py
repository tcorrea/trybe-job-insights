from src.counter import count_ocurrences
import pytest
from unittest.mock import mock_open, patch


@pytest.fixture
def fake_data():
    return "javascript JAVASCRIPT PYTHON python pythom javascrip"


EXPECTED_JS_OCURRENCES = 2
EXPECTED_PY_OCURRENCES = 2


def test_counter(fake_data):
    with pytest.raises(FileNotFoundError):
        count_ocurrences("", "")

    with patch("builtins.open", mock_open(read_data=fake_data)):
        javascript_ocurrences = count_ocurrences("", "javascript")
        python_ocurrences = count_ocurrences("", "python")

    assert javascript_ocurrences == EXPECTED_JS_OCURRENCES
    assert python_ocurrences == EXPECTED_PY_OCURRENCES
