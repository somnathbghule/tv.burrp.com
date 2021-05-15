#!/usr/bin/python3
from html.parser import HTMLParser
import re
import codecs

from EventInformation import Event
from EventInformation import Time
import FetchHTML
class EventInformationParser(HTMLParser):
	def __init__(self):
		HTMLParser.__init__(self)
		self.showTime=False
		self.durationFlag=False
		self.synopsisFlag=False
		self.moreInfoFlag=False	
		self.doMoreFlag=False
		self.startEndTime=""
		self.synopsis=""
	def handle_starttag(self, tag, attrs):
		if tag=='td':
			for name, value in attrs:
				if name=='class' and value=='showTime':
					self.showTime=True
		if tag=='h4' and self.showTime:
			self.durationFlag=True
		if tag=='div': #div class="synopsis"
			for name, value in attrs:
				if name=='class' and value=='synopsis':
					self.synopsisFlag=True
		if self.doMoreFlag and tag=='span':
			for name, value in attrs:
				if name=='id' and value=='morecontent':
					self.moreInfoFlag=True
	#def handle_endtag(self, tag):
	#	if tag=='div':
	#		self.synopsisFlag=False

	def handle_data(self, data):
		if self.durationFlag:
			data=data.replace('\t', '')
			data=data.split()
			data=' '.join(data)
			self.startEndTime=data.strip()
			#print (self.startEndTime)
			self.durationFlag=False
			self.showTime=False
		if self.synopsisFlag:
			#print "syn: ", data
			self.synopsis=self.synopsis+data
			self.synopsisFlag=False
			self.doMoreFlag=True
		if self.moreInfoFlag:
			self.doMoreFlag=False
			self.moreInfoFlag=False
			#print "moreinfo: ", data
			self.synopsis=self.synopsis+data
			#print "sys:", self.synopsis

						

class DayEpgParser(HTMLParser):
	def __init__(self, day):
		HTMLParser.__init__(self)
		self.tdResultTimeFlag=False
		self.timeFlag=False
		self.timeFlagStart=False
		self.timeampm=False
		self.count=0
		self.time=Time()
		self.event=Event()

		self.resultThumb=False		
		self.eventList=[]

		self.href=day.href
		self.servicename=day.channelname
		self.catagory=day.catagory
	def handle_starttag(self, tag, attrs):
		if tag=='td':
			for name, value in attrs:
				if name=='class' and re.search('resultTime*', value):
					self.tdResultTimeFlag=True

		if tag=='b' and self.tdResultTimeFlag:
			for name, value in attrs:
				if name=='class' and value=='from':
					self.timeFlag=True
		if tag=='sup' and self.timeFlagStart:
			for name, value in attrs:
				if name=='class' and value=='ap':
					self.timeampm=True

		if tag=='td':
			for name, value in attrs:
				if name=='class' and re.search('resultTitle*', value):
					self.resultThumb=True
		if tag=='a' and self.resultThumb==True:
			for name, value in attrs:
				if name=='href':
					#print value
					hrefurl=value
					programInfo=EventInformationParser()
					programInfo.feed(FetchHTML.getHTMLPage(hrefurl))
					self.event.setStartEndTime(programInfo.startEndTime)
					self.event.setSynopsis(programInfo.synopsis)					
					self.event.setChannelName(self.servicename)
					self.event.setCatagory(self.catagory)
					self.event.parseStartTime(hrefurl)
					#print "time: ", programInfo.startEndTime
				if name=='title':
					self.event.setName(value)
					self.eventList.append(self.event)
			self.resultThumb=False	 
				
			
	#def handle_endtag(self, tag):
	
	def handle_data(self, data):
		if self.timeFlag:
			data=data.replace('\n', '\b')
			data=data.replace('\t', '')
			self.event=Event()
			self.time=Time()
			self.time.setDigit(data)
			self.timeFlagStart=True
			self.timeFlag=False
			self.event.setTime(self.time)
		if self.timeampm:
			self.count=self.count+1
			self.timeampm=False
			self.time.setDayNight(data)
			#print self.time.digit, self.time.daynight

