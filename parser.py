#-*-coding:utf-8-*-

from collections import OrderedDict
from traitements import *
import os
import csv


'''
datasDirectory = "./data"

def getFisherDict(params):
	if len(params) > 0:
		if os.path.exists("./fisher"):
			myFisherFileName = os.listdir("./fisher")
			if (len(myFisherFileName) == 1) && (myFisherFileName[0] == "fisher.txt"):
				return FisherDictFromFile()		
	return createFisherFile(params)

def FisherDictFromFile():
	dictionary = {}
	with open("fisher/fisher.txt", "r") as filepointer:
		for line in filepointer.readlines():
			item = line.strip().split(" ; ")
			dictionary[item[0]] = (item[1], item[2])
	return dictionary


def createlisteFisherDict(params): #param est une liste 
	if os.path.exists("datasDirectory"):
		myDatasFileName = os.listdir("datasDirectory")
		myDatas = []
		dictionary = {}
		for r in myDatasFileName:
			myDatas.append(getFileByLine(reviewsdirectory + '/' + r))
		for r in myDatas:
			dictionary = addDataToFisher(r, dictionary, params)
		return dictionary

def WriteFisherFile(dict):
	with open("fisher", "w+") as filepointer:
		for (wordInDict, ident) in dict.items():
			filepointer.write(wordInDict + ";" + ident + "\n")
	




def addDataToFisher(data, currentFisher, params):   #param est une liste 
	for param in params:
		if param == "words":
			currentFisher = addWordFromDataToFisher(data, currentFisher)
		if param == "bigramw":
		if param == "trigramc":
	return currentFisher


def addWordFromDataToFisher(data, currentFisher):
	words = data.split(" ")
	
	for word in words:
		if not(word in words.item()):
			currentFisher.append({word:len(currentFisher)})
	return currentFisher



'''

def parseCSV(fichier, boolCodeSimplifie):
	reader = csv.reader(fichier, delimiter=";")
	tokens=[]
	for row in reader:
	
		label = row[-1]
		if boolCodeSimplifie:
			if len(label) > 3:	
				label = label[:3]
		
		estEnfant = row[3] == 0
			
		tokens.append((row[6], label, estEnfant))
	return tokens
'''	
def parseCSVTrain(fichier):
	reader = csv.reader(fichier, delimiter=";")
	tokens=[]
	for row in reader:
		if len(row[-1]) > 3:	
			label = row[-1][:3]
		else:
			label = row[-1]
		tokens.append((row[6], label))
	return tokens

def parseCSVEval(fichier):
	reader = csv.reader(fichier, delimiter=";")
	tokens=[]
	for row in reader:
		tokens.append(row[6])
	return tokens
'''


'''
prend une liste de tuple contenant en premier element une string contenant les causes et en deuxieme element une string contenant le code associe
retourne un dictionnaire prenant en cle un code et en element une liste des elements à utiliser
'''
def dataToUlist(data, DictTag, ngramW, ngramCTraitement, ngramC):
	tupleList = []
	
	#
	# Inserer traitement de data
	#
	data = faireTraitement(data) #ou qqchose comme ça
	
	for line in data:
		listeTag = []
		if line[2]:
			listeTag.append(DictTag["enfant"])
		listeTag = listeTag + traitementCauses(line[0], DictTag, ngramW, ngramCTraitement, ngramC)
		
		tupleList.append((line[1], listeTag))
	return tupleList;

def traitementCauses(causes, DictTag, ngramW, ngramCTraitement, ngramC):
	liste = []
	
	liste += ngramWord(causes, DictTag, ngramW)
	
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
		
	for word in words:
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
	
	
def writeFile(trainTupleList, filename):
	with open(filename, "w+") as filepointer:
		for Tuple in trainTupleList:
			for ucode in Tuple[1]:
				filepointer.write(str(ucode) + " ")
			filepointer.write(str(Tuple[0] if not Tuple[0] =='' else "NULL") +"\n")

			'''
def writeTrainFile(trainTupleList):
	with open("trainData", "w+") as filepointer:
		for Tuple in trainTupleList:
			for ucode in Tuple[1]:
				filepointer.write(str(ucode) + " ")
			filepointer.write(": " + str(Tuple[0]) +"\n")

def writeEvalFile(evalList):
	with open("evalData", "w+") as filepointer:
		for line in evalList:
			for ucode in line:
				filepointer.write(str(ucode) + " ")
			filepointer.write("\n")
'''




