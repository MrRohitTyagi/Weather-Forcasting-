from bs4 import BeautifulSoup
import requests
import datetime
import pyttsx3

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

    
#########    to smake your program speak the weather info
# engine = pyttsx3.init('sapi5')
# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[0].id)


# def speak(audio):
#     engine.say(audio)
#     engine.runAndWait()
########


def weather(city,city1):
    try:
        city = city.replace(" ", "+")
        res = requests.get(
            f'https://www.google.com/search?q={city}&oq={city}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8', headers=headers)
        soup = BeautifulSoup(res.text, 'html.parser')
        location = soup.select('#wob_loc')[0].getText().strip()
        # time = soup.select('#wob_dts')[0].getText().strip()
        weathers = soup.select('#wob_tm')[0].getText().strip()
        print(location)
        now = datetime.datetime.now()
        

        current_time = now.strftime("%H:%M:%S")
        print("Current Time =", current_time)
        # print(time)
        print(datetime.date.today())
        print(f"current temperature in {city1} is {weathers} °C")
        # print(speak(f"current temperature in {city1} is {weathers} °C")) #to smake your program speak the weather info

    except Exception as e:
        print("Enter correct name")    

print("Enter the city name")
city = input()
city1 = city
city = city + "weather"
weather(city,city1)

