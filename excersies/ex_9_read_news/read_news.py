# The task you have to perform is to read the news using  python. Build a program that will give you daily top latest news.

import requests
import json

def text_to_speech(text):
    from win32com.client import Dispatch
    speaker = Dispatch("SAPI.Spvoice")
    speaker.speak(text)

if __name__ == "__main__":
    text_to_speech("NEWS FOR TODAY")
    
    api_key = "eab99b98ba37455e82e8459de446d853"
    news_url = f"https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey={api_key}"
    
    response = requests.get(news_url)
    news_data = response.json()
    
    articles = news_data["articles"]
    
    for article in articles:
        title = article["title"]
        text_to_speech(title)
        text_to_speech("Moving on to the next news..")
    
    text_to_speech("Thanks for listening")
