class Vacancy:
    """
    Represents a vacancy in the HH.ru system.

    Attributes:
        name (str): The title of the vacancy.
        salary (dict): The salary of the vacancy in the format {from: int, to: int}.
        currency (str): The currency of the salary.
        url (str): The URL of the vacancy.
        requirement (str, optional): The requirement for the vacancy. Defaults to 'Информация отсутствует'.

    Methods:
        __repr__ (str): Returns a string representation of the object.
    """
    def __init__(self, name, salary, currency, url, requirement='Информация отсутствует'):
        self.name = name
        self.salary = salary
        self.currency = currency
        self.url = url
        self.requirement = requirement

    def __repr__(self):
        return f'Name: {self.name}\nSalary: {self.salary}\nCurrency: {self.currency}\nURL: {self.url}\nRequirement: {self.requirement}'
