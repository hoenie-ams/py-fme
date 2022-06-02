"""
Demo of classes
"""


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    @staticmethod
    def say_hi():
        print("Hello")


my_object = Rectangle(length=10, width=20)

print(my_object.length)
print(my_object.area())


class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        # self.balance = self.balance + amount
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def show_balance(self):
        print(f"{self.owner} has EUR {self.balance}.")


account_thomas = BankAccount("Thomas")
account_thomas.deposit(100)
account_thomas.withdraw(50)
account_thomas.show_balance()


class Base:
    pass


class Derived(Base):
    pass


class Vehicle:
    description = "This is a vehicle"

    def brake(self):
        return "Braking the vehicle"

    def drive(self):
        return "Let's go!"


class Car(Vehicle):
    def __init__(self, color: str):
        self.color = color


car = Car("black")
print(car.drive())
print(car.brake())

for x in range(5):
    print(x)

print("hello")
