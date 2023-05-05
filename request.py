import requests
from bs4 import BeautifulSoup as bs


url = "https://news.google.com"


def arr_links():
    response = requests.get(url)
    soup = bs(response.text, "html.parser")
    new_links = [link.get('href') for link in soup.find_all('a', {'class': 'WwrzSb'})]
    return new_links
