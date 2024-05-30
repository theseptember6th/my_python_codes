# The task you have to perform is to read the news using  python. Build a program that will give you daily top latest news.

import requests
import json
def speak(str):
    from win32com.client import Dispatch
    speak=Dispatch("SAPI.Spvoice")
    speak.speak(str)

if __name__ == "__main__":
    speak("NEWS FOR TODAY")
    url="https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey=eab99b98ba37455e82e8459de446d853"
    news=requests.get(url).text
    news_dict=json.loads(news)
    #print(news_dict["status"])
    #print(news_dict["articles"])
    arts=news_dict["articles"]
    for article in arts:
        speak(article["title"])
        speak("Moving on to the next news..")
    speak("Thanks for listening")