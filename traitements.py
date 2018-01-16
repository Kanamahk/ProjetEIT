#-*-coding:utf-8-*-
import re 
import collections

def faireTraitements(data):
	for line in data:
		line = basicTraitement(line)
    
    return data

def basicTreatments(line):
	line = line.lower()
	
	line = re.sub("[\']", ' ', line)
	line = re.sub("[`â€˜â€™â‰ªâ‰«â€œâ€,;:!?./-]", '', line) #choix d'echanger le tiret par un vide
	
	line = re.sub("[éèê]", 'e', line)
	line = re.sub("[îï]", 'i', line)
	line = re.sub("[ô]", 'o', line)
	line = re.sub("[oe]", 'oe', line)
		
	return line
	
def supressionMotsInutiles(line):

	#motsInutiles = ["le", "la", "les", "du", "de", "des", "au", "aux"]
	
	return line
	

def creationListeMots(data):
	dic = []
	
	