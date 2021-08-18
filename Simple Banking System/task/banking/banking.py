from Card import Card, check_luhn_algorithm
from Database import Database


def obtain_user_option_account():
    accept_options = [0, 1, 2, 3, 4, 5]
    while True:
        menu = f"\n" \
               f"1. Balance\n" \
               f"2. Add income\n" \
               f"3. Do transfer\n" \
               f"4. Close account\n" \
               f"5. Log out\n" \
               f"0. Exit"
        print(menu)
        user_option = int(input())
        print()
        if user_option in accept_options:
            return user_option
        else:
            print("Wrong option")


def go_exit(database: Database):
    database.close_connection()
    print("Bye!")


def go_user_account_balance(database: Database, card: Card):
    print(f"Balance: {card.balance}")
    go_user_account(database, card)


def go_user_account_logout(database: Database):
    print("You have successfully logged out!")
    create_menu(database)


def go_user_add_income(database: Database, card: Card):
    print("Enter income:")
    income = int(input())
    card = database.add_income_card(card, income)
    print("Income was added!")
    go_user_account(database, card)


def go_user_do_transfer(database: Database, card: Card):
    print("Transfer")
    print("Enter card number:")
    card_number_to_transfer = input()
    if not check_luhn_algorithm(card_number_to_transfer):
        print("Probably you made a mistake in the card number. Please try again!")
    elif not database.exists_card_by_card_number(card_number_to_transfer):
        print("Such a card does not exist.")
    else:
        print("Enter how much money you want to transfer:")
        amount_to_transfer = int(input())
        if database.transfer_amount_card(card, card_number_to_transfer, amount_to_transfer):
            card.balance -= amount_to_transfer
            print("Success!")
        else:
            print("Not enough money!")

    go_user_account(database, card)


def go_user_close_account(database: Database, card: Card):
    database.close_account(card)
    print("The account has been closed!")
    create_menu(database)


def go_user_account(database: Database, card: Card):
    user_option = obtain_user_option_account()
    if user_option == 1:
        go_user_account_balance(database, card)
    elif user_option == 2:
        go_user_add_income(database, card)
    elif user_option == 3:
        go_user_do_transfer(database, card)
    elif user_option == 4:
        go_user_close_account(database, card)
    elif user_option == 5:
        go_user_account_logout(database)
    elif user_option == 0:
        go_exit(database)


def go_main_login_account(database: Database):
    print("Enter your card number:")
    card_number = int(input())
    print("Enter your PIN:")
    card_pin = int(input())
    print()
    user_card = database.fetch_card(card_number, card_pin)
    if user_card is not None:
        print("You have successfully logged in!")
        go_user_account(database, user_card)
    else:
        print("Wrong card number or PIN!")
        create_menu(database)


def go_main_create_account(database: Database):
    new_card = Card()
    new_card.create_one(database)
    print("Your card has been created")
    print("Your card number:")
    print(new_card.number)
    print("Your card PIN:")
    print(new_card.pin)
    create_menu(database)


def obtain_user_option_main():
    accept_options = [0, 1, 2]
    while True:
        menu = f"\n" \
               f"1. Create an account\n" \
               f"2. Log into account\n" \
               f"0. Exit"
        print(menu)
        user_option = int(input())
        print()
        if user_option in accept_options:
            return user_option
        else:
            print("Wrong option")


def create_menu(database: Database):
    user_option = obtain_user_option_main()
    if user_option == 1:
        go_main_create_account(database)
    elif user_option == 2:
        go_main_login_account(database)
    elif user_option == 0:
        go_exit(database)


def create_db():
    database = Database()
    database.check_tables()
    return database


def main():
    database = create_db()
    create_menu(database)


if __name__ == '__main__':
    main()
