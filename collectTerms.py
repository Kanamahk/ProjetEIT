#!/usr/bin/python3
# this script parses HTML files from a medical dictionary
# and outputs the formatted names
# unfortunately the source data is imperfect, but oh well

# operates on a set of data collected thusly :
"""
for i in (seq 2376)
 wget http://dictionnaire.academie-medecine.fr/\?q=\&page=$i
end
"""
# (it's not bourne shell syntax, it's a shell called fish)

# then the script is run 
"""
for i in (seq 2376)
 ./collectTerms.py index.html\?q=\&page=$i
end > medicalTerms
"""

# it collects whathever text is tagged as class=term

# also yeah you have to install this, but it's a one-liner
from bs4 import BeautifulSoup

import sys
with open(sys.argv[1]) as f :
	source = f.read()

soup = BeautifulSoup(source, 'html5lib')

htmlTerms = soup.findAll("p", {"class" : "terme"})

terms=[]

for i in htmlTerms :
	text = i.contents[0].text
	
	# conditions
	if len(text) < 3 :
		continue
	
	text = text.replace("®","")
	text = text.replace("™","")

	# due to unreliable formatting on website
	text = text.replace("l.m.", "") 
	# there are a bunch of other errors like this, unfortunately.
	# things like "<b>CMR s</b>igle pour"

	# remove bracketed terms
	if "(" in text:
		text = text[:text.rfind("(")]

	text = text.casefold()

	# potentially remove accents ?


	text = text.strip()


	terms.append(text)


for i in terms:
	print(i)
