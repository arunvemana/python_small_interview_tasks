import calendar


def days_count(year: int, month: int):
    """calculate the days with respected
    special days list and normal days list
    """
    special_sum = []
    normal_sum = []
    for month_cal in calendar.monthcalendar(year, month):
        normal_price_days = [calendar.MONDAY, calendar.TUESDAY, calendar.WEDNESDAY, calendar.THURSDAY,
                             calendar.FRIDAY]
        special_price_days = [calendar.SATURDAY, calendar.SUNDAY]
        special_price_count = list(map(lambda var: 1 if month_cal[var] != 0 else 0, special_price_days))
        special_sum.extend(special_price_count)
        normal_price_count = list(map(lambda var: 1 if month_cal[var] != 0 else 0, normal_price_days))
        normal_sum.extend(normal_price_count)

    return sum(special_sum), sum(normal_sum)


def index_run(year: int = 2020, special_price: int = 8, normal_price: int = 5):
    """Main function
    return: month_abbr and price"""
    months = [month_no for month_no in range(1, 12)]
    for month in months:
        special, normal = days_count(year, month)
        print(f"{calendar.month_abbr[month]} {year} - Rs.{special * special_price + normal * normal_price}")


# running the main function
input_value = []
has_input = input("Do u like to provided year,price?(Y/N)") or None
if has_input and (has_input.lower() == "y" or has_input.lower() == "yes"):
    for i in ["Please enter the Year:",
              "Please enter the Special Day Price:",
              "Please enter the Normal Day Price"]:
        input_value.append(int(input(i)))
    index_run(input_value[0], input_value[1], input_value[2])
else:
    index_run()
