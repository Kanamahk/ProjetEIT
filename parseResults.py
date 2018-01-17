#!/usr/bin/python3

import sys

if len(sys.argv) != 3 :
	print("Produces statistics from Wapiti outputs")
	print("Usage: "+sys.argv[0]+" <original labeled file> <machine-labeled file>")
	sys.exit(1)

with open(sys.argv[1]) as o:
	original = o.readlines()
with open(sys.argv[2]) as m:
	machine = m.readlines()
	
# should be unneeded, but we can't trust the upstream too much
# removes empty cells (lines)
machine = [x for x in machine if x.strip()]


# three items per class :
# number of appearances in corpus,
# number of right guesses
# number of wrong guesses
classes = {}

# so in theory the line ńumbers are synced, saving us some work

for i in range(len(machine)):
	# get a list of classes
	o = original[i].split()[-1]
	m = machine[i].split()[-1]
	o = o.split()
	m = m.split()
	
	for j in o :
		if j in classes :
			classes[j][0]+=1
		else:
			classes[j] = [1,0,0]
		if j in m :
			classes[j][1]+=1
	for j in m : # a bit wasteful, but eh
		if j not in o :
			if j in classes :
				classes[j][2]+=1
			else:
				classes[j] = [0,0,1]
			



# collecting stats

# this times it's :
# error rate
# precision
# recall
stats = {}
print(len(classes))
for i in classes.items() :
	stats[i[0]] = [0.0,0.0,0.0]
	# (FN + FP) / N
	try:
		stats[i[0]][0] = (1-i[1][1]) / i[1][0]
	except ZeroDivisionError:
		stats[i[0]][0] = 1
	# VP / (VP + FP)
	try:
		stats[i[0]][1] = i[1][1] / (i[1][1]+i[1][2])
	except ZeroDivisionError:
		stats[i[0]][1] = 1
	# VP / (VP + FN)
	try:
		stats[i[0]][2] = i[1][1] / (i[1][1]+ (i[1][0]-i[1][1])) #FIXME : I think I messed up
	except ZeroDivisionError:
		stats[i[0]][2] = 1


# then we iterate through to average those to get a global idea

averages = [0.0,0.0,0.0]


for i in stats.items() :
	averages[0] += i[1][0]
	averages[1] += i[1][1]
	averages[2] += i[1][2]

	
averages[0] /= len(stats)
averages[1] /= len(stats)
averages[2] /= len(stats)

print("total error rate : "+str(averages[0]*100))
print("total precision : "+str(averages[1]*100))
print("total recall : "+str(averages[2]*100))# You are not you, you are me.
