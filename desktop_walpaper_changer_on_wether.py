# www.timeanddate.com/weather/india/
import urllib
from urllib import request
from bs4 import BeautifulSoup
import subprocess
import datetime
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

    return degree,cond

city = input()
degree,cond = weather(city)
t_degree=degree[0:len(degree)-1]
act=int(t_degree)
hourss = datetime.datetime.now()
hours= hourss.hour
print ("current time=",hours,"cureent_temp=",act,"current_weather=",cond)
if act<10 and hours<=18:
    subprocess.Popen("DISPLAY=:0 GSETTINGS_BACKEND=dconf /usr/bin/gsettings set org.gnome.desktop.background picture-uri file://{0}".format(r'image/day_cold.jpg'), shell=True)
if act<10 and hours>18:
    subprocess.Popen("DISPLAY=:0 GSETTINGS_BACKEND=dconf /usr/bin/gsettings set org.gnome.desktop.background picture-uri file://{0}".format(r'image/night_cold.jpg'), shell=True)
su_cloud='cloud'
su_sun='sunny'
su_fog='fog'
su_rain='rain'
su_thunder='thunder'
su_storm='storm'
cl=cond.find(su_cloud)
su=cond.find(su_sun)
ra=cond.find(su_rain)
fo=cond.find(su_fog)
th=cond.find(su_thunder)
st=cond.find(su_storm)
if act>10 and hours<=18:
    if cl != -1:
        print("in line 47")
        subprocess.Popen("DISPLAY=:0 GSETTINGS_BACKEND=dconf /usr/bin/gsettings set org.gnome.desktop.background picture-uri file://{0}".format("/home/ankush/cool_python_scripts/image/day_clould.jpg"), shell=True)
    elif su !=-1:
        print("in line 50")
        subprocess.Popen("DISPLAY=:0 GSETTINGS_BACKEND=dconf /usr/bin/gsettings set org.gnome.desktop.background picture-uri file://{0}".format("/home/ankush/cool_python_scripts/image/day_sun.jpg"), shell=True)
    elif ra !=-1:
        print("in line 53")
        subprocess.Popen("DISPLAY=:0 GSETTINGS_BACKEND=dconf /usr/bin/gsettings set org.gnome.desktop.background picture-uri file://{0}".format("/home/ankush/cool_python_scripts/image/rain.jpg"), shell=True)
    elif th!=-1:
        print("in line 56")
        subprocess.Popen("DISPLAY=:0 GSETTINGS_BACKEND=dconf /usr/bin/gsettings set org.gnome.desktop.background picture-uri file://{0}".format("/home/ankush/cool_python_scripts/image/thunder.jpg"), shell=True)
    elif st!=-1:
        print("in line 59")
        subprocess.Popen("DISPLAY=:0 GSETTINGS_BACKEND=dconf /usr/bin/gsettings set org.gnome.desktop.background picture-uri file://{0}".format("/home/ankush/cool_python_scripts/image/thunder.jpg"), shell=True)
    elif fo!=-1:
        print("in line 62")
        subprocess.Popen("DISPLAY=:0 GSETTINGS_BACKEND=dconf /usr/bin/gsettings set org.gnome.desktop.background picture-uri file://{0}".format("/home/ankush/cool_python_scripts/image/fog.jpg"), shell=True)

elif act>10 and hours>18:
    if cl != -1:
        print("in line 47")
        subprocess.Popen("DISPLAY=:0 GSETTINGS_BACKEND=dconf /usr/bin/gsettings set org.gnome.desktop.background picture-uri file://{0}".format("/home/ankush/cool_python_scripts/image/night_cloud.jpg"), shell=True)
    elif su !=-1:
        print("in line 50")
        subprocess.Popen("DISPLAY=:0 GSETTINGS_BACKEND=dconf /usr/bin/gsettings set org.gnome.desktop.background picture-uri file://{0}".format("/home/ankush/cool_python_scripts/image/night_moon.jpg"), shell=True)
    elif ra !=-1:
        print("in line 53")
        subprocess.Popen("DISPLAY=:0 GSETTINGS_BACKEND=dconf /usr/bin/gsettings set org.gnome.desktop.background picture-uri file://{0}".format("/home/ankush/cool_python_scripts/image/night_rain.jpg"), shell=True)
    elif th!=-1:
        print("in line 56")
        subprocess.Popen("DISPLAY=:0 GSETTINGS_BACKEND=dconf /usr/bin/gsettings set org.gnome.desktop.background picture-uri file://{0}".format("/home/ankush/cool_python_scripts/image/thunder.jpg"), shell=True)
    elif st!=-1:
        print("in line 59")
        subprocess.Popen("DISPLAY=:0 GSETTINGS_BACKEND=dconf /usr/bin/gsettings set org.gnome.desktop.background picture-uri file://{0}".format("/home/ankush/cool_python_scripts/image/thunder.jpg"), shell=True)
    elif fo!=-1:
        print("in line 62")
        subprocess.Popen("DISPLAY=:0 GSETTINGS_BACKEND=dconf /usr/bin/gsettings set org.gnome.desktop.background picture-uri file://{0}".format("/home/ankush/cool_python_scripts/image/night_cold.jpg"), shell=True)
