from dataclasses import dataclass
import os
import json
from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from typing import List

engine = create_engine('sqlite:///test.db')
Base = declarative_base()
Session = sessionmaker(bind=engine)


class Account(Base):
    __tablename__ = 'account'

    id = Column(Integer, primary_key=True)
    account_no = Column(String)
    pin = Column(String)
    amount = Column(Integer)


class ABM:
    def __init__(self, load_data: bool = False):
        self.session = Session()
        if load_data:
            self.load_account()

    def load_account(self) -> List[Account]:
        _file_path = os.path.abspath('./accounts.json')
        with open(_file_path, 'rb') as d:
            json_data = json.loads(d.read())
        _account_list: list = []
        for index, account in enumerate(json_data.keys()):
            _account_list.append(
                Account(
                    id=index,
                    account_no=account,
                    pin=json_data[account]['pin'],
                    amount=json_data[account]['amount']
                )
            )
        self.session.bulk_save_objects(_account_list)
        self.session.commit()
        return _account_list

    def check_account(self, account_no):
        account = self.session.query(Account).filter(Account.account_no == account_no).first()
        return account

    def check_pin(self, account: Account, pin: str):
        if pin == account.pin:
            return True
        else:
            return False


class Transcation:
    def __init__(self):
        self.session = Session()

    def deposit(self, account_no, amount):
        self.session.query(Account).filter(Account.account_no == account_no).update(
            {Account.amount: Account.amount + amount}, synchronize_session='evaluate')
        self.session.commit()

    def withdraw(self, account_no, amount):
        original_balance = self.checkbalance(account_no)
        if original_balance >= amount:
            self.session.query(Account).filter(Account.account_no == account_no).update(
                {Account.amount: Account.amount - amount}, synchronize_session='evaluate')
            self.session.commit()

    def checkbalance(self, account_no):
        user = self.session.query(Account).filter(Account.account_no == account_no).first()
        return user.amount

    def transfer(self, original_account_no, balance, trans_account_no):
        original_bal = self.checkbalance(original_account_no)
        if original_bal >= balance:
            self.withdraw(original_account_no, balance)
            self.deposit(trans_account_no, balance)
            return "Transfer complete"
        else:
            return "Not sufficient balance"


if __name__ == '__main__':
    Base.metadata.create_all(bind=engine)
    run = ABM()
    original_account_no = input("Provide account no to login:")
    account_no = run.check_account(original_account_no)
    if account_no:
        user_pin = input("Provide the pin for account!")
        check = run.check_pin(account_no, user_pin)
        if check:
            print("what u want to do")
            trans = Transcation()
            while True:
                options = input("Choose Options\n1.Deposit\n2.withdraw\n3.checkBalance\n4.transfer\n5.quit")
                if options == '1' or options.lower() == 'deposit':
                    print("Deposit")
                    try:
                        amount = int(input("how much u want to deposit"))
                    except ValueError as _:
                        print("Provide only int value")
                    trans.deposit("12234324", amount)
                elif options == '2' or options.lower() == 'withdraw':
                    print("withdraw")
                    try:
                        amount = int(input("how much u want to withdraw"))
                    except ValueError as _:
                        print("Provide only int value")
                    trans.withdraw("12234324", amount)
                elif options == '3' or options.lower() == 'checkbalance':
                    print("checkbalance")
                    print(trans.checkbalance(original_account_no))
                elif options == '4' or options.lower() == 'transfer':
                    transfer_account = input("Enter which account to transfer")
                    try:
                        amount = int(input("Amount to transfer"))
                    except ValueError as _:
                        print("Provide only int value")
                    print(trans.transfer(original_account_no, amount, transfer_account))
                else:
                    break
    else:
        print("no account was found on the number")
