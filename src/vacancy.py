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
    def __init__(self, name: str, desc: str, salary_from: int, salary_to: int, currency: str, url: str, requirement: str='Информация отсутствует'):
        self.name = name
        self.desc = desc
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.currency = currency
        self.url = url
        self.requirement = requirement

    def __repr__(self):
        return f"Vacancy(name={self.name}, desc={self.desc}, salary_from={self.salary_from}, salary_to={self.salary_to}, currency={self.currency}, url={self.url}, requirement={self.requirement})"
