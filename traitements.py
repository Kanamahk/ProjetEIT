#-*-coding:utf-8-*-
import re 
import collections

def faireTraitements(data):
	data2=[]
	for line in data:
		treatedLine = basicTreatments(line[0])
		data2.append((treatedLine, line[1], line[2]))
	return data2

def basicTreatments(line):
	if line != '':
		line = line.lower()
		
		line = re.sub("[\'_,]", ' ', line)

		line = re.sub("\(([^ ])", r" ( ", line) # separate ( from following word if a space 
		line = re.sub("([^ ])\(", r" ( ", line) # separate ( from following word if a space
		line = re.sub("\)([^ ])", r" ) ", line) # separate ) from following word if a space 
		line = re.sub("([^ ])\)", r" ) ", line) # separate ) from following word if a space
		
		line = re.sub("[,;:!?.-]", '', line) #choix d'echanger le tiret par un vide
		
		line = re.sub("[éèêë]", 'e', line)
		line = re.sub("[îï]", 'i', line)
		line = re.sub("[ôö]", 'o', line)
		line = re.sub("[àâ]", 'a', line)
		line = re.sub("ç", 'c', line)
		line = re.sub("[œ]", 'oe', line)
		
		line = re.sub("[ ]+", ' ', line)
		
	return line
	
def supressionMotsInutiles(line):

	#motsInutiles = ["le", "la", "les", "du", "de", "des", "au", "aux"]
	
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
	