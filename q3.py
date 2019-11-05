import requests
import time
from bs4 import BeautifulSoup
from playsound import playsound


'''
def matches():
    url = "http://mapps.cricbuzz.com/cbzios/match/livematches"
    try:
        r = requests.get(url).json()
    except Exception:
        raise
    crawled_data = r
    matches = crawled_data['matches']
    data = []

    for match in matches:
        #print ("hello")
        #print(match)
        data.append(match['match_id'])

    return data


def matchinfo(id_match):

    url = "http://mapps.cricbuzz.com/cbzios/match/" + id_match
    try:
        r = requests.get(url).json()
    except Exception:
        raise
    crawled_data = r

    d = {}
    d['id'] = id_match
    d['series'] = crawled_data.get('series_name')
    return d

def calforeachmatch(match):
    data = []
    for i in match:
        data.append(matchinfo(i))
    return data
'''
def crawlforlivescore(id_match):
    while True:
        url = "https://www.espncricinfo.com/series/8877/game/1194273/knights-vs-titans-11th-match-4-day-franchise-series-2019-20"
        try:
            r = requests.get(url)
        except Exception:
            raise

        soup = BeautifulSoup(r.content,"html.parser")
        # print(soup.prettify())
        var =soup.find_all('div',class_='recent-overs-wrapper')
        #var = soup.find_all('div')
        print(len(var))
        st = var[0]
        st2 = st.text
        print(st2)
        run=[]
        run = st2.split('|')
        runs = run[-1];
        print(runs)
        if runs[-1] == "W":
            print("it is a wicket")
            playsound('wickets.mp3')
        elif runs[-1] == "6" :
            print("it is a six")
            playsound('sixes.mp3')
        elif runs[-1] == "4":
            print("it is a four")
            playsound('fours.mp3')
        elif runs[-1] == "1":
            print("one run")
        else:
            print("dot ball")
            #playsound('fours.mp3')
        time.sleep(5)

def parselinks(links):
    for i in links:


def crawlforlivematches():
    url = "https://www.espncricinfo.com/scores"
    try:
        r = requests.get(url)

    except Exception:
        raise


    # match_ids = json['matches'].keys()
    # all_matches = json['matches'].values()
    # print(match_ids)
    # print(all_matches)
    soup = BeautifulSoup(r.content,"html.parser")
    #print(soup.prettify)

    matches = soup.find_all('span', class_ = 'cscore_time')
    links = soup.find_all('a', class_='cscore_details')
    print(links)
    parselinks(links)
    print(len(matches))
    for i in matches:
        print(i)
        data = soup.find('span','data-reactid')
        print(data)
        print(i.text)
    return 0


def main():
    # match = matches()
    '''for i in match:
        print(i)
    print(match[0])'''
     #calculate match info for 1st match
    '''data = matchinfo(match[0])
    print(data)'''

    #do this for all matches
    #match_information = []
    match_information = crawlforlivematches()
    '''match_information = calforeachmatch(match)
    for i in match_information:
        print(i)
        # match_information = matchinfo(i)
        #print(match_information)'''

    '''keep this off for sometime
    crawlforlivescore(match[0])'''







if __name__ == '__main__':
    main()
