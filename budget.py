
class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
        self.money = 0

    def deposit(self, money, msg=None):
        self.money += money
        self.ledger.append({'description': msg or '', 'amount': money})
        return True

    def withdraw(self, money, msg=None):
        if not self.check_funds(money):
            return False

        self.money -= money
        self.ledger.append({'description': msg or '', 'amount': -money})
        return True

    def check_funds(self, money):
        return money <= self.money

    def transfer(self, money, other_category):
        return (
            self.withdraw(money, "Transfer to " + other_category.name)
            and other_category.deposit(money, "Transfer from " + self.name)
        )

    def get_balance(self):
        return self.money

    def __str__(self):
        resultaat = self.name.center(30, '*') + '\n'

        for lijn in self.ledger:
            description = lijn["description"]
            amount = lijn["amount"]

            if len(description) > 23:
                description = description[:23]

            resultaat += f"{description:<23}{amount:>7.2f}\n"

        resultaat += "Total: " + str(self.money)
        return resultaat


def create_spend_chart(categories):
    pass
