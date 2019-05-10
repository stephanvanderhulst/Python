"""
Author: Anurag Rana
Usage: python google.py <keyword>
Description: Script googles the keyword and opens top 10(max) search results in separate tabs in the browser
Usage: python filename.py keyword
Tested with Python3
"""

import webbrowser
import requests
import bs4


def start(keyword="business intelligence", tabs=10):

	res = requests.get('https://google.com/search?q='+keyword)
	soup = bs4.BeautifulSoup(res.text,'lxml')
	links = soup.select('.r a')
	tab_counts = min(tabs, len(links))

	for i in range(tab_counts):
		webbrowser.open('https://google.com' + links[i].get('href'))


start("data warehousing", 5)