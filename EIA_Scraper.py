from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

def getSoup():
  url = "https://www.eia.gov/beta/"
  page = urlopen(url)
  html_bytes = page.read()
  #print(html_bytes)
  html = html_bytes.decode("utf-8")

  soup = BeautifulSoup(html, 'html.parser')
  return soup

def clean_text(text):
  return re.sub("[\r\n\t]+", " ", text).strip()

soup = getSoup()
accordion = soup.find_all("div", {"class": "accordion-content"})
for acc in accordion:
    header = acc.h1.text
    print("=================================================================\n")
    print(header)
    print("\n=================================================================")

    articles = acc.find_all('ul')
    for article in articles:
        lis = article.find_all('li')
        title = clean_text(lis[0].a.text)
        raw_date = lis[1].find("span", {"class": "date"}).text
        date = clean_text(raw_date)
        content = re.sub("<.*>", "", lis[2].text)
        parag = clean_text(content)
        print("title: " + title)
        print("date: " + date)
        print("parag: " + parag)
        print("---------------------------------------------------------------")
    
    print()


