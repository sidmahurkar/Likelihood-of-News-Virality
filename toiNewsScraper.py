from bs4 import BeautifulSoup
from newspaper import Article

import requests
import newspaper
import pandas as pd

def scrapeNews(URL):

	url = URL
	page_request = requests.get(url)
	data = page_request.content
	soup = BeautifulSoup(data,"html.parser")

	urls = []
	counter = 0
	for divtag in soup.find_all('div', {'class': 'headlines-list'}):
		for ultag in divtag.find_all('ul', {'class': 'clearfix'}):
			if (counter <= 10):
				for litag in ultag.find_all('li'):
					urls.append("https://timesofindia.indiatimes.com" + litag.find('a')['href'])

    # headlines = newspaper.build(url)

	news_data = []
	# for article in headlines.articles:
	for i in urls:
		article = Article(i, language = "en")
		article.download()
		article.parse()
		article.nlp()

		data = {}
		data['authors'] = article.authors
		data['publish date'] = article.publish_date
		data['text'] = article.text
		data['images'] = article.images
		data['movies'] = article.movies
		data['keywords'] = article.keywords
		data['summary'] = article.summary

		news_data.append(data)

		print(news_data)

url = "https://timesofindia.indiatimes.com/home/headlines"

scrapeNews(url)
