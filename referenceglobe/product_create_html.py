import requests
from bs4 import BeautifulSoup
import re
from jinja2 import Environment, FileSystemLoader
import sys
import getopt


def get_data(url: str = None):
    if url:
        response = requests.get(url)
        if response.status_code == 200:
            parsed_src = BeautifulSoup(response.content, "html.parser")
            product_list = parsed_src.find(id="product-listing").select("div")
            table_data = [[
                "Product Title",
                "Model of the product",
                "Price",
                "weight",
                "Description",
                "Product Image",
            ]]

            for i in set(product_list):
                product_image = i.find("div", class_="listing-left back")
                if product_image:
                    product_image = product_image.find("a")
                    product_image = ("http://www.referenceglobe.com/zencart/" +
                                     product_image.find("img")["src"])

                product_details = i.find("div", class_="back listing-right")
                if product_details:
                    data = product_details.get_text().strip()
                    title = re.match(r"^.*(?=Model)", data, re.DOTALL)
                    title = title.group()

                    model = re.match(r"^.*(?<=Model:\s)(.*(?=Price))", data,
                                     re.MULTILINE)
                    model = model.group(1)

                    price = re.match(r"^.*(?<=Price:\s)(.*(?=Weight))", data,
                                     re.DOTALL)
                    price = price.group(1)

                    weight = re.match(r"^.*(?<=Weight:\s)(.*(?=Date))", data,
                                      re.DOTALL)
                    weight = weight.group(1)

                product_description = i.find(
                    "div", class_="clearBoth listings-description")
                if product_description:
                    product_description = product_description.get_text().strip(
                    )
                    table_data.append([
                        title,
                        model,
                        price,
                        weight,
                        product_description,
                        product_image,
                    ])
        return tuple(table_data)


def generate_html(count=2):
    url = "http://www.referenceglobe.com/zencart/index.php?main_page=products_new"
    print(f"calling url is {url}")
    table_list = get_data(url)
    file_loader = FileSystemLoader("templates")
    env = Environment(loader=file_loader)
    template = env.get_template("Table_ui.txt")
    output = template.render(table_list=table_list[:count + 1])
    with open("result.html", "w") as f:
        f.write(output)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        opts = ""
        try:
            opts, argvs = getopt.getopt(sys.argv[1:], "hc:")
        except getopt.GetoptError:
            print(
                "You can pass `product_create_html.py -c 2` for the number of result in the `result.html`\n default count is 2"
            )
        for opt, argv in opts:
            if opt == "-h":
                print(
                    "You can pass `product_create_html.py -c 2` for the number of result in the `result.html`\n default count is 2"
                )
            elif opt == "-c":
                generate_html(int(argv))
            else:
                print(opt, argv)
    else:
        print("\nexcuting the code with default value of total rows is 2")
        generate_html()
