import requests
# Город (указан как на сайте)
city = "Moscow,RU"
# API ключ полученный с сайта
appid = "c090649760f7f1cefdbac887baeadb92"
# Получение данных с OpenWeather с учётом города, температуры, языкового пакета
res = requests.get("http://api.openweathermap.org/data/2.5/weather", params={'q': city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
# Парсинг (декодирование информации с сайта)
data = res.json()
# Вывод данных
print("Город:", city)
print("Погодные условия:", data['weather'][0]['description'])
print("Температура:", data['main']['temp'], 'градус(ов)')
print("Минимальная температура:", data['main']['temp_min'], 'градус(ов)')
print("Максимальная температура", data['main']['temp_max'], 'градус(ов)')
# ДЗ (Скорость ветра и видимость)
print("Скорость ветра:", data['wind']['speed'], 'м/c')
print("Видимость:", data['visibility'], 'м')

#Получение данных с OpenWeather (forecast)
res = requests.get("http://api.openweathermap.org/data/2.5/forecast", params={'q': city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
data = res.json()
print("Прогноз погоды на неделю:")
for i in data['list']:
    print("Дата <", i['dt_txt'],
          "> \r\nТемпература <", '{0:+3.0f}'.format(i['main']['temp']),
          "> \r\nПогодные условия <", i['weather'][0]['description'],
# ДЗ (Скорость ветра и видимость)
          "> \r\nСкорость ветра <", i['wind']['speed'],
          "> \r\nВидимость <", i['visibility'],
          ">")

