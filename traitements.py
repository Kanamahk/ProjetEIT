#-*-coding:utf-8-*-
import re 
import collections

def faireTraitement(data):
    i = 0
    ret = ""
    while i < len(data):
        if(data[i] != '.' or data[i] != ',' or data[i] != ';' or data[i] != '!' or data[i] != '?' or data[i] != ':'):
            ret += data[i]
        else:
            i = i + 1
        i = i + 1
    return ret
	data = basicTraitement(data)

	return data
	
def basicTraitement(data):
	for line in data:
		line = line.lower()
	return data;