#!/usr/bin/python3
from urllib.request import urlopen
from html.parser import HTMLParser
weburl="http://tv.burrp.com/channels.html"

def getHTMLPage(url):
	url=str(url)
	url=url.replace('’', '\'')
	url=url.replace('⁄','/')
	url=url.replace(' ', '%20')
	url=url.replace('…','...')
	#url=url.encode('utf-8')
	#url=url.decode('utf-8')
	#print (url)
	html = urlopen(url)
	return str(html.read().decode('utf-8'))

