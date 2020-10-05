import requests
from win32com.client import Dispatch
import time


def speak(s):
    speaker = Dispatch("SAPI.SpVoice")
    speaker.Speak(s)


def get_top_headlines(news_api_url):
    response = requests.get(news_api_url)

    news = response.json()
    articles = news['articles']
    c = []
    for i in articles:
        c.append(i['title'] + i['description'])

    return c


if __name__ == '__main__':
    url = (f'http://newsapi.org/v2/top-headlines?'
           'country=in&'
           'apiKey={your_api_key}')

    content = get_top_headlines(url)

    for x in content:
        speak(x)
        time.sleep(3)
