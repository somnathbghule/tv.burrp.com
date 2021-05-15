#!/usr/bin/python3
from ServiceParser import ServiceEPGParser
from EventParser import DayEpgParser
import FetchHTML
from ServiceList import ServiceListParser
from SqlDatabase import EPGDatabase
weburl="http://tv.burrp.com/channels.html"

class EPG(object):
	def __init__(self):
		self.epgdatabase=EPGDatabase('/home/rohit/myworkspace/python/epgserver-v1.00/rsrc/liveepg.db')	
	def getAllServiceList(self):
		parser = ServiceListParser()
		parser.feed(FetchHTML.getHTMLPage(weburl))
		return parser.serviceList

	def getSelectiveServiceUrlList(self,serviceList):
		urlList=[]
		parser = ServiceListParser()
		parser.feed(FetchHTML.getHTMLPage(weburl))
		for service in parser.serviceList:
			if not len(serviceList):
				break
			for chname in serviceList:
				if (chname).lower()==(service.name).lower():
					urlList.append(service)
					serviceList.remove(chname)
		if not len(urlList):
			print ("debug: Service Not Found")	
		return urlList;

	def getServicesEPG(self, serviceList):
		for service in serviceList:
			print (service.name)
			serviceepgparser=ServiceEPGParser(service)	
			serviceepgparser.feed(FetchHTML.getHTMLPage(serviceepgparser.href))
			serviceepgparser.updateList()
			for day in serviceepgparser.weekdays:
				dayepgparser=DayEpgParser(day)
				dayepgparser.feed(FetchHTML.getHTMLPage(dayepgparser.href))
				#print len(dayepgparser.programList)
				for event in dayepgparser.eventList:
					query='INSERT INTO epg(name) VALUES ('+event.name+');'
					self.epgdatabase.setQuery(query)
					#print  (event.channelname, "|", event.catagory, "|", event.startTime,"|", event.endTime, "|",event.name, "|", event.startEndTime, "|", event.duration)#,"|",event.synopsis
		self.epgdatabase.close()		 

#serviceList=['Sony Max 2','Sony MAX','FILMY','Zee Cinema', 'Star Plus','9XM','DD National','Sony Mix','Aaj Tak','HBO','Sony sab','Sony pix','star movies','zee action','zee smile','star pravah','animal planet']
serviceList=['zee cinema']
epg=EPG()
epg.getServicesEPG(epg.getSelectiveServiceUrlList(serviceList))
	
