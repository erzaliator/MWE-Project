from collections import Counter
from numpy import *
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
	x=zeros((lenny, lenny), int)
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
				#now counter will contain list of all unique words in a sentence and not the entire corpus
				counter = getwordbins(sentence)
				print counter
				
				for key, value in counter.most_common():
					if value > 0:
						if key != '':
							sentenceuniquearray.append(key)
				for wordsofsentence in sentenceuniquearray:
					freq=counter[wordsofsentence]
				smalllenny=len(sentenceuniquearray)
				for flexingram in xrange(2,8,1):
				#flexigram is the length of the variable ngram starting from a bigram. 8 is assumed to be the lenght of the largest sentence in the corpus
					for flexicounter in xrange(len(sentence)-flexingram+1):
					#flexicounter is iterating one ngram in the sentence at a time
						for ngramlength in xrange(flexingram):
						#ngramlenght is each element in the ngram starting from index index flexicounter
							print sentence[flexicounter+ngramlength]
						print "----------------"

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


main('input_matrixgenerator.txt')
