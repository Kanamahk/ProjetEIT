#!/usr/bin/python3
#-*-coding:utf-8-*-

import os
import sys
from parser import *
from readFileFonctions import getFileByLine
#from writeInFileFunctions import write_dict

#reviewsdirectory = "./reviews"


if __name__=="__main__":
	if "-s" in sys.argv :
		save = True
		modelName = sys.argv[sys.argv.index("-t")+1]
	else:
		save = False
		modelName = ""
		
	if "-m" in sys.argv :
		model = sys.argv[sys.argv.index("-t")+1]
		DictTag = parseModel(model)
	else:
		DictTag = {}
		DictTag["enfant"] = 'u0'
	
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
		
	
	
	trainFileContent = getFileByLine(trainFile)
	evalFileContent = getFileByLine(evalFile)

	traindata = parseCSV(trainFileContent, True)
	evalData = parseCSV(evalFileContent, True)
	
	trainDataParsed = dataToUlist(traindata, DictTag, ngramW, ngramCTraitement, ngramC)
	evalDataParsed = dataToUlist(evalData, DictTag, ngramW, ngramCTraitement, ngramC)

	
	writeFile(trainDataParsed, "trainData")
	writeFile(evalDataParsed, "evalData")
	
	if save : 
		writeModel(DictTag, modelName)
	
	
