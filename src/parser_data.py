from abstract_class import Parser
from vacancy import Vacancy


class ParserVacancy(Parser):
    def __init__(self, data: list):
        self.data = data
        self.list_instances = self.__creating_a_list_of_instances()

    def __repr__(self):
        return f'Data: {self.data}'

    def get_vacancys(
        self,
        filter_words: list = None,
        salary_from: int = None,
        salary_to: int = None,
        sort_salary_from: bool = False,
        sort_salary_to: bool = False,
        top_n: int = None
    ) -> list[Vacancy]:
        if filter_words is not None:
            self.__filter_vacancies(filter_words)
        if salary_from is not None and salary_to is not None:
            self.__get_vacancies_by_salary(salary_from, salary_to)
        if sort_salary_from:
            self.__sort_vacancies_from()
        if sort_salary_to:
            self.__sort_vacancies_to()
        if top_n is not None:
            self.__get_top_vacancies(top_n)
        return self.list_instances

    def __filter_vacancies(self, filter_words: list):
        """
        Filters the list of vacancy instances based on the given filter words.

        Args:
            filter_words (list): A list of words to filter the vacancy instances.

        Returns:
            None

        This function iterates over each vacancy instance in the list and checks if any of the filter words are present in the instance's title. If a filter word is found, the instance is added to the `filter_vacancies` list. The `list_instances` attribute is then updated with the `filter_vacancies` list.

        Example:
            >>> parser = ParserVacancy([Vacancy("Python Developer", "Python developer needed", 100, 200, "https://example.com/vacancy1"), Vacancy("Java Developer", "Java developer needed", 200, 300, "https://example.com/vacancy2")])
            >>> parser.__filter_vacancies(["Python"])
            >>> parser.list_instances
            [Vacancy("Python Developer", "Python developer needed", 100, 200, "https://example.com/vacancy1")]
        """
        filter_vacancies = []
        for instance in self.list_instances:
            for word in filter_words:
                if word.lower().strip() in instance.title.lower():
                    filter_vacancies.append(instance)
                    break
        self.list_instances = filter_vacancies

    def __get_vacancies_by_salary(self, salary_from: int, salary_to: int):
        """
        Filters the list of vacancy instances based on the given salary range.

        Args:
            salary_from (int): The minimum salary range.
            salary_to (int): The maximum salary range.

        Returns:
            None

        This function iterates over each vacancy instance in the list and checks if the salary range of the instance falls within the given range. If the salary range is within the range, the instance is added to the `ranged_vacancies` list. Finally, the `list_instances` attribute is updated with the `ranged_vacancies` list.

        Example:
            >>> parser = ParserVacancy([Vacancy("Python Developer", "Python developer needed", 100, 200, "https://example.com/vacancy1"), Vacancy("Java Developer", "Java developer needed", 200, 300, "https://example.com/vacancy2")])
            >>> parser.__get_vacancies_by_salary(150, 250)
            >>> parser.list_instances
            [Vacancy("Python Developer", "Python developer needed", 100, 200, "https://example.com/vacancy1")]

        Raises:
            ValueError: If the salary range is not valid.
        """
        try:
            ranged_vacancies = []
            for instance in self.list_instances:
                if instance.salary_from is None:
                    instance.salary_from = 0
                if instance.salary_to is None:
                    instance.salary_to = 0
                if instance.salary_from >= salary_from and instance.salary_to <= salary_to:
                    ranged_vacancies.append(instance)
            self.list_instances = ranged_vacancies
        except ValueError:
            print("Диапазон выбран некорректно")

    def __sort_vacancies_from(self):
        """
        Sorts the list of vacancy instances in descending order based on the `salary_from` attribute.

        Returns:
            list[dict]: A sorted list of vacancy instances.

        This function is used to sort the list of vacancy instances based on the `salary_from` attribute in descending order.
        The sorted list is then updated in the `list_instances` attribute.

        Example:
            >>> parser = ParserVacancy([Vacancy("Python Developer", "Python developer needed", 100, 200, "https://example.com/vacancy1"), Vacancy("Java Developer", "Java developer needed", 200, 300, "https://example.com/vacancy2")])
            >>> parser.__sort_vacancies_from()
            >>> parser.list_instances
            [Vacancy("Java Developer", "Java developer needed", 200, 300, "https://example.com/vacancy2"), Vacancy("Python Developer", "Python developer needed", 100, 200, "https://example.com/vacancy1")]
        """
        sorted_vacancies = sorted(
            self.list_instances, key=lambda x: x.salary_from, reverse=True)
        self.list_instances = sorted_vacancies

    def __sort_vacancies_to(self):
        """
        Sorts the list of vacancy instances in descending order based on the `salary_to` attribute.

        Returns:
            list[dict]: A sorted list of vacancy instances.

        This function is used to sort the list of vacancy instances based on the `salary_to` attribute in descending order.
        The sorted list is then updated in the `list_instances` attribute.

        Example:
            >>> parser = ParserVacancy([Vacancy("Python Developer", "Python developer needed", 200, 300, "https://example.com/vacancy1"), Vacancy("Java Developer", "Java developer needed", 100, 200, "https://example.com/vacancy2")])
            >>> parser.__sort_vacancies_to()
            >>> parser.list_instances
                [Vacancy("Java Developer", "Java developer needed", 100, 200, "https://example.com/vacancy2"), Vacancy("Python Developer", "Python developer needed", 200, 300, "https://example.com/vacancy1")]
        """
        sorted_vacancies = sorted(
            self.list_instances, key=lambda x: x.salary_to, reverse=True)
        self.list_instances = sorted_vacancies

    def __get_top_vacancies(self, top_n: int):
        """
        Gets the top `top_n` vacancies from the list of instances and updates the list of instances with the top vacancies.

        Parameters:
            top_n (int): The number of top vacancies to retrieve.

        Returns:
            None

        Example:
            >>> parser = ParserVacancy([Vacancy("Python Developer", "Python developer needed", 100, 200, "https://example.com/vacancy1"), Vacancy("Java Developer", "Java developer needed", 200, 300, "https://example.com/vacancy2"), Vacancy("JavaScript Developer", "JavaScript developer needed", 300, 400, "https://example.com/vacancy3")])
            >>> parser.__get_top_vacancies(2)
            >>> parser.list_instances
            [Vacancy("JavaScript Developer", "JavaScript developer needed", 300, 400, "https://example.com/vacancy3"), Vacancy("Java Developer", "Java developer needed", 200, 300, "https://example.com/vacancy2")]

        """
        top_vacancies = self.list_instances[:top_n]
        self.list_instances = top_vacancies

    def __creating_dictionary_list(self) -> list[dict]:
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
                salary_from = item['salary'].get(
                    'from') if item['salary'] else None
                salary_to = item['salary'].get(
                    'to') if item['salary'] else None
                vacancies_list.append(
                    {"title": item['name'], "desc": item['area']['name'], "salary_from": salary_from, "salary_to": salary_to,
                     "link": item['area']['url']})
            return vacancies_list
        else:
            raise TypeError

    def __creating_a_list_of_instances(self) -> list[Vacancy]:
        """
        Creates a list of instances of the Vacancy class based on the data attribute.

        Returns:
            list[Vacancy]: A list of Vacancy instances.

        Raises:
            TypeError: If the data attribute is not a list of dictionaries.
        """
        data = self.__creating_dictionary_list()
        if len(data) == 0:
            return None

        if isinstance(data, list[dict]):
            vacancies_list = []
            for item in self.vacancies_list:
                vacancy_ex = Vacancy(
                    item["title"], item["desc"], item["salary_from"], item["salary_to"], item["link"])
                vacancies_list.append(vacancy_ex)

            return vacancies_list
        else:
            raise TypeError
