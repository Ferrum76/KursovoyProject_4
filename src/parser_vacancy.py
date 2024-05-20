from .abstract_class import Parser
from .vacancy import Vacancy


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
        res = self.__creating_a_list_of_instances()
        if filter_words is not None and len(filter_words) > 0:
            res = self.__filter_vacancies(res, filter_words)
        if salary_from is not None and salary_to is not None and salary_from < salary_to and salary_to > 0 and salary_from > 0:
            res = self.__get_vacancies_by_salary(res, salary_from, salary_to)
        if sort_salary_from:
            res = self.__sort_vacancies_from(res)
        if sort_salary_to:
            res = self.__sort_vacancies_to(res)
        if top_n is not None and top_n > 0:
            res = self.__get_top_vacancies(res, top_n)
        return res

    def __filter_vacancies(self, data: list, filter_words: list) -> list[dict]:
        """
        Filters the list of vacancy instances based on the given filter words.

        Args:
            filter_words (list): A list of words to filter the vacancy instances.

        Returns:
            list: A list of filtered vacancy instances.

        This function iterates over each vacancy instance in the list and checks if any of the filter words are present in the instance's name. If a filter word is found, the instance is added to the `filter_vacancies` list. The `list_instances` attribute is then updated with the `filter_vacancies` list.

        Example:
            >>> parser = ParserVacancy([Vacancy("Python Developer", "Python developer needed", 100, 200, "https://example.com/vacancy1"), Vacancy("Java Developer", "Java developer needed", 200, 300, "https://example.com/vacancy2")])
            >>> parser.__filter_vacancies(["Python"])
            [Vacancy("Python Developer", "Python developer needed", 100, 200, "https://example.com/vacancy1")]
        """
        filter_vacancies = []
        for instance in data:
            for word in filter_words:
                if word.lower().strip() in instance.name.lower():
                    filter_vacancies.append(instance)
                    break
        return filter_vacancies

    def __get_vacancies_by_salary(self, data: list, salary_from: int, salary_to: int) -> list[dict]:
        """
        Filters the list of vacancy instances based on the given salary range.

        Args:
            salary_from (int): The minimum salary range.
            salary_to (int): The maximum salary range.

        Returns:
            list: A list of vacancy instances whose salary range falls within the given range.

        This function iterates over each vacancy instance in the list and checks if the salary range of the instance falls within the given range. If the salary range is within the range, the instance is added to the `ranged_vacancies` list. Finally, the `list_instances` attribute is updated with the `ranged_vacancies` list.

        Example:
            >>> parser = ParserVacancy([Vacancy("Python Developer", "Python developer needed", 100, 200, "https://example.com/vacancy1"), Vacancy("Java Developer", "Java developer needed", 200, 300, "https://example.com/vacancy2")])
            >>> parser.__get_vacancies_by_salary(150, 250)
            [Vacancy("Python Developer", "Python developer needed", 100, 200, "https://example.com/vacancy1")]

        Raises:
            ValueError: If the salary range is not valid.
        """
        try:
            # Create an empty list to store the filtered vacancy instances
            ranged_vacancies = []

            # Iterate over each vacancy instance in the list
            for instance in data:
                # If the salary_from attribute is None, set it to 0
                if instance.salary_from is None:
                    instance.salary_from = 0

                # If the salary_to attribute is None, set it to 0
                if instance.salary_to is None:
                    instance.salary_to = 0

                # Check if the salary range of the instance falls within the given range
                if salary_from <= instance.salary_from and salary_to >= instance.salary_to:
                    # If the salary range is within the range, add the instance to the ranged_vacancies list
                    ranged_vacancies.append(instance)

            # Return the filtered list of vacancy instances
            return ranged_vacancies
        except ValueError:
            print("Диапазон выбран некорректно")

    def __sort_vacancies_from(self, data: list) -> list[dict]:
        """
        Sorts the list of vacancy instances in descending order based on the `salary_from` attribute.

        Returns:
            list[dict]: A sorted list of vacancy instances.

        This function is used to sort the list of vacancy instances based on the `salary_from` attribute in descending order.
        The sorted list is then updated in the `list_instances` attribute.

        Example:
            >>> parser = ParserVacancy([Vacancy("Python Developer", "Python developer needed", 100, 200, "https://example.com/vacancy1"), Vacancy("Java Developer", "Java developer needed", 200, 300, "https://example.com/vacancy2")])
            >>> parser.__sort_vacancies_from()
            [Vacancy("Java Developer", "Java developer needed", 200, 300, "https://example.com/vacancy2"), Vacancy("Python Developer", "Python developer needed", 100, 200, "https://example.com/vacancy1")]
        """
        if not data:
            print("Список вакансий пуст", data)
            return []
        sorted_vacancies = sorted(
            data, key=lambda x: x.salary_from, reverse=True)
        return sorted_vacancies

    def __sort_vacancies_to(self, data: list[dict]) -> list[dict]:
        """
        Sorts the list of vacancy instances in descending order based on the `salary_to` attribute.

        Returns:
            list[dict]: A sorted list of vacancy instances.

        This function is used to sort the list of vacancy instances based on the `salary_to` attribute in descending order.
        The sorted list is then updated in the `list_instances` attribute.

        Example:
            >>> parser = ParserVacancy([Vacancy("Python Developer", "Python developer needed", 200, 300, "https://example.com/vacancy1"), Vacancy("Java Developer", "Java developer needed", 100, 200, "https://example.com/vacancy2")])
            >>> parser.__sort_vacancies_to()
                [Vacancy("Java Developer", "Java developer needed", 100, 200, "https://example.com/vacancy2"), Vacancy("Python Developer", "Python developer needed", 200, 300, "https://example.com/vacancy1")]
        """
        sorted_vacancies = sorted(
            data, key=lambda x: x.salary_to, reverse=True)
        return sorted_vacancies

    def __get_top_vacancies(self, data: list[dict], top_n: int) -> list[dict]:
        """
        Gets the top `top_n` vacancies from the list of instances and updates the list of instances with the top vacancies.

        Parameters:
            top_n (int): The number of top vacancies to retrieve.

        Returns:
            list[dict]: A list of top `top_n` vacancies.

        Example:
            >>> parser = ParserVacancy([Vacancy("Python Developer", "Python developer needed", 100, 200, "https://example.com/vacancy1"), Vacancy("Java Developer", "Java developer needed", 200, 300, "https://example.com/vacancy2"), Vacancy("JavaScript Developer", "JavaScript developer needed", 300, 400, "https://example.com/vacancy3")])
            >>> parser.__get_top_vacancies(2)
            [Vacancy("JavaScript Developer", "JavaScript developer needed", 300, 400, "https://example.com/vacancy3"), Vacancy("Java Developer", "Java developer needed", 200, 300, "https://example.com/vacancy2")]

        """
        print(data)
        return data[:top_n]

    def __creating_dictionary_list(self) -> list[dict]:
        """
        Creates a list of dictionaries containing information about vacancies.

        Returns:
            list[dict]: A list of dictionaries, where each dictionary represents a vacancy and contains the following keys:
                - "name" (str): The name of the vacancy.
                - "desc" (str): The description of the vacancy area.
                - "salary_from" (int or None): The minimum salary of the vacancy.
                - "salary_to" (int or None): The maximum salary of the vacancy.
                - currency (str): The currency of the salary.
                - "link" (str): The URL of the vacancy area.

        Raises:
            TypeError: If the data attribute is not a list.
        """
        if len(self.data) == 0:
            return []
        if isinstance(self.data, list):
            vacancies_list = []
            for item in self.data:
                vacancies_list.append({
                    "name": item['name'],
                    "desc": item['area']['name'],
                    "salary_from": item.get('salary', {}).get('from', None),
                    "salary_to": item.get('salary', {}).get('to', None),
                    "currency": item.get('salary', {}).get('currency', 'RUB'),
                    "link": item['area']['url'],
                    "requirement": item.get('snippet', {}).get('requirement', 'Информация отсутствует')}
                )

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
            return []

        if isinstance(data, list):
            vacancies_list = []
            for item in data:
                vacancy_ex = Vacancy(
                    item["name"],
                    item["desc"],
                    item["salary_from"],
                    item["salary_to"],
                    item["currency"],
                    item["link"],
                    item["requirement"]
                )
                vacancies_list.append(vacancy_ex)

            return vacancies_list
        else:
            raise TypeError
