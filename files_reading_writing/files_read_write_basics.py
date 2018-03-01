#! /usr/bin/env python
def main():

	#Open a file for writing 

	#f = open("textfile.txt", "w+")

	# Open the file for appending text to the end 

	f = open("textfile.txt", "r")

	# Write some lines of data to the file 

	# for i in range(10):
	# 	f.write("This is line " + str(i) + "\r\n")


	#close file
	#f.close()

	# Open the file backup and read contents

	# readline() reads one line character at a time, readlines() reads in the whole file at once and splits it by line.

	if f.mode == 'r':
		#contents = f.read()
		#print contents

		fl = f.readlines()
		for x in fl:
			print x



if __name__ == '__main__':
   main()