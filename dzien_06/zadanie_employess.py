"""
Zaimplementuj klasę Employee umożliwiającą rejestrowanie czasu
pracy oraz wypłacanie pensji na podstawie zadanej stawki
godzinowej. Jeżeli pracownik będzie pracował więcej niż 8 godzin
(podczas pojedynczej rejestracji czasu) to kolejne godziny policz
jako nadgodziny (z podwójną stawką godzinową).
Przykład użycia:

# >>> employee = Employee('Jan', 'Nowak', 100.0)
# >>> employee.register_time(5)
# >>> employee.pay_salary()
# 500.0
# >>> employee.pay_salary()
# 0.0
# >>> employee.register_time(10)
# >>> employee.pay_salary()
# 1200.0

>>> b = Biuro()
>>> b.add_employee(employee)
>>> b.export("dane.csv")

imie;nazwisko;stawka;godziny
Jan;Kowalski,100.0,5

"""
import csv

class Employee:
    def __init__(self, first_name, last_name, rate_per_hour):
        self.first_name = first_name
        self.last_name = last_name
        self.rate_per_hour = rate_per_hour
        self.worked_hours = 0

    def pay_salary(self):
        if self.worked_hours <= 8:
            to_pay = self.worked_hours * self.rate_per_hour
        else:
            to_pay = (8 + 2 * (self.worked_hours - 8)) * self.rate_per_hour
        self.worked_hours = 0
        return to_pay

    def register_time(self, hours):
        self.worked_hours += hours


def test_Employee_init():
    employee = Employee('Jan', 'Nowak', 100.0)
    assert employee
    assert employee.rate_per_hour == 100.0


def test_Employee_pay_salary():
    employee = Employee('Jan', 'Nowak', 100.0)
    assert employee.pay_salary() == 0


def test_Employee_register_time():
    employee = Employee('Jan', 'Nowak', 100.0)
    assert employee.worked_hours == 0
    employee.register_time(5)
    assert employee.worked_hours == 5


def test_Employee_pay_salary_after_register_time():
    employee = Employee('Jan', 'Nowak', 100.0)
    employee.register_time(5)
    assert employee.pay_salary() == 500
    assert employee.pay_salary() == 0


def test_Employee_pay_salary_over_time_hours():
    employee = Employee('Jan', 'Nowak', 100.0)
    employee.register_time(10)
    assert employee.pay_salary() == 1200
    assert employee.pay_salary() == 0