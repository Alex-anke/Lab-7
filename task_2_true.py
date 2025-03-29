import requests
import json
from datetime import datetime


def get_vacancies(keyword, area_id):
    url = f"https://api.hh.ru/vacancies?text={keyword}&area={area_id}&currency_code=RUR&per_page=20&page=0"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
    response = requests.get(url, headers=headers)
    data = json.loads(response.text)

    vacancies = []
    for item in data["items"]:
        salary = item.get('salary')
        if salary:
            salary_from = salary.get('from')
            salary_to = salary.get('to')
            salary_currency = salary.get('currency')
            if salary_from and salary_to:
                salary_str = f"{salary_from} - {salary_to} {salary_currency}"
            elif salary_from:
                salary_str = f"{salary_from} {salary_currency}"
            elif salary_to:
                salary_str = f"{salary_to} {salary_currency}"
            else:
                salary_str = "Н/Д"

            published_at = datetime.fromisoformat(item["published_at"]).strftime('%m.%d.%Y')
            vacancy = {
                "Название": item["name"],
                "Работодатель": item["employer"]["name"],
                "Зарплата": salary_str,
                "Регион": item["area"]["name"],
                "Дата публикации": published_at
            }
            vacancies.append(vacancy)

    return vacancies


keyword = "python"
area_id = 2

vacancies = get_vacancies(keyword, area_id)

for vacancy in vacancies:
    for key, value in vacancy.items():
        print(f"{key}: {value}")
    print()
