#!/usr/bin/python
class TimeDisplay(object):
	def __init__(self, hr, minute, ampm):
		self.hr=hr
		self.minute=minute	
		self.ampm=ampm
	def hourinsec(self):
		if(self.hr==12):
			self.hr=0
		return 	(self.hr*3600)
	def mininsec(self):
		return 	(self.minute*60)

def amIsEqualTopm(startTime, endTime):
	start=startTime.hourinsec()+startTime.mininsec()		
	end=endTime.hourinsec()+endTime.mininsec()
	result=end-start
	if result < 0 :
		result=24*3600+result	
	if result==0:
		result=24*3600	
	#print "diff:", result," ", result/3600,"hh",":",(result%3600)/60,"mm"
	return result

def amTopm(startTime, endTime):
	diff_in_start_time_to_12=12*3600-(startTime.hourinsec()+startTime.mininsec())
	diff_in_end_time_to_12=(endTime.hourinsec()+endTime.mininsec())
	result=diff_in_end_time_to_12+diff_in_start_time_to_12
	#print "diff:", result," ", result/3600,"hh",":",(result%3600)/60,"mm"
	return result

def findTimeDiff(startTime, endTime):
	if(startTime.ampm==endTime.ampm):
		return amIsEqualTopm(startTime, endTime)
	#elif(startTime.ampm=="AM" and endTime.ampm=="PM"): #afternoon
	#	return amTopm(startTime, endTime)
	#elif(startTime.ampm=="PM" and endTime.ampm=="AM"): #nextday
	#	return amTopm(startTime, endTime)
	else:
		return amTopm(startTime, endTime)	
	
#start=TimeDisplay(11, 59, "AM")				
#end=TimeDisplay(11, 59, "AM")				
#result=findTimeDiff(start, end)
#print "diff:", result," ", result/3600,"hh",":",(result%3600)/60,"mm"

