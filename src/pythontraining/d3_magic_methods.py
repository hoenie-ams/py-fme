"""
Demo of magic methods
"""
from functools import total_ordering


class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f"Bank account of {self.owner}"

    def __gt__(self, other):
        return self.balance > other.balance


account_julia = BankAccount("Julia", 100)
account_timo = BankAccount("Timo", 50)
print(account_julia > account_timo)


class SubBankAccount(BankAccount):
    def __init__(self, owner, balance):
        super().__init__(owner, balance)


sub = SubBankAccount("Thomas", 100)
print(sub)


@total_ordering
class Person:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def __eq__(self, other):
        return self.height == other.height

    def __lt__(self, other):
        return self.height < other.height

    def __str__(self):
        return f"Person named {self.name}"