#!/usr/bin/python3
#-*-coding:utf-8-*-

import os
import sys
from parser import *
#from readFileFonctions import getFileByLine
#from writeInFileFunctions import write_dict

#reviewsdirectory = "./reviews"

maSuperExtension = ".passurgit"

if __name__=="__main__":
	if "-s" in sys.argv :
		save = True
		modelName = sys.argv[sys.argv.index("-s")+1]
	else:
		save = False
		modelName = "modelUcode"
		
	if "-m" in sys.argv :
		model = sys.argv[sys.argv.index("-t")+1]
		dictTag = parseModel(model)
	else:
		dictTag = {}
		dictTag["enfant"] = 'u0'
	
	# training file	
	if "-t" in sys.argv :
		trainFile = sys.argv[sys.argv.index("-t")+1]
	else:
		#trainFile = "../CLEFeHealth2017Task1_training_FR1/corpus/train/AlignedCauses_2006-2012full.csv"
		trainFile = "../CLEFeHealth2017Task1_training_FR1/corpus/train/train.csv"
	
	if "-e" in sys.argv :
		evalFile = sys.argv[sys.argv.index("-e")+1]
	else:
		#evalFile = "../CLEFeHealth2017Task1_training_FR1/corpus/train/AlignedCauses_2006-2012full.csv"
		evalFile = "../CLEFeHealth2017Task1_training_FR1/corpus/train/eval.csv"
	
	if "-ngramW" in sys.argv :
		ngramW = int(sys.argv[sys.argv.index("-ngramW")+1])
	else:
		ngramW = 1
	
	if "-ngramC" in sys.argv :
		ngramCTraitement = True
		ngramC = int(sys.argv[sys.argv.index("-ngramC")+1])
	else:
		ngramCTraitement = False
		ngramC = 0
		
	if "-p" in sys.argv :
		useParenthese = True
	else :
		useParenthese = False
	
	if "-cs" in sys.argv :
		codeSimplifie = True
	else :
		codeSimplifie = False
	
	trainFileContent = getFileByLine(trainFile)
	evalFileContent = getFileByLine(evalFile)

	trainData = parseCSV(trainFileContent, codeSimplifie)
	evalData = parseCSV(evalFileContent, codeSimplifie)

	if "-dico" in sys.argv :
		useDico = useDicoFct(trainData+evalData)
	else :
		useDico = None
		
	
	trainDataParsed = dataToUlist(trainData, dictTag, ngramW, ngramCTraitement, ngramC, useDico, useParenthese)
	evalDataParsed = dataToUlist(evalData, dictTag, ngramW, ngramCTraitement, ngramC, useDico, useParenthese)

	
	writeFile(trainDataParsed, "trainData"+maSuperExtension)
	writeFile(evalDataParsed, "evalData"+maSuperExtension)
	
	if save : 
		writeModel(dictTag, modelName+maSuperExtension)
	
	
