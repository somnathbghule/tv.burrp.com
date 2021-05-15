#!/usr/bin/python3
from html.parser import HTMLParser
from random import randint

from ServiceParser import ServiceEPGParser
from EventParser import DayEpgParser
import FetchHTML


class Service(object):
	def __init__(self, name, href, catagory):
		self.name=name
		self.href=href
		self.catagory=catagory
	def setName(self, name):
		self.name=name
	def setHref(self, href):
		self.href=href
	def setCatagory(self, catagory):
		self.catagory=catagory

class ServiceListParser(HTMLParser):
	def __init__(self):
		HTMLParser.__init__(self)
		self.catagoryFlag=False
		self.servicelink=False
		self.serviceList=[]
		self.cat=""
	def handle_starttag(self, tag, attrs):
		self.catagoryFlag=False
		if tag == 'legend':
			for name, value in attrs:
				if name == 'class' and value == 'channelCategory':
					self.catagoryFlag=True
					self.lasttag=tag
					self.cat=""
		if tag == 'a' :
			for name, value in attrs:
				if name=='class' and value=='channelLogoBox':
					for name, value in attrs:
						if name == 'href':
							#print "-----href--------", value
							self.service=Service("", "", "")
							self.service.setCatagory(self.cat)
							self.service.setHref(value)
						if name == 'title':
							#print "-----title--------", value
							self.service.setName(value)
							self.serviceList.append(self.service)
	def handle_endtag(self, tag):
		if tag == 'legend':
			self.catagoryFlag = False
	def handle_data(self, data):
		if self.catagoryFlag:
			self.cat=self.cat+data
			#print ("----catagory--------",self.cat)

