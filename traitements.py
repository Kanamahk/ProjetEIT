#-*-coding:utf-8-*-

import re 
import collections

def faireTraitement(data):
	data = basicTraitement(data)

	return data
	
def basicTraitement(data):
	for line in data:
		line = line.lower()
	return data;