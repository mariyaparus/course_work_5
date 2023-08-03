from src.utils import table_add_data, create_table, csv_writer, clear_table, connection
from src.DBManager import DBManager


def user_interaction():
    """Функция для взаимодействия с пользователем"""

    create_db = input('Здравствуйте! Введите, пожалуйста, название вакансии для создания базы данных:\n')
    csv_writer(create_db)
    create_table()
    clear_table()
    table_add_data()
    connection.close()

    client = DBManager('vacancies')

    while True:
        try:
            choice_user = int(input(
                f'''\nВыберите информацию, которую хотите получить, и нажмите соответствующую цифру:\n                
1 - список всех компаний и количество вакансий у каждой компании
2 - список всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на вакансию
3 - средняя зарплата по вакансиям
4 - список всех вакансий, у которых зарплата выше средней
5 - список всех вакансий, в названии которых содержится ключевое слово, например “python”
0 - завершить работу программы\n
Ваша цифра:\n'''))
            if choice_user in [1, 2, 3, 4, 5]:
                if choice_user == 1:
                    get_info = client.get_companies_and_vacancies_count()
                    for v in get_info:
                        print(v)
                elif choice_user == 2:
                    get_vacancies = client.get_all_vacancies()
                    for v in get_vacancies:
                        print(v)
                elif choice_user == 3:
                    avg_salary = client.get_avg_salary()
                    print(avg_salary)
                elif choice_user == 4:
                    higher_salary = client.get_vacancies_with_higher_salary()
                    for v in higher_salary:
                        print(v)
                elif choice_user == 5:
                    user_keyword = input('Введите ключевое слово для поиска по вакансиям:\n')
                    vac_with_keyword = client.get_vacancies_with_keyword(user_keyword)
                    for v in vac_with_keyword:
                        print(v)
            elif choice_user == 0:
                break
            else:
                raise ValueError
        except ValueError:
            print('\nНекорректный ввод, повторите запрос!')
