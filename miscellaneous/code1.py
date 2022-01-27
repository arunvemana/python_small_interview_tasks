import requests
import json
from typing import List

QUESTION = "Get the data from the API https://gorest.co.in/public/v1/posts and print data create the list\n \
containing all user_id in above API and print it"
OBSERVATION = "This api response contain pagination so have to consider that for all user_id"


class ISawAProblem(Exception):
    """Custom Exception"""
    pass


class main():
    def __init__(self):
        self.base_url = "https://gorest.co.in/public/v1/posts"
        self.pagination_param = "page"  # page=1
        self.output: list = []

    def get_response(self, page_no: int) -> json:
        params = {self.pagination_param: page_no}
        data = requests.get(self.base_url, params=params)
        if data.status_code == 200:
            return data.json()
        else:
            raise ISawAProblem("Not having a 200 response")

    def get_user_id(self, data: List[dict]) -> List[int]:
        _user_id: int = []
        for user in data:
            try:
                _user_id.append(user['user_id'])
            except KeyError as _:
                raise ISawAProblem("not having a user_id in the response")
        return _user_id

    def run(self):
        page_count = 0
        while True:
            try:
                data = self.get_response(page_count)['data']
                if data:
                    self.output.extend(self.get_user_id(data))
                    print(page_count)
                    page_count += 1
                else:
                    return self.output
            except ISawAProblem as e:
                print(f"Error caused by {e}")
                break


if __name__ == "__main__":
    start = main()
    user_ids = start.run()
    print("TOTAL NO OF USER_IDS is:", len(user_ids))
    print(user_ids)
    print("TOTAL NO OF UNIQUE USER_IDS IS:", len(set(user_ids)))
    print(set(user_ids))
