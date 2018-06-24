# to install lib  use  pip install feedparser  OR   easy_install feedparser
# FB Group: Kali linux and blackarch tools
# edit by Joseph A Morcos
# python 3.7 with feedparser lib
from datetime import datetime
import feedparser
BBC_FEED_URL='http://feeds.bbci.co.uk/news/%s/rss.xml'

def read_news(feed_url):
	try:
		data=feedparser.parse(feed_url)
	except Exception as e:
		print("Got error : %s" %str(e))
		
	for entry in data.enteries:
		print((entry.title))
		ptiny((entry.link))
		print((entry.description))
		print("\n")
		print("\n")
			
	if __name__=="__main__":
		print("=== Reading news feed from BBC (%s)===== " %datetime.today())
		print("Enter the type of news feed :")
		print("Available options are : world, uk, health, sci-tech, business, technology")
		type=raw_input("news feed type :")
		read_news(BBC_FEED_URL%type)
		print("+++ end of BBC news feed+++++")
