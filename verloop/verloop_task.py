# to retreive the data from the url
import requests
# to parse and find the details from the retreived data
from bs4 import BeautifulSoup
# to save in file
import json


def details_scrap(base_url: str):
    try:
        response = requests.get(base_url).text
        soup = BeautifulSoup(response, "lxml")
        output = {}
        # loop for the required text from html elements
        for details in soup.find_all(class_="leftContainer"):
            book_title = details.find('h1').text.strip()
            average_rating = details.find('span', attrs={'itemprop': 'ratingValue'}).text.strip()
            rating_count = details.find('meta', attrs={'itemprop': 'ratingCount'}).get('content')
            num_pages = details.find('span', attrs={'itemprop': 'numberOfPages'}).text.split()[0]
            publication_year = details.find('div', attrs={'id': 'details'}).find_all('div', attrs={'class': 'row'})[
                1].text.strip()
            # finding the year and month from the string
            _temp_list = publication_year.split()
            publication_year = _temp_list[-1]
            for index, month_year in enumerate(_temp_list):
                if month_year.isdigit():
                    re_published = f"{_temp_list[index - 1]} {_temp_list[index]}"
                    break
            # image_url = details.find('a',attrs={'itemprop':'image'})['href']
            image_url = details.find('div', attrs={'class': 'editionCover'}).find('img')['src']
            _authors = details.find_all('div', attrs={'class': 'authorName__container'})
            authors = ''
            for extract_names in _authors:
                authors += extract_names.text.strip()

            # adding data 
            output['book_title'] = book_title
            output['average_rating'] = average_rating
            output['rating_count'] = rating_count
            output['num_pages'] = num_pages
            output['image_url'] = image_url
            output['publication_year'] = publication_year.strip(')')
            output['re_published_year'] = re_published
            output['authors'] = authors
            # saving the output to the file for sample view
            with open("output.json", "w") as f:
                json.dump(output, f)
            return json.dumps(output, indent=1)
    except requests.exceptions.ConnectionError:
        return "raise an exception InvalidGoodreadsURL"
    except AttributeError:
        return "raise an exception InvalidGoodreadsURL"


# print(details_scrap("https://www.goodreads.com/book/show/12067.Good_Omens"))


print(details_scrap(input("enter your full url:-")))
