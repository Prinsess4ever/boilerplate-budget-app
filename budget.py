
class Category:
    def __init__(self, food):
        self.aan_wat_je_geeft = food
        self.ledger = []
        self.money = 0
        self.lijst = []
        self.fiets = ""

    def deposit(self, money, msg=None):
        self.money += money
        if msg is not None:
            self.ledger.append({'description': msg, 'amount': money})
        else:
            self.ledger.append({'description': '', 'amount': money})

    def withdraw(self, money, msg):
        self.money -= money
        self.ledger.append({'description': msg, 'amount': money})

    def transfer(self, money, other_category):
        self.ledger.append({'description': "Transfer to " + other_category.aan_wat_je_geeft, 'amount': -money})
        other_category.ledger.append({'description': "Transfer from " + self.aan_wat_je_geeft, 'amount': money})
        self.money -= money
        other_category.money += money
        return True
    def get_balance(self):
        # *************Food*************
        # initial deposit        1000.00
        # groceries               -10.15
        # restaurant and more foo -15.89
        # Transfer to Clothing    -50.00
        # Total: 923.96
        food = self.aan_wat_je_geeft
        x = food.center(30, '*')
        resultaat = x + '\n'
        aantal = 0
        ok = ""
        for lijn in self.ledger:
            iets_nemen = self.ledger[aantal]

            description = iets_nemen["description"]
            amount = iets_nemen["amount"]

            if aantal != 0:
                ok = "Total: " + str(self.money)

            if len(description) > 30:
                description = description[:23]
            if aantal > 0:
                resultaat1 = f"{description:<23}{-amount:>7.2f}"
            else:
                resultaat1 = f"{description:<23}{amount:>7.2f}"
            resultaat += resultaat1 + '\n'
            aantal += 1
        a =1
        return self.money






def create_spend_chart(categories):
    pass
