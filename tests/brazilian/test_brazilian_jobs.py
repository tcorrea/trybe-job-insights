from src.brazilian_jobs import read_brazilian_file
import pytest


@pytest.fixture
def fake_expected_data():
    return {"title": "Maquinista", "salary": "2000", "type": "trainee"}


# @pytest.fixture
# def fake_data():
#     return {"titulo": "Maquinista", "salario": "2000", "tipo": "trainee"}


def test_brazilian_jobs(fake_expected_data):
    expected_data = read_brazilian_file("tests/mocks/brazilians_jobs.csv")

    assert expected_data[0] == fake_expected_data

    # TODO: mock a função jobs.read que é chamada no read_brazilian_file
