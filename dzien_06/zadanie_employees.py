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

# >>> b = Biuro()
# >>> b.add_employee(employee)
# >>> b.export("dane.csv")

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

    def __str__(self):
        return f"<Employee: {self.first_name} {self.last_name} ({self.rate_per_hour})>"

    def __repr__(self):
        return self.__str__()

    def pay_salary(self):
        if self.worked_hours <= 8:
            to_pay = self.worked_hours * self.rate_per_hour
        else:
            to_pay = (8 + 2 * (self.worked_hours - 8)) * self.rate_per_hour
        self.worked_hours = 0
        return to_pay

    def register_time(self, hours):
        self.worked_hours += hours

    def to_list(self):
        return [self.first_name, self.last_name, self.rate_per_hour, self.worked_hours]


class Biuro:

    def __init__(self):
        self.employees = []

    def add_employee(self, employee: Employee):
        self.employees.append(employee)

    def export(self, filename: str):
        with open(filename, "w") as f:
            writer = csv.writer(f, delimiter=";")
            writer.writerow(["first_name", "last_name", "rate_per_hour", "worked_hours"])
            # writer.writerows([emp.__dict__.values() for emp in self.employees])
            writer.writerows([emp.to_list() for emp in self.employees])
