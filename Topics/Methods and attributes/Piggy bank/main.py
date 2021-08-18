class PiggyBank:
    # create __init__ and add_money methods

    def __init__(self, dollars, cents):
        self.dollars = dollars
        self.cents = cents

    def add_money(self, deposit_dollars, deposit_cents):
        cents_to_dollars = (deposit_cents + self.cents) // 100
        cents_left = (deposit_cents + self.cents) % 100
        self.dollars += deposit_dollars + cents_to_dollars
        self.cents = cents_left

