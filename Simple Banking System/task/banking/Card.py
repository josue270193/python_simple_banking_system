import random

from Database import Database


def generate_checksum(new_card_number: str):
    numbers = [int(n) for n in new_card_number]
    numbers = [numbers[index] * 2 if index % 2 == 0 else numbers[index] for index in range(len(numbers))]
    numbers = [n - 9 if n > 9 else n for n in numbers]
    return f"{(10 - (sum(numbers) % 10)) % 10}"


def check_luhn_algorithm(card_number: str):
    return card_number is not None and generate_checksum(card_number[:-1]) == card_number[-1]


class Card:

    def __init__(self):
        self.id = 0
        self.number = ""
        self.pin = ""
        self.balance = 0
        self.inn = "400000"

    def create_one(self, database: Database):
        random.seed()
        new_card_number = None
        while new_card_number is None or database.exists_card_by_card_number(new_card_number):
            customer_account_number = f"{random.randint(0, 999999999):0<9}"  # Complete with zeros using 9 digit
            new_card_number = self.inn + customer_account_number
            checksum = generate_checksum(new_card_number)
            new_card_number += checksum

        self.id = int(new_card_number)
        self.number = new_card_number
        self.pin = f"{random.randint(0, 9999):0<4}"  # Complete with zeros using 4 digit
        database.insert_card(self)
