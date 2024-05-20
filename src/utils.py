from src.vacancy import Vacancy
from src.parser_vacancy import ParserVacancy

CRITERIA_COMMAND = {
    1: 'help - вызвать список критерий',
    2: 'name - поиск вакансий по имени',
    3: 'salary_from - зарплата от',
    4: 'salary_to - зарплата до',
    5: 'sorted_salary_from - сортировка по зарплате от',
    6: 'sorted_salary_to - сортировка по зарплате до',
    7: 'top_n - топ N вакансий',
    8: 'add - добавить фильтры',
    9: 'done - применить фильтры',
    10: 'clear - очистить фильтры',
    11:' stop - выйти и отменить фильтры',
}

PARAMS_ADDED = {
    'name': 'Название вакансии',
    'salary_from': 'Зарплата от',
    'salary_to': 'Зарплата до',
    'sorted_salary_from': 'Сортировка по зарплате от',
    'sorted_salary_to': 'Сортировка по зарплате до',
    'top_n': 'Топ N вакансий',
    'add': 'Добавить критерии поиска',
    'done': 'Применить критерии поиска',
    'clear': 'Очистить критерии поиска',
}

def menu():
    message = 'Доступные команды:\n1. help - вызвать список команд\n2. search - поиск вакансий\n3. exit - выход из программы\n'
    return message

def get_info_commands_criteria():
    print('Доступные критерии поиска:')
    message =  [message for message in CRITERIA_COMMAND.values()]
    return '\n'.join(message)

def get_params_info_commands_criteria(params: dict):
    print('Добавлены следующие критерии поиска:')
    count = 0
    message = []
    for p in params.values():
        count += 1
        message.append(f'\t{count}: {p}')
    return '\n'.join(message)