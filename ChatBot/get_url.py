import requests
from lxml import html
from googlesearch import search
from bs4 import BeautifulSoup

query = 'Testing'

## Google Search query results as a Python List of URLs
search_result_list = list(search(query, tld="co.in", num=10, stop=3, pause=1))

page = requests.get(search_result_list[0])

print(search_result_list[0])

print(page.status_code)

tree = html.fromstring(page.content)

soup = BeautifulSoup(page.content, features="lxml")

#print(soup)
