#!/usr/bin/python3
from html.parser import HTMLParser

class Day(object):
	def __init__(self, channelname, catagory, href):
		self.channelname=channelname
		self.catagory=catagory
		self.href=href

class ServiceEPGParser(HTMLParser):
	def __init__(self, channel):					
		HTMLParser.__init__(self)
		self.name=channel.name
		self.catagory=channel.catagory
		self.href=channel.href
		self.tdFlag=False	
		self.divFlag=False	
		self.count=0 #control on repeatation
		self.todays=[]
		self.weekdays=[]
		#print self.href
	def handle_starttag(self, tag, attrs):
		#print tag
		if tag=='td': #only for todays and tomorrows full schedule
			for name, value in attrs:
				if name=='class' and value=='dateHdr':
					self.tdFlag=True
		if 	self.tdFlag==True and tag=='a':
			self.tdFlag=False
			for name, value in attrs:
				if name=='href':
					self.todays.append(value)
		if tag=='div':
			for name, value in attrs:
				if name=='class' and value=='dateIndicator':
					self.divFlag=True
					self.count+=1
		
		if self.count>1:
			self.divFlag=False
			
		if 	tag=='a' and self.divFlag==True:
			for name, value in attrs:
				if name=='class' and (value=='' or value=='currentlySelectedDay'):
					for name, value in attrs:
						if name=='href':
							#print value
							day=Day(self.name, self.catagory, value)
							self.weekdays.append(day)

	#def handle_endtag(self, tag):
		#if tag=='div':
		#	self.divFlag=False
	#def handle_data(self, data):
	#	print data
	def updateList(self):
		self.weekdays[0].href=self.todays[0]

		

