#! /usr/bin/env python

try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen
# to process json needed 
import json 


def printResults(data):
	theJSON= json.loads(data)
	if "title" in theJSON["metadata"]:
		print(theJSON["metadata"]["title"])
		count = theJSON["metadata"]["count"]
		print str(count) + " events recorded"

def main():
	urlData ="https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"	
	webURL = urlopen(urlData)
	print ("result code: " + str(webURL.getcode()))
	if (webURL.getcode() == 200):
		data = webURL.read()
		printResults(data)
	else:
		print ("recieved error, cannot parse results")


if __name__ == '__main__':
   main()