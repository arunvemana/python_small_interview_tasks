import dateutil.parser
import pandas
import pandas as pd


def date_parse(date: str,format:str):
    # yourdate = dateutil.parser.parse(date)
    yourdate = pd.to_datetime(date)
    quarter = pd.Timestamp(yourdate).quarter
    year = pd.Timestamp(yourdate).year
    print(quarter, year)
    return format.format(quarter=quarter,year=year)

def question_2():
    year,quarter = 0,0
    sample = ['2015-12-31', '1/1/1995', '3Q16', '2021Q3']
    format = "{quarter}Q{year}"
    output  = [date_parse(date,format) for date in sample ]
    print(output)


if __name__ == '__main__':
    # date_parse('2021q3')
    question_2()
