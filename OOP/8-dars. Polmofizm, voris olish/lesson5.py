from uuid import uuid4


class Bank:
    def __init__(self, name, date, bank_card, bank_balance):
        self.name = name
        self.date = date
        self.__bank_id = uuid4()
        self.__bank_card = "3444 5566 7788 9900"

        self.__bank_balance = bank_balance


class Card(Bank):
    def __init__(self, name=None, bank_card=None, bank_balance=None, first_name=None, last_name=None, phone=None,
                 card=None, date=None, balance=None, password=None):
        super().__init__(name, date, bank_card, bank_balance)
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.card = card
        self.__balance = balance
        self.__password = password

    def get_bank_card(self):
        return self.__bank_card


card1 = Card()
card1.get_bank_card()
