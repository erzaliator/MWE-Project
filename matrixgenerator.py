from collections import Counter
from numpy import *
import re
import numpy
from tempfile import mkdtemp
import os.path as path
hello = path.join("./", 'xmas.dat')
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
	#str=str.replace("?",".")
	re.sub(' +',' ',str)
	fh.close()
	return str


def openfile_and_split(filename):
	fh = open(filename, "r+")
	str = fh.read()
	str=str.replace(","," ")
	str=str.replace("\n"," ")
	str=str.replace("&comma"," ")
	#str=str.replace(";"," ")
	#str=str.replace(":"," ")
	#str=str.replace("!"," ")
	#str=str.replace("?",".")
	re.sub(' +',' ',str)
	str=str.split('.')
	fh.close()
	return str

def getwordbins(words):
	cnt = Counter()
	for word in words:
		cnt[word] += 1
	return cnt



def main(filename):
	txt = openfile_and_replace(filename)
	array=list()
	sentenceuniquearray=list()
	txt=txt.replace(","," ")
	txt=txt.replace("\n"," ")
	txt=txt.replace("&comma"," ")
	txt=txt.replace("?",".")
	words = txt.split(' ')
	bins = getwordbins(words)
	for key, value in bins.most_common():
		if value > 0:
			if key != '':
				array.append(key)
	#array contains a list of unique words
	lenny=len(array)
	#x contains the matrix of unique words X unique words
#	x=zeros((lenny, lenny), int)
	x=numpy.memmap(hello, dtype='int', mode='w+', shape=(lenny, lenny))
#	print x
#reading file line by line and then doing the matrix operation
	l=list()
	with open('input_matrixgenerator.txt') as f:
		while True:
			z=f.read(1)
			if not z:
				break
			elif z == ',' or z == '\n':
				None
			elif z == '&comma':
				None
			elif z=='.' or z == '?':
				#in each iteration, ""sentence"" gets overwritten by a new sentence's value
				sentence = ''.join(l)										
				
				#strip deletes all the trailing and leading white spaces
				sentence=sentence.strip(" ")
				sentence=sentence.split(' ')
				#now ""sentence"" is an array of each word of the sentence
				#now counter willcontain list of all unique words in a sentence and not the entire corpus
				counter = getwordbins(sentence)
				for key, value in counter.most_common():
					if value > 0:
						if key != '' or key!= '&comma':
							sentenceuniquearray.append(key)
				for wordsofsentence in sentenceuniquearray:
					freq=counter[wordsofsentence]
				smalllenny=len(sentenceuniquearray)
				for i in xrange(smalllenny):
					for j in xrange(i, smalllenny):
						#ai and aj are indexes in the main matrix
						#whereas i and j will be the value in the individual sentence level matrix's indexes
						ai=array.index(sentenceuniquearray[i])
						aj=array.index(sentenceuniquearray[j])
						if i == j:
							freq1 = counter[sentenceuniquearray[i]]
							freq2 = counter[sentenceuniquearray[i]]-1
							x[ai][aj]+=(freq2*freq1)
						else :
							freq1 = counter[sentenceuniquearray[i]]
							freq2 = counter[sentenceuniquearray[j]]
							product=freq2*freq1
							x[ai][aj]+=product
							x[aj][ai]+=product
				#l needs to get refreshed everytime so that it now contains a fresh list of all the characters in each sentence
				#so does sentence and sentenceuniquearray
				#the counter's instance along with the referenced one in the function needs to be deleted, dont wanna blow up the ram
				del sentence[:]
				del counter
				del sentenceuniquearray[:]
				l=list()
			else:
				l.append(z)	

	f.close()
	print x

main('input_matrixgenerator.txt')
