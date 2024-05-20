class Vacancy:

    def __init__(self, name, salary, currency, url, requirement='Информация отсутствует'):
        self.name = name
        self.salary = salary
        self.currency = currency
        self.url = url
        self.requirement = requirement

    def __repr__(self):
        return f'Name: {self.name}\nSalary: {self.salary}\nCurrency: {self.currency}\nURL: {self.url}\nRequirement: {self.requirement}'
    
    def __gt__(self, other):
        """
        Compare two Vacancy objects based on their salary.

        Parameters:
            other (Vacancy): The Vacancy object to compare with.

        Returns:
            Vacancy or str: If both salaries are not None and self.salary['to'] > other.salary['to'], return self.
            Otherwise, return 'Зарплата не указана' if either salary is None.
        """
        if self.salary is not None and other.salary is not None:
            if self.salary['to'] > other.salary['to']:
                return self
            else:
                return other
        return 'Зарплата не указана'

    def __lt__(self, other):
        """
        Compare two Vacancy objects based on their salary.

        Parameters:
            other (Vacancy): The Vacancy object to compare with.

        Returns:
            Vacancy or str: If both salaries are not None and self.salary['to'] < other.salary['to'], return self.
            Otherwise, return 'Зарплата не указана' if either salary is None.
        """
        if self.salary is not None and other.salary is not None:
            if self.salary['to'] < other.salary['to']:
                return self
            else:
                return other
        return 'Зарплата не указана'