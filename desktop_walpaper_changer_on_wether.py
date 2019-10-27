# www.timeanddate.com/weather/india/
import urllib
from urllib import request
from bs4 import BeautifulSoup


def weather(city):
    try:
        the_url = "https://www.timeanddate.com/weather/india/" + city
        the_page = urllib.request.urlopen(the_url)
    except Exception as e:
        return "Invaild city name"

    soup = BeautifulSoup(the_page, "html.parser")
    content = soup.findAll('div', {"class": "three columns"})[0]
    temp = content.find('div', {'class': 'h2'}).text
    cond = str(content.findAll('p')[0].text)
    degree = temp.split(" ")[0].encode('ascii', 'ignore').decode()
    msg = degree + " - " + cond
    return msg

city=input()
msg=weather(city)
print(msg)