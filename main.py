from src.hh_api import FromHHru
from src.parser_vacancy import ParserVacancy
from src.saver import JSONSaver
import src.utils as utils


def interface():
    """Функция для взаимодействия с пользователем"""

    print('Добро пожаловать в интерактивный поиск вакансий на сайте hh.ru \n')
    print('Для получения доступных команд введите help \n')

    while True:
        cmd = input(utils.menu())
        if cmd == 'help' or cmd == '1':
            cmd = input(utils.menu())

        if cmd == 'search' or cmd == '2':
            user_vacancy = input(
                'Введите вакансию для поиска на сайте hh.ru: \n')
            hh = FromHHru()
            vacancies = hh.get_vacancies(user_vacancy)

            pv = ParserVacancy(data=vacancies)
            parse_vacansy = pv.parse_vacansys()
            saver = JSONSaver()
            res = {"items": parse_vacansy}
            saver = saver.save(res)

            print(f'Найдено: {len(parse_vacansy)} вакансий по запросу "{user_vacancy}" и сохранено в файл вакансий в {saver.get_path()}')

            b = input('Требуется ли добавить фильтры к вакансиям да/нет: \n')

            if b == 'да':
                while True:
                    params = {}

                    sub_cmd = input(utils.get_info_commands_criteria())

                    if sub_cmd == 'stop' or sub_cmd == '11':
                        break

                    if sub_cmd == 'help' or sub_cmd == '1':
                        sub_cmd = input(utils.get_info_commands_criteria())

                    if sub_cmd == 'name' or sub_cmd == '2':
                        name_vac = input('Введите название вакансии: \n')
                        params['name'] = name_vac
                        utils.get_params_info_commands_criteria(params)

                    if sub_cmd == 'salary_from' or sub_cmd == '3':
                        salary_from = input('Введите зарплату от: \n')
                        params['salary_from'] = salary_from
                        utils.get_params_info_commands_criteria(params)

                    if sub_cmd == 'salary_to' or sub_cmd == '4':
                        salary_to = input('Введите зарплату до: \n')
                        params['salary_to'] = salary_to
                        utils.get_params_info_commands_criteria(params)

                    if sub_cmd == 'sorted_salary_from' or sub_cmd == '5':
                        params['sorted_salary_from'] = True
                        utils.get_params_info_commands_criteria(params)

                    if sub_cmd == 'sorted_salary_to' or sub_cmd == '6':
                        params['sorted_salary_to'] = True
                        utils.get_params_info_commands_criteria(params)

                    if sub_cmd == 'top_n' or sub_cmd == '7':
                        top_n = input('Введите топ N вакансий: \n')
                        params['top_n'] = top_n
                        utils.get_params_info_commands_criteria(params)

                    if sub_cmd == 'add' or sub_cmd == '8':
                        parse_vacansy = pv.parse_vacansys(params)
                        print("Фильтры добавлены применены к вакансиям")
                        res['items'] = parse_vacansy
                        saver.save(res)
                        print(f'Найдено: {len(parse_vacansy)} вакансий по запросу "{user_vacancy}" и сохранено в файл вакансий в {saver.get_path()}')
                        sub_cmd = 'clear'

                    if sub_cmd == 'done' or sub_cmd == '9':
                        break

                    if sub_cmd == 'clear' or sub_cmd == '10':
                        params = {}
                        print('Фильтры очищены')
                        sub_cmd = input(utils.get_info_commands_criteria())

            name_exit = input('Хотите очистить файл вакансий да/нет: \n')

            if name_exit == 'да' or name_exit == 'yes' or name_exit == 'y' or name_exit == 'Y':
                saver.delete()
                print('Файл вакансий очищен')
                cmd = input(utils.menu())

        if cmd == 'exit' or cmd == '3':
            print(
                'До свидания, спасибо за использование интерактивного поиска вакансий на сайте hh.ru')
            break

interface()