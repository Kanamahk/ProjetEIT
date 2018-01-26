#-*-coding:utf-8-*-
import re 
import collections
from medicalTerms import *

def faireTraitements(data, useDico=None):
	data2=[]
	for line in data:
		treatedLine = basicTreatments(line[0])
		data2.append((treatedLine, line[1], line[2]))
	
	if useDico != None:
		print("Correcting mistakes")
		#import pdb
		#pdb.set_trace()
		for i in range(len(data2)):
			buf=""
			sentence = data2[i][0].split()
			for j in range(len(sentence)):
				try:
					buf+=" "+useDico[sentence[j]]
				except KeyError:
					buf+=" "+sentence[j]
			buf.strip()
			data2[i]=(buf, data2[i][1], data2[i][2])
			print(progressBar(i, len(data2), 50), end="\r")
		print(" "*50, end="\r")
		
	return data2

def basicTreatments(line):
	if line != '':
		line = line.lower()
		
		line = re.sub("[\'_,]", ' ', line)

		line = re.sub("\(([^ ])", r" ( ", line) # separate ( from following word if a space 
		line = re.sub("([^ ])\(", r" ( ", line) # separate ( from following word if a space
		line = re.sub("\)([^ ])", r" ) ", line) # separate ) from following word if a space 
		line = re.sub("([^ ])\)", r" ) ", line) # separate ) from following word if a space
		
		line = re.sub("\+([^ ])", r" + ", line) # separate ) from following word if a space 
		line = re.sub("([^ ])\+", r" + ", line) # separate ) from following word if a space
		
		line = re.sub("[,;:!?.-]", '', line) #choix d'echanger le tiret par un vide
		
		line = re.sub("[éèêë]", 'e', line)
		line = re.sub("[îï]", 'i', line)
		line = re.sub("[ôö]", 'o', line)
		line = re.sub("[àâ]", 'a', line)
		line = re.sub("ç", 'c', line)
		line = re.sub("[œ]", 'oe', line)
		
		line = re.sub("[ ]+", ' ', line)
		
	return line

def useDicoFct(data):
	medicalTerms = parseMedicalTerms("medicalTerms", 5)
	
	return buildSubstitutionTable(medicalTerms, data,{},95,5) 

def supressionMotsInutiles(line):
	motsInutiles = ["le", "la", "les", "du", "de", "des", "au", "aux", "a", "avec", "et", "en", "l", "un", "une", "c"]
	
	for word in line:
		if word in motsInutiles:
			word = ""
	
	return line
	

def creationListeMots(data):
	dic = []
	for line in data:
		for word in line.split(" "):
			if word in dic.keys():
				dic[word] += 1
			else:
				dic[word] = 1
	return dic
	
