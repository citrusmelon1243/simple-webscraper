import urllib.request
from bs4 import BeautifulSoup
import collections


class Scraper:
    def __init__(self, site):
        self.site = site

    def scrape(self):
        newsroom = open("/home/curtisbyers/websites", 'w')
        collections.Callable = collections.abc.Callable
        html = (urllib.request.urlopen(self.site)).read()
        parser = "html.parser"
        sp = BeautifulSoup(html, parser)
        for tag in sp.find_all("a"):
            url = tag.get("href")
            if url is None:
                continue
            if "http" in url:
                print("\n" + url)
                newsroom.write("\n" + url)


news = "https://news.google.com/"
Scraper(news).scrape()
