from django.shortcuts import render
import requests
from bs4 import BeautifulSoup

toi_response = requests.get("https://timesofindia.indiatimes.com/briefs")
toi_soup = BeautifulSoup(toi_response.content,"html5lib")

toi_news_headings = toi_soup.select("h2 a")[:10]
toi_news = [news.text for news in toi_news_headings]

th_response = requests.get("https://www.thehindu.com/latest-news/")
th_soup = BeautifulSoup(th_response.content,"html5lib")

th_headings = th_soup.select(".latest-news a")[:10]
th_news = [news.text for news in th_headings]


# Create your views here.
def index(request):
    return render(request,"News/index.html",{"toi_news":toi_news, "th_news":th_news})
