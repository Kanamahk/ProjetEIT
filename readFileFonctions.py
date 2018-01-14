#-*-coding:utf-8-*-

import re 

def getFile(fileName): 
	file_pointer = open(fileName, "r")
	contents = file_pointer.read() # or readlines() or readline()
	file_pointer.close()
	return contents


def getFileByLine(fileName): 
	file_pointer = open(fileName, "r")
	contents = []
	for line in file_pointer.readlines():
		contents.append(line)
	file_pointer.close()
	return contents


def getTokenFromFile(fileName):
	file_pointer = open(fileName, "r")
	contents = []
	for line in file_pointer.readlines():
		i = 0
		while i < len(line):
			if (line[i] == ',' or line[i] == '.' or line[i] == ':' or line[i] == '?' or line[i] == '!' or line[i] == '\'' or line[i] == '\"' or line[i] == ';'):
				line = line[:i] + ' ' + line[i:]
				i+=1		
			if (line[i] == '\n'):
				line = line[:i] + ' ' + line[(i+3):]
			i+=1
		line = line[:len(line)-1]
		for word in re.split("[\s]+",  line):
			if word != '\n':
				contents.append(word)
	file_pointer.close()
	return contents



def read_paragraph_file(filename):
    paragraphs = []
    with open(filename, "r") as filepointer:
        for line in filepointer.readlines():
            if line.strip()=="": continue # ignore blank paragraphs
            paragraphs.append(line.strip()) # remove whitespace with strip()
    return paragraphs


def read_word_list_file(filename):
    wordlist = []
    with open(filename, "r") as filepointer:
        for line in filepointer.readlines():
            word = line.strip() # remove whitespace
            if word=="": continue # ignore blank lines
            wordlist.append(word)
    return wordlist


def read_tab_separated_file(filename):
    rows = []
    with open(filename, "r") as filepointer:
        for line in filepointer.readlines():
            line = line.strip() # strip on whitespace
            if line=="": continue # ignore blank lines
            rows.append(line.split("\t")) # split on tabs
    return rows 







