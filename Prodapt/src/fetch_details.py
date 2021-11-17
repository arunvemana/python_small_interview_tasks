import requests
from src.custom_typing_hint import Url, Url_response
import logging


def get_livescore_card_hmtl(url: Url) -> Url_response:
    try:
        score_card = requests.get(url)
        return score_card.content
    except requests.exceptions.RequestException as Error:
        logging.exception(Error)


def get_livescore_html(url: Url) -> Url_response:
    try:
        page_html = requests.get(url)
        return page_html.content
    except requests.exceptions.RequestException as Error:
        logging.exception(Error)
