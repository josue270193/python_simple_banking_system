import sqlite3

import Card


class Database:

    def __init__(self):
        self.connection = sqlite3.connect("card.s3db")
        self.table_card = "card"

    def check_tables(self):
        cursor = self.connection.cursor()
        query_table_card = f"CREATE TABLE IF NOT EXISTS {self.table_card} (" \
                           f"id INTEGER, " \
                           f"number TEXT, " \
                           f"pin TEXT, " \
                           f"balance INTEGER DEFAULT 0" \
                           f");"
        cursor.execute(query_table_card)
        cursor.close()
        self.connection.commit()

    def insert_card(self, card: Card):
        cursor = self.connection.cursor()
        query_insert_card = f"INSERT INTO {self.table_card} VALUES (" \
                            f"{card.id}," \
                            f"'{card.number}'," \
                            f"'{card.pin}'," \
                            f"{card.balance}" \
                            f");"
        cursor.execute(query_insert_card)
        cursor.close()
        self.connection.commit()

    def exists_card_by_card_number(self, card_number: str):
        cursor = self.connection.cursor()
        query_select_card = f"SELECT * " \
                            f"FROM {self.table_card} " \
                            f"WHERE number = '{card_number}';"
        cursor.execute(query_select_card)
        result = cursor.fetchone()
        cursor.close()
        return result is not None

    def fetch_card_by_card_number(self, card_number: int) -> Card:
        cursor = self.connection.cursor()
        query_select_card = f"SELECT * " \
                            f"FROM {self.table_card} " \
                            f"WHERE number = '{card_number}' " \
                            f";"
        cursor.execute(query_select_card)
        result = cursor.fetchone()
        cursor.close()
        if result is not None:
            card = Card.Card()
            card.id = result[0]
            card.number = result[1]
            card.pin = result[2]
            card.balance = result[3]
            return card
        else:
            return None

    def fetch_card(self, card_number: int, card_pin: int) -> Card:
        cursor = self.connection.cursor()
        query_select_card = f"SELECT * " \
                            f"FROM {self.table_card} " \
                            f"WHERE number = '{card_number}' " \
                            f"AND pin = '{card_pin}' " \
                            f";"
        cursor.execute(query_select_card)
        result = cursor.fetchone()
        cursor.close()
        if result is not None:
            card = Card.Card()
            card.id = result[0]
            card.number = result[1]
            card.pin = result[2]
            card.balance = result[3]
            return card
        else:
            return None

    def add_income_card(self, card: Card, income: int):
        cursor = self.connection.cursor()
        query_add_income_card = f"UPDATE {self.table_card} " \
                                f"SET balance = balance + ({income}) " \
                                f"WHERE id = {card.id}" \
                                f";"
        cursor.execute(query_add_income_card)
        cursor.close()
        self.connection.commit()
        card.balance += income
        return card

    def close_account(self, card):
        cursor = self.connection.cursor()
        query_close_account = f"DELETE FROM {self.table_card} " \
                              f"WHERE id = {card.id}" \
                              f";"
        cursor.execute(query_close_account)
        cursor.close()
        self.connection.commit()

    def close_connection(self):
        self.connection.close()

    def transfer_amount_card(self, transmitter_card_info, card_number_to_transfer, amount_to_transfer):
        transmitter_card = self.fetch_card(transmitter_card_info.number, transmitter_card_info.pin)
        if transmitter_card is not None and transmitter_card.balance >= amount_to_transfer:
            receiver_card = self.fetch_card_by_card_number(card_number_to_transfer)
            if receiver_card is not None:
                self.add_income_card(receiver_card, amount_to_transfer)
                self.add_income_card(transmitter_card, -amount_to_transfer)
                return True
        return False
