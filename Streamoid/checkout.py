# calculating checkout price out


class Checkout:
    def __init__(self, offer={}):
        self.item = {}
        self.offers = offer
        self.data = {
            "stv": {"name": "Sony Tv", "price": 549.99},
            "cac": {"name": "Central AC", "price": 1399.99},
            "nsh": {"name": "Nike Shoe", "price": 109.50},
            "mch": {"name": "Charger", "price": 30.00},
        }

    def scan(self, item):
        if self.item.get(item):
            self.item[item] += 1
        else:
            self.item[item] = 1

    def total(self):
        if self.offers.get("offers"):
            for item_name in self.offers["offers"]:
                if self.item.get(item_name) and self.item[item_name] >= int(
                    self.offers["offers"][item_name][0]
                ):
                    scanned_count = self.item[item_name]
                    self.item[item_name] = (
                        scanned_count
                        / int(self.offers["offers"][item_name][0])
                        * self.offers["offers"][item_name][1]
                    ) + scanned_count % int(self.offers["offers"][item_name][0])

        if self.offers.get("discount"):
            for item_name in self.offers["discount"]:
                if self.item.get(item_name) and self.item[item_name] >= int(
                    self.offers["discount"][item_name][0]
                ):
                    discount_price = self.offers["discount"][item_name][1]
                    # replacing the original price with discount price
                    self.data[item_name]["price"] = discount_price

        if self.offers.get("free"):
            for item_name in self.offers["free"]:
                if self.item.get(item_name):
                    for each_free_item in self.offers["free"][item_name]:
                        self.item[each_free_item] = (
                            self.item.get("each_free_item", 0) - 1
                        )
        # cal
        total_sum = 0
        for each_item in self.item:
            if self.item[each_item] > 0:
                total_sum += self.item[each_item] * self.data[each_item]["price"]
        return total_sum


def test_run():
    test_cases = [
        ["nsh", "nsh", "nsh", "mch"],
        ["nsh", "stv", "stv", "nsh", "stv", "stv", "stv"],
        ["cac", "mch", "stv"],
    ]

    for test_case in test_cases:
        d = Checkout(
            {
                "offers": {"nsh": (3, 2)},
                "discount": {"stv": (4, 499.99)},
                "free": {"cac": ["mch"]},
            }
        )

        for item in test_case:
            d.scan(item)
        print(u"\u0024" + str(d.total()))


data = {
    "offer": {"item_name": ("count", "actual count")},
    "discount": {"tem_name": ("offer_count", "value")},
    "free": {"item_name": ["free item list"]},
}

if __name__ == "__main__":
    test_run()
