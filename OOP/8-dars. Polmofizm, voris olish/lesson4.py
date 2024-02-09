class BankCard:
    def __init__(self, name, card, password, balance, phone):
        self.name = name
        self.card = card
        self.__password = password
        self.__balance = balance
        self.phone = phone


user_card = BankCard("Uzcard", 8600_0609_8825_6393, "****", 120_634, 891_348_33_70)

print(user_card.name)
print(user_card.card)
print(user_card.__password)
print(user_card.__balance)
print(user_card.phone)

