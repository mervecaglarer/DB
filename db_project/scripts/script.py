import csv
import operator
sample=open('intwall.csv', "r")
csv1=csv.reader(sample)

list=[]
with open("intwallnew.csv", "w+") as f:
	fileWriter = csv.writer(f)
	for row in sample:
		for eachline in csv1:
			if (eachline in list):
				pass
			elif (eachline==['INTWALL']):
				pass
			else :
				list.append(eachline)
				fileWriter.writerow(eachline)
