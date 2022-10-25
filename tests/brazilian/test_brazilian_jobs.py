from src.brazilian_jobs import read_brazilian_file
import pytest
from unittest.mock import patch


@pytest.fixture
def fake_expected_data():
    return [{"title": "Maquinista", "salary": "2000", "type": "trainee"}]


@pytest.fixture
def fake_data():
    return [{"titulo": "Maquinista", "salario": "2000", "tipo": "trainee"}]


# NOTE: A função "read_brazilian_file" usa a função "read" do modulo "jobs",
# NOTE: por isso que tentar mockar a função "read" no modulo
# NOTE: read_brazilian_file estava dando erro.
# NOTE: Mock da função "read" tem que ser passado antes das fixtures. Ref:
# https://stackoverflow.com/questions/25057383/patch-decorator-is-not-compatible-with-pytest-fixture
@patch("src.jobs.read")
def test_brazilian_jobs(read_mock, fake_expected_data, fake_data):
    read_mock.return_value = fake_data
    expected_data = read_brazilian_file("any-path")

    assert expected_data == fake_expected_data
