import requests
from selenium import webdriver
import json
from bs4 import BeautifulSoup
import time
import urllib.request
import time
from functools import reduce
from operator import add

from selenium.webdriver.chrome.options import Options

# Weather API
API_KEY = 'ilLuMG3kTVe7eJzWYfKDpiSm0BdKwJbE'
LOCATION_KEY = '328328'
cURL = "http://dataservice.accuweather.com/currentconditions/v1/328328?apikey=ilLuMG3kTVe7eJzWYfKDpiSm0BdKwJbE&details=true"

# News API
newsUrl = ('https://newsapi.org/v2/top-headlines?'
           'country=gb&'
           'apiKey=9d237adefcc6451092b8203ccce29a02')


def scrap_weather_Data():
    with urllib.request.urlopen(cURL) as URL:
        data = json.loads(URL.read().decode())
    for key in data:
        print(type(key['Wind']))
        print(key['Wind']['Speed']['Metric']['Value'])
        windSpeed = key['Wind']['Speed']['Metric']['Value']
        cloudCover = key['CloudCover']
        percip = key['PrecipitationSummary']['Precipitation']['Metric']['Value']
        return [windSpeed, cloudCover, percip]


def scrap_tweets_Data():
    try:
        URL = "https://www.trendsmap.com/local/united+kingdom#collapse_trends"
        r = requests.get(URL)
        soup = BeautifulSoup(r.content, 'html5lib')
        print(soup.prettify())
        # plain_text = source_code.text
        # soup = bs4.BeautifulSoup(plain_text, 'html5lib')
        row = soup.findAll('div', attrs={'class': 'inline-tweet-text'})
        response_list = []

        num = len(row)
        for i in range(4):
            response_list.append(str(row[i].text))
            print(str(row[i].text))
    except:
        # driver.close()
        print("something went wrong")


def scrap_bbcNews_Data():
    try:
        resp = []
        response = requests.get(newsUrl)
        jsonResp = response.json()
        # loaded_json = json.loads(response)
        data = jsonResp['articles']
        print(len(data))
        for index in data:
            title = index['title']
            resp.append(title)
            print(title)
        return resp
    except:
        print("something went wrong in news api")


def unique(list1):
    # intilize a null list
    unique_list = []

    # traverse for all elements
    for x in list1:
        # check if exists in unique_list or not
        if x not in unique_list:
            unique_list.append(x)
            # print list
    return unique_list


def run_forever():
    count = 0
    tweetList = []
    while True:
        toptweets = scrap_tweets_Data()
        tweetList.append(toptweets)
        count += 1
        time.sleep(5)
        if (count == 4):
            try:
                singleList = reduce(add, tweetList)
                top10tweets = unique(singleList)
                print(top10tweets)
                news_resp = scrap_bbcNews_Data()
                print('#################################################')
                print(news_resp)
                weather_resp = scrap_weather_Data()
                print(weather_resp)
                print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
                count = 0
                tweetList = []
            except:
                continue
        # time.sleep(120)


if __name__ == "__main__":
    print(scrap_weather_Data())
