#-*-coding:utf-8-*-

from collections import OrderedDict
from traitements import *
import os
import csv

def getFileByLine(fileName): 
	file_pointer = open(fileName, "r")
	contents = []
	for line in file_pointer.readlines():
		contents.append(line)
	file_pointer.close()
	return contents

def parseCSV(fichier, boolCodeSimplifie, fichierSansCode):
	reader = csv.reader(fichier, delimiter=";")
	tokens=[]
	for row in reader:
		if fichierSansCode:
			label = ""
		else:
			label = row[-1]
			if boolCodeSimplifie:
				if len(label) > 3:	
					label = label[:3]
		
		estEnfant = row[3] == 0
			
		tokens.append((row[6], label, estEnfant))
	return tokens
	
def parseModel(model):	
	file_pointer = open(fileName, "r")
	DictTag = {}
	for (word, ucode) in file_pointer.readlines().split(":"):
		DictTag[word] = ucode
	file_pointer.close()
	return DictTag

'''
prend une liste de tuple contenant en premier element une string contenant les causes et en deuxieme element une string contenant le code associe
retourne un dictionnaire prenant en cle un code et en element une liste des elements à utiliser
'''
def dataToUlist(data, DictTag, ngramW, ngramCTraitement, ngramC, useDico, useParenthese):
	tupleList = []
	
	if False:
		data = faireTraitements(data, useDico)
	
	for line in data:
		listeTag = []
		if line[2]:
			listeTag.append(DictTag["enfant"])
		listeTag = listeTag + traitementCauses(line[0], DictTag, ngramW, ngramCTraitement, ngramC, useParenthese)
		
		tupleList.append((line[1], listeTag))
	return tupleList;

def traitementCauses(causes, DictTag, ngramW, ngramCTraitement, ngramC, useParenthese):
	liste = []
	
	liste += ngramWord(causes, DictTag, ngramW)
	
	if useParenthese:
		liste += parenthese(causes, DictTag)
	
	if ngramCTraitement:
		liste += ngramChar(causes, DictTag, ngramC)
	
	return liste
	
def ngramWord(causes, DictTag, n):
	liste = []
	if n < 1:
		return liste
		
	words = causes.split(" ")
	if n > 1:
		words = ["DEBUT_PHRASE_TOKEN"] + words + ["FIN_PHRASE_TOKEN"]
		
	#for word in words:
	for i in range(0, len(words) - (n-1)):
		word = ""
		for j in range(0, n):
			if j != 0:
				word += "_"
			word += words[i+j]
		
		if word not in DictTag.keys():
			DictTag[word] = 'u' + str(len(DictTag))

		liste.append(DictTag[word])
		
	return liste + ngramWord(causes, DictTag, n-1)

def ngramChar(causes, DictTag, n):
	liste = []
	
	if(n < 3):
		return liste
	
	causeTmp = causes
	if(len(causes) > n):
		for i in range(0, len(causes)-n):
			ngram = causeTmp[:3]
			if ngram not in DictTag.keys():
				DictTag[ngram] = 'u' + str(len(DictTag))
			causeTmp = causeTmp[1:]
			liste.append(DictTag[ngram])
	return liste + ngramChar(causes, DictTag, n-1)

	
def parenthese(causes, DictTag):
	liste = []	
	words = causes.split(" ")
	
	if "(" in words or ")" in words:
		do = False
		for word in words:
			if word == "(":
				do = True
			if do:
				if word+"_PARENTHESE" not in DictTag.keys():
					DictTag[word+"_PARENTHESE"] = 'u' + str(len(DictTag))
				liste.append(DictTag[word+"_PARENTHESE"])
	return liste
	
def writeFile(trainTupleList, filename, fichierSansCode):
	with open(filename, "w+") as filepointer:
		for Tuple in trainTupleList:
			for ucode in Tuple[1]:
				filepointer.write(str(ucode) + " ")
			if not fichierSansCode:	
				filepointer.write(str(Tuple[0] if not Tuple[0] =='' else "NULL") +"\n")

def writeModel(DictTag, filename):
	with open(filename, "w+") as filepointer:
		for key in DictTag.keys():
			filepointer.write(str(key) + ":" + str(DictTag[key]+"\n"))


