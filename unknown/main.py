from dataclasses import dataclass
import os
import json
from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from typing import List

engine = create_engine('sqlite:///test.db', echo=True)
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


class Transcation(ABM):
    def deposit(self):
        pass

    def withdraw(self):
        pass

    def checkbalance(self):
        pass


if __name__ == '__main__':
    Base.metadata.create_all(bind=engine)
    run = ABM()
    account_no = run.check_account("abc")
    if account_no:
        user_pin = "1234"
        check = run.check_account(account_no, user_pin)
        if check:
            print("what u want to do")
            print()
    else:
        print("no account was found on the number")
