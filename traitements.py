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
	line = line.lower()
	
	line = re.sub("[\'_]", ' ', line)
	line = re.sub("[`â€˜â€™â‰ªâ‰«â€œâ€,;:!?./-\(\) &]", '', line) #choix d'echanger le tiret par un vide
	
	line = re.sub("[éèê]", 'e', line)
	line = re.sub("[îï]", 'i', line)
	line = re.sub("[ô]", 'o', line)
	line = re.sub("[œ]", 'oe', line)
		
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
	