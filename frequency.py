"""This file generates the frequency of the unique words given by the input file input.txt. It then outputs
the result onto the command line. To read the output later in a file type the command 
'python frequency.py > output.txt' and open the file output.txt. In the ouput, each line has a unique
character and each character has the frequency written in front of it separated by a space."""
from collections import Counter
import re

def openfile_and_replace(filename):
	fh = open(filename, "r+")
	str = fh.read()
	str=str.replace("."," ")
	str=str.replace(","," ")
	str=str.replace("\n"," ")
	str=str.replace("&comma"," ")
	#str=str.replace(";"," ")
	#str=str.replace(":"," ")
	#str=str.replace("!"," ")
	re.sub(' +',' ',str)
	fh.close()
	return str

def getwordbins(words):
	cnt = Counter()
	for word in words:
		cnt[word] += 1
	return cnt
def main(filename):
	txt = openfile_and_replace(filename)
	#txt = removegarbage(txt)
	words = txt.split(' ')
	bins = getwordbins(words)
	for key, value in bins.most_common():
		if value > 5: 
			if key != '':
				print key,value

main('input.txt')
