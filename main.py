from application.salary import calculate_salary
from application.db.people import get_employees
from datetime import date as dt
from selenium import webdriver

driver = webdriver.Chrome()
def start_browser():
    """Запустить браузер и перейти по ссылке"""
    driver.get('http://ya.ru')
    print('Успешно открыл браузер и сайт Я.ру')

if __name__ == '__main__':
    """Запустить функции и распечатать текущую дату"""
    calculate_salary()
    get_employees()
    print(dt.today().strftime('%d.%m.%Y'))
    start_browser()