from abstract_class import AbstractHH
import requests

BASE_API_HH_URL = 'https://api.hh.ru/vacancies'


class FromHHru(AbstractHH):
    """
    Class for connecting to HH API and retrieving vacancies.

    Parameters:
        url_get (str, optional): The URL to get vacancies from. Defaults to 'https://api.hh.ru/vacancies'.
    """

    def __init__(self, url_get=BASE_API_HH_URL):
        """
        Initializes a new instance of the class.

        Parameters:
            url_get (str, optional): The URL to get vacancies from. Defaults to 'https://api.hh.ru/vacancies'.
        """
        self.url_get = url_get

    def __repr__ (self):
        """
        Returns a string representation of the object.

        Returns:
            str: The string representation of the object, which includes the API URL.
        """
        return f'Api url: {self.url_get}'

    def get_vacancies(self, keyword):
        """
        Retrieves a list of vacancies from the API based on the provided keyword.

        Parameters:
            keyword (str): The keyword to search for in the vacancy descriptions.

        Returns:
            list: A list of vacancy objects containing information such as title, description, salary, and location.
        """
        params = {'text': keyword, 'page': 0, 'per_page': 100}
        response = requests.get(self.url_get, params=params)
        
        if response.status_code != 200:
            raise Exception(f'Error: {response.status_code} - {response.text}')
        

        return response.json()['items']
