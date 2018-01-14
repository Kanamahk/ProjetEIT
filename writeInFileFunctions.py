#-*-coding:utf-8-*-

def write_word_file(wordList, fileName):
	file_pointer = open(fileName, "w")
	for word in wordList:
		file_pointer.write(word)	
		file_pointer.write("\n")
	file_pointer.close()

def write_word_list_file(wordlist, fileName):
	with open(fileName, "w") as filepointer:
		for word in wordlist:
			filepointer.write(word+"\n")  


def write_paragraph_file(paragraphs, fileName):
	with open(fileName, "w") as filepointer:
		for paragraph in paragraphs:
			filepointer.write(paragraph+"\n")

def write_tab_separated_file(rows, fileName):
	with open(fileName, "w") as filepointer:
		for row in rows:
			filepointer.write("\t".join(row)+"\n") 

def write_dict(dictionary, fileName):
	with open(fileName, "w+") as filepointer:
		for tok in dictionary:
			filepointer.write(tok+" : " + str(dictionary[tok]) +"\n")

