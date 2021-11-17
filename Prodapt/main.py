from src.fetch_details import get_livescore_html, get_livescore_card_hmtl
from src.parse_details import scorecard_parsing, get_details, get_score_card_number
import logging
logging.basicConfig(level=logging.INFO)

# Url\'s information
url = "https://www.cricbuzz.com/api/html/cricket-scorecard/"
livescore_url = "https://www.cricbuzz.com/cricket-match/live-scores"
recent_score_url = "https://www.cricbuzz.com/cricket-match/live-scores/recent-matches"
FILENAME = 'Match Details.json'

if __name__ == '__main__':
    logging.info(f"Getting the detail from {livescore_url}")
    body = get_livescore_html(livescore_url)
    number = get_score_card_number(body)
    if number:
        url = url + number
    else:
        logging.info("No live match found moving to ")
        logging.info(f"Getting details from {recent_score_url}")
        body = get_livescore_html(recent_score_url)
        number = get_score_card_number(body)
        url = url + number
    data = get_livescore_card_hmtl(url)
    parsed_data = scorecard_parsing(data)
    details = get_details(parsed_data)
    with open(FILENAME, 'w') as f:
        f.write(str(details))
        logging.info(f"Match Details saved in {FILENAME}")
