#!/usr/bin/python3
#-*-coding:utf-8-*-

import os
import sys
import csv
from traitements import *
from collections import OrderedDict

maSuperExtension = ".passurgit"

def getFileByLine(fileName): 
	file_pointer = open(fileName, "r")
	contents = []
	for line in file_pointer.readlines():
		contents.append(line)
	file_pointer.close()
	return contents
	
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
	
def creationListeMots(data):
	dic = {}
	for line in data:
		for word in line[0].split(" "):
			if word in dic.keys():
				dic[word] += 1
			else:
				dic[word] = 1
	return dic

def gardeLesPetitsMots(dic, n):
	dic2 = {}
	for key in dic.keys():
		if len(key) <= n:
			dic2[key] = dic[key]
			
	return dic2
	
def writeDic(dic, filename):
	with open(filename, "w+") as filepointer:
		for key in dic.keys():
			filepointer.write(str(key) + " : " + str(dic[key])+"\n")

if __name__=="__main__":
	if "-f" in sys.argv :
		f = True
		file = sys.argv[sys.argv.index("-f")+1]
	else:
		f = False
		file = "../CLEFeHealth2017Task1_training_FR1/corpus/train/AlignedCauses_2006-2012full.csv"
			
	if "-n" in sys.argv :
		n = int(sys.argv[sys.argv.index("-f")+1])
	else:
		n = 3
	
	fileContent = getFileByLine(file)
	data = parseCSV(fileContent, True)
	
	data = faireTraitements(data)
	
	monDic = creationListeMots(data)
	#monDic = gardeLesPetitsMots(monDic, n)
	
	monDic = OrderedDict(sorted(monDic.items(), key=lambda t: t[1]))
	
	writeDic(monDic, "monDicDeMotsInutile"+maSuperExtension)