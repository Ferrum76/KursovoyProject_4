from vacancy import Vacancy


class Parser:
    def __init__(self, data: list):
        self.data = data
        self.vacancies_list=self.creating_dictionary_list()

    def __repr__(self):
        return f'Data: {self.data}'
    
    def creating_dictionary_list(self) -> list[dict]:
        """
        Creates a list of dictionaries containing information about vacancies.

        Returns:
            list[dict]: A list of dictionaries, where each dictionary represents a vacancy and contains the following keys:
                - "title" (str): The title of the vacancy.
                - "desc" (str): The description of the vacancy area.
                - "salary_from" (int or None): The minimum salary of the vacancy.
                - "salary_to" (int or None): The maximum salary of the vacancy.
                - "link" (str): The URL of the vacancy area.

        Raises:
            TypeError: If the data attribute is not a list.
        """
        if len(self.data) == 0:
            return None
        if isinstance(self.data, list):
            vacancies_list = []
            for item in self.data:
                salary_from = item['salary'].get('from') if item['salary'] else None
                salary_to = item['salary'].get('to') if item['salary'] else None
                vacancies_list.append(
                    {"title": item['name'], "desc": item['area']['name'], "salary_from": salary_from, "salary_to": salary_to,
                    "link": item['area']['url']})
            return vacancies_list
        else:
            raise TypeError
        
        
    def creating_a_list_of_instances(self) -> list[Vacancy]:
        """
        Creates a list of instances of the Vacancy class based on the data attribute.

        Returns:
            list[Vacancy]: A list of Vacancy instances.

        Raises:
            TypeError: If the data attribute is not a list of dictionaries.
        """
        if len(self.data) == 0:
            return None
        
        if isinstance(self.data, list[dict]):
            vacancies_list = []
            for item in self.vacancies_list:
                vacancy_ex = Vacancy(item["title"], item["desc"], item["salary_from"], item["salary_to"], item["link"])
                vacancies_list.append(vacancy_ex)

            return vacancies_list
        else:
            raise TypeError