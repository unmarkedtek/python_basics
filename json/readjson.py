#! /usr/bin/env python
print "hello"

import json
from pprint import pprint

#data = json.load(open('data.json'))
#data = json.load(open('array.json'))
data = json.load(open('effects.json'))

pprint(data)

# #! /usr/bin/env python


# try:
#     from urllib.request import urlopen
# except ImportError:
#     from urllib2 import urlopen
# # to process json needed 
# import json 


# def printResults(data):
# 	theJSON= json.loads(data)
# 	if "title" in theJSON["metadata"]:
# 		print(theJSON["metadata"]["title"])
# 		count = theJSON["metadata"]["count"]
# 		print str(count) + " events recorded"

# def main():

# 	urlData ="https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"	
# 	webURL = urlopen(urlData)
# 	print ("result code: " + str(webURL.getcode()))
# 	if (webURL.getcode() == 200):
# 		data = webURL.read()
# 		printResults(data)
# 	else:
# 		print ("recieved error, cannot parse results")


# if __name__ == '__main__':
#    main()

#    {
#     "glossary": {
#         "title": "example glossary",
# 		"GlossDiv": {
#             "title": "S",
# 			"GlossList": {
#                 "GlossEntry": {
#                     "ID": "SGML",
# 					"SortAs": "SGML",
# 					"GlossTerm": "Standard Generalized Markup Language",
# 					"Acronym": "SGML",
# 					"Abbrev": "ISO 8879:1986",
# 					"GlossDef": {
#                         "para": "A meta-markup language, used to create markup languages such as DocBook.",
# 						"GlossSeeAlso": ["GML", "XML"]
#                     },
# 					"GlossSee": "markup"
#                 }
#             }
#         }
#     }
# }


# [
#     {
#         "id": 2,
#         "name": "An ice sculpture",
#         "price": 12.50,
#         "tags": ["cold", "ice"],
#         "dimensions": {
#             "length": 7.0,
#             "width": 12.0,
#             "height": 9.5
#         },
#         "warehouseLocation": {
#             "latitude": -78.75,
#             "longitude": 20.4
#         }
