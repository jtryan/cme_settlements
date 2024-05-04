
# beauty_soup.py

from bs4 import BeautifulSoup
from urllib.request import urlopen

url = "https://www.cmegroup.com/markets/equities/sp/e-mini-sandp500.settlements.html"
page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")


if __name__ == "__main__":
    
