import requests
import keyboard

API_KEY = "cad5bfce75e0a57185142660d2258d06"

while True:
    city = input("Введите название города: ")

    try:
        res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                           params={'q': city, 'units': 'metric', 'lang': 'ru', 'appid': API_KEY})
        data = res.json()

        print(f"Погода: {data['weather'][0]['description']}")
        print(f"Температура: {data['main']['temp']}°C")
        print(f"Влажность: {data['main']['humidity']}%")
        print(f"Давление: {data['main']['pressure']} hPa")

    except KeyError:
        print("кажется что-то пошло не так. Попробуйте другой город.")
    except requests.exceptions.RequestException:
        print("Ошибка сети. Проверьте подключение к интернету.")

    print("Для выхода нажмите ESC, для продолжения - пробел.")

    while True:
        key = keyboard.read_key()
        if key == "esc":
            exit()
        elif key == " ":
            break