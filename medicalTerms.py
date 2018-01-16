# functions for exploiting a medical terms dictionary for reducing spelling mistakes

from utility import *
from fuzzywuzzy import fuzz

"""
Outputs a table of single-words medical terms
with the minimum length of (minWordLen)
"""
def parseMedicalTerms(inFile, minWordLen=5, printProgress=True):
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
	
	return terms


"""
Loops through words in the given string and replaces them with a term from
the terms list if they are close enough (Levenshtein distance>= threshold)
Then returns the corrected string

Requires fuzzywuzzy
"""
def correctMistakes(terms, string, threshold=95, minWordLen=5):
	for i in range(len(string)):
		if len(string[i])>=minWordLen : # I went from hours to seconds (literally) with this check, pls leave in place
			for j in terms:
				if fuzz.ratio(string[i],j) >= threshold :
					string[i] = j
					break
