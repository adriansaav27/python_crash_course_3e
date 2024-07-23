import pytest
import employee


@pytest.fixture
def create_person():
    return employee.Employee("Andrew", "Smith", 27_000)


def test_give_default_raise(create_person):
    create_person.give_raise()
    assert create_person.annual_salary == 32_000


def test_give_custom_raise(create_person):
    create_person.give_raise(3_000)
    assert create_person.annual_salary == 30_000
