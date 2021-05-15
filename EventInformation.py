#!/usr/bin/python3
import re
import TimeDiff
class Time(object):
	def __init__(self):
		self.digit=""
		self.daynight=""
	def setDigit(self, digit):
		self.digit=digit
	def setDayNight(self, daynight):
		self.daynight=daynight
class Event(object):
	def __init__(self):
		self.name=""
		self.time=Time()
		self.startEndTime=""
		self.synopsis=""
		self.channelname=""
		self.catagory=""
		self.startTime=""
		self.endTime=""
		self.duration=""
	def calculateDuration(self, starthour,startminute, startampm, endhour,endminute, endampm):
		result=0
		start=TimeDiff.TimeDisplay(starthour,startminute, startampm)				
		end=TimeDiff.TimeDisplay(endhour,endminute, endampm)				
		result=TimeDiff.findTimeDiff(start, end)
		self.duration=str(result)
	def findFuration(self):
		time=self.startEndTime
		#print (time)
		ind=0
		starthr=0
		startmin=0
		endhr=0
		endmin=0
		starttimeampm=""
		endtimeampm=""
		for num in re.finditer("\d+", time):
			#print (num.group(0), ": ", ind)
			if ind==0:
				starthr=int(num.group(0))
			if ind==1:
				startmin=int(num.group(0))
			if ind==2:
				endhr=int(num.group(0))
			if ind==3:
				endmin=int(num.group(0))
			ind=ind+1
		#print(starthr,":",startmin, endhr, ":", endmin)
		ind=0	
		for word in re.finditer("[AM|PM]\w+", time):
			if ind==0:
				starttimeampm=word.group(0)
			if ind==1:
				endtimeampm=word.group(0)
			ind=ind+1
			#print (word.group(0))
		#print (starttimeampm, ":", endtimeampm)
		self.calculateDuration(starthr, startmin,starttimeampm,endhr, endmin, endtimeampm)
	def setName(self, name):
		self.name=name
	def setTime(self, time):
		self.time=time
	def setStartEndTime(self,startEndTime):
		self.startEndTime=startEndTime
		self.findFuration()
	def setSynopsis(self, synopsis):
		self.synopsis=synopsis.strip()
	def setChannelName(self, name):
		self.channelname=name
	def setCatagory(self, catagory):	
		self.catagory=catagory
	def setStartTime(self, startTime):	
		self.startTime=startTime
		self.endTime=str(int(self.startTime)+int(self.duration))	
	def setEndTime(self, endTime):	
		self.endTime=endTime
	def parseStartTime(self, url):
		#print (":", url)
		splitted=url.split('/')
		time=splitted[len(splitted)-2]
		self.setStartTime(time)
	
