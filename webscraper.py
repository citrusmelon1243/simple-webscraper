import urllib.request
from bs4 import BeautifulSoup

class Scraper:
    def __init__(self, site):
        self.site = site

    def scrape(self):
        html = (urllib.request.urlopen(self.site)).read()
        parser = "html.parser"
        sp = BeautifulSoup(html, parser)
        for tag in sp.findall("a"):
            url = tag.get("href")
            if url is None:
                continue
            if "html" in url:
                print("\n" + url)

news = "https://news.google.com/home?hl=en-US&gl=US&ceid=US:en"
Scraper(news).scrape()
