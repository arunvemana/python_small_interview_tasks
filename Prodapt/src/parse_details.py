from bs4 import BeautifulSoup
from dataclasses import dataclass, field, fields, asdict
from src.custom_typing_hint import Url_response, CricbuzzResponse
from typing import List, Union
import re
import json
import logging


@dataclass
class BatterTable:
    Batter: str = None
    Status: str = ''
    R: int = 0
    B: int = 0
    Fours: int = 0
    Sixes: int = 0
    SR: float = 0.0


@dataclass
class BowlerTable:
    Bowler: str = None
    O: str = None
    M: str = None
    R: str = None
    W: str = None
    NB: str = None
    WD: str = None
    ECO: str = None


@dataclass
class Innings:
    CountryName: str = None
    Score: str = None
    Batter: BatterTable = field(default_factory=BatterTable)
    Bowler: BowlerTable = field(default_factory=BowlerTable)


@dataclass
class OutputStructure:
    MatchStatus: str = None
    TotalInnings: List[Innings] = field(default_factory=Innings)

    def __repr__(self):
        return json.dumps(asdict(self))


def scorecard_parsing(scorecard: Url_response) -> CricbuzzResponse:
    try:
        soup = BeautifulSoup(scorecard, 'html.parser')
        return soup
    except BeautifulSoup.ParserRejectedMarkup as Error:
        logging.exception(Error)


def batter_table(_table: CricbuzzResponse):
    try:
        _rows = []
        for row in _table:
            battertable = BatterTable()
            if len(fields(BatterTable)) == len(row.find_all('div')):
                for col_name, col_value in zip(fields(BatterTable), row.find_all('div')):
                    setattr(battertable, col_name.name, col_value.text)
                    # scoretable.Batter = col.text
                _rows.append(battertable)
        return _rows
    except AttributeError as Error:
        logging.exception(Error)


def bowler_table(_table: CricbuzzResponse):
    try:
        _rows = []
        for row in _table:
            bowlertable = BowlerTable()
            if len(fields(BowlerTable)) == len(row.find_all('div')):
                for col_name, col_value in zip(fields(BowlerTable), row.find_all('div')):
                    setattr(bowlertable, col_name.name, col_value.text)
                _rows.append(bowlertable)
        return _rows
    except AttributeError as Error:
        logging.exception(Error)


def get_details(res_body: CricbuzzResponse):
    try:
        var = OutputStructure()
        var.MatchStatus = res_body.find("div", class_="cb-scrcrd-status").text
        # innings = res_body.findAll('div', id_='innings_',partial=True)
        _list_innings = []
        for inning in res_body.select('div[id*="innings_"]'):
            _inning = Innings()
            _inning.CountryName = inning.find("div", class_="cb-scrd-hdr-rw").find('span').text
            _inning.Score = inning.find("span", class_="pull-right").text
            # Extraction of score table.
            table_details = inning.find_all("div", class_="cb-scrd-itms")
            _inning.Batter = batter_table(table_details)
            _inning.Bowler = bowler_table(table_details)
            # adding each innings
            _list_innings.append(_inning)
        var.TotalInnings = _list_innings
        return var
    except AttributeError as Error:
        logging.exception(Error)


def get_score_card_number(res_body: CricbuzzResponse) -> Union[str, None]:
    try:
        body = BeautifulSoup(res_body, 'html.parser')
        number_url = body.find(title="Scorecard")['href']
        var = re.search(r"(?<=\/)\d+(?=\/)", number_url)
        return var.group()
    except TypeError as Error:
        logging.exception(Error)
        return None
