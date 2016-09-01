import urllib2
import json

def getHttpResponse(url):
	response = urllib2.urlopen(url)
	data = json.load(response)   
	return data