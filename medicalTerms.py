# functions for exploiting a medical terms dictionary for reducing spelling mistakes

from utility import *
from fuzzywuzzy import fuzz

medicalSet = None

"""
Outputs a table of single-words medical terms
with the minimum length of (minWordLen)
"""
def parseMedicalTerms(inFile, minWordLen=5, printProgress=True):
	#import pdb
	#pdb.set_trace()
	global medicalSet
	if medicalSet != None:
		return medicalSet
		
	if printProgress:
		print("Parsing medical terms dictionary")
	with open(inFile) as f :
		terms = f.read()
	terms = terms.split()
	i = 0
	while i < len(terms):
		if printProgress:
			print(progressBar(i, len(terms), 50), end="\r")
		if len(terms[i]) < minWordLen:
			del terms[i]
		else:
			i+=1
	
	if printProgress:
		print(" "*50, end="\r")
	
	medicalSet = terms
	
	return terms


"""
Loops through words in the given string and replaces them with a term from
the terms list if they are close enough (Levenshtein distance>= threshold)
Then returns the corrected string

Requires fuzzywuzzy :
pip3 install fuzzywuzzy python-Levenshtein
"""
def correctMistakes(terms, string, threshold=95, minWordLen=5):
	for i in range(len(string)):
		if len(string[i])>=minWordLen :
			for j in terms:
				if fuzz.ratio(string[i],j) >= threshold :
					string[i] = j
					break
	return string
