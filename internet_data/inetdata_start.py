#! /usr/bin/env python

#
# Example fetching data feom the web
#
try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen

from pprint import pprint 

def main():
	webUrl = urlopen("http://www.google.com")
	print("result code: " + str(webUrl.getcode()))
	data = webUrl.read()
	pprint(data)


if __name__ == "__main__":
	main()