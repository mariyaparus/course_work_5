import psycopg2


class DBManager:
    """Класс для работы с БД"""

    def __init__(self, dbname):
        self.dbname = dbname
        self.user = 'postgres'
        self.password = '****'
        self.host = 'localhost'

    def connect(self):
        conn = psycopg2.connect(
            dbname=self.dbname,
            user=self.user,
            password=self.password,
            host=self.host
        )
        return conn

    def get_companies_and_vacancies_count(self):
        """Список всех компаний и количество вакансий у каждой компании"""

        conn = self.connect()
        cur = conn.cursor()
        cur.execute("""
            SELECT company_name, COUNT(*) as vacancies_count
            FROM vacancies
            GROUP BY company_name
            ORDER BY vacancies_count DESC
        """)
        result = cur.fetchall()
        cur.close()
        conn.close()
        return result

    def get_all_vacancies(self):
        """Список всех вакансий с указанием названия компании, названия вакансии, зарплаты и ссылки на вакансию"""

        conn = self.connect()
        cur = conn.cursor()
        cur.execute("""
            SELECT company_name, vacancy_name, salary_from, url
            FROM vacancies
            ORDER BY salary_from DESC
        """)
        result = cur.fetchall()
        cur.close()
        conn.close()
        return result

    def get_avg_salary(self):
        """Средняя зарплата по вакансиям"""

        conn = self.connect()
        cur = conn.cursor()
        cur.execute("""
            SELECT AVG(salary_from)
            FROM vacancies
        """)
        result = cur.fetchone()[0]
        cur.close()
        conn.close()
        return result

    def get_vacancies_with_higher_salary(self):
        """Список всех вакансий, у которых зарплата выше средней"""

        avg_salary = self.get_avg_salary()
        conn = self.connect()
        cur = conn.cursor()
        cur.execute(f"""
            SELECT company_name, vacancy_name, salary_from, url
            FROM vacancies
            WHERE salary_from > {avg_salary}
            ORDER BY salary_from DESC
        """)
        result = cur.fetchall()
        cur.close()
        conn.close()
        return result

    def get_vacancies_with_keyword(self, keyword):
        """Список всех вакансий, в названии которых содержатся переданные в метод слова"""

        conn = self.connect()
        cur = conn.cursor()
        cur.execute(f"""
            SELECT company_name, vacancy_name, salary_from, url
            FROM vacancies
            WHERE vacancy_name LIKE '%{keyword}%'
            ORDER BY salary_from DESC
        """)
        result = cur.fetchall()
        cur.close()
        conn.close()
        return result


if __name__ == '__main__':
    pass
