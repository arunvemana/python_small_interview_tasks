from dataclasses import dataclass, asdict, field
from typing import List
from pydantic import BaseConfig

USER_INPUT = "User Input: "


class NotaValidInpit(Exception):
    pass


class OutOfOptions(Exception):
    pass


@dataclass
class Item:
    Product: str = None
    Brand: str = None
    Price: int = None
    Quantity: int = None
    Total_price: float = None


@dataclass
class Bill:
    CustomerName: str = None
    Items: List[Item] = field(default_factory=list)

    def addItem(self, item):
        self.Items.append(item)


class Store(BaseConfig):
    products = {"Soaps": [("Cintol", 10), ("Dettol", 10), ("Lux", 11)],
                "Chocolates": [("Cadbury", 11), ("Parley", 5), ("Parrys", 3)],
                "Dairy Products": [("milk", 13), ("curd", 10), ("buttermilk", 7)],
                "Vegetables & Fruits": [("apple", 50), ("mango", 40), ("bitterguard", 20)]}


def Purchase():
    _bill = Bill()
    S = Store()
    _bill.CustomerName = input(f"Please Enter the Customer's name \n {USER_INPUT}")
    display_products = ',\t'.join(map(lambda x: f'{x[0]} {x[1]}', enumerate(S.products.keys(), 1)))
    category_choice = input(
        f"Select the product types that the customer has Purchased\n{display_products}\n{USER_INPUT}")
    if not len(category_choice) > 0:
        raise OutOfOptions("please provide the choice")
    else:
        try:
            products = map(int, category_choice.split(','))
        except ValueError as _:
            raise NotaValidInpit("provide choice with ',' comma seperate")
        for product in products:
            _purchased = Item()
            product_name = list(S.products.keys())[product - 1]
            _purchased.Product = product_name
            brands = ',\t'.join(map(lambda x: f'{x[0]} {x[1][0]}', enumerate(S.products.get(product_name), 1)))
            try:
                brand_choice = int(input(f"Select the {product_name} brand\n{brands}\n{USER_INPUT}"))
            except ValueError as _:
                raise NotaValidInpit("Provide number and only one input")
            if not brand_choice:
                print("Please provide the choice")
            else:
                brand_name, price = S.products.get(product_name)[brand_choice - 1]
                _purchased.Brand = brand_name
                _purchased.Price = price
                try:
                    quantity = int(input(f"Please provide the Quantity of the {brand_name} {product_name} "))
                except ValueError as _:
                    raise NotaValidInpit("Provide as int and valid option")
                _purchased.Quantity = quantity
                _purchased.Total_price = price * quantity
                print(_purchased)
            _bill.addItem(_purchased)
    print(asdict(_bill))


if __name__ == '__main__':
    Purchase()
