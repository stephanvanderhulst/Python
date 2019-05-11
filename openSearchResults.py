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
import math


def openResults(keyword, results):
	#https://www.google.com/search?q=data+warehousing&start=20
	for set in range(math.ceil(results/10)):
		print(f'Opening set number {set+1} of 10 results')
		start_value = max(0,((set+1)*10)-10)
		print(f'The start value for this set is {start_value}')

		res = requests.get(f'https://google.com/search?q={keyword}&start={start_value}')
		print(f'https://google.com/search?q={keyword}&start={start_value}')
		soup = bs4.BeautifulSoup(res.text,'lxml')
		links = soup.select('.r a')
		tab_counts = min(results, len(links))

		for i in range(tab_counts):
			print('https://google.com' + links[i].get('href'))
			webbrowser.open('https://google.com' + links[i].get('href'))


openResults("data warehousing", 20)