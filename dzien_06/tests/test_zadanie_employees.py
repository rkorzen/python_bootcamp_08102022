import pytest

# import sys
# sys.path.insert(0, "..")
from zadanie_employees import Employee, Biuro


@pytest.fixture
def employee():
    return Employee('Jan', 'Nowak', 100.0)


@pytest.fixture
def biuro():
    return Biuro()


def test_Employee_init(employee):
    assert employee
    assert str(employee) == "<Employee: Jan Nowak (100.0)>"
    assert repr(employee) == "<Employee: Jan Nowak (100.0)>"
    assert employee.rate_per_hour == 100.0


def test_Employee_pay_salary(employee):
    assert employee.pay_salary() == 0


def test_Employee_register_time(employee):
    assert employee.worked_hours == 0
    employee.register_time(5)
    assert employee.worked_hours == 5


def test_Employee_pay_salary_after_register_time(employee):
    employee.register_time(5)
    assert employee.pay_salary() == 500
    assert employee.pay_salary() == 0


def test_Employee_pay_salary_over_time_hours(employee):
    employee.register_time(10)
    assert employee.pay_salary() == 1200
    assert employee.pay_salary() == 0


def test_Biuro():
    assert Biuro()


def test_Biuro_add_employee(employee, biuro):
    assert len(biuro.employees) == 0
    biuro.add_employee(employee)
    assert len(biuro.employees) == 1

    employee2 = Employee('Rafał', 'K', 200.0)
    biuro.add_employee(employee2)
    assert len(biuro.employees) == 2


def test_Biuro_export_to_csv(employee, biuro):
    employee2 = Employee('Rafał', 'K', 200.0)
    biuro.add_employee(employee)
    biuro.add_employee(employee2)
    biuro.export("test_dane.csv")
    with open("test_dane.csv") as f:
        assert f.read() == """first_name;last_name;rate_per_hour;worked_hours
Jan;Nowak;100.0;0
Rafał;K;200.0;0
"""
