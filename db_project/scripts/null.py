import csv

results = []
with open("struct.csv") as csvfile:
    reader = csv.reader(csvfile) 
    for row in reader:
        results.append(row)


for data in results:
	if(data == []):
		data.append('Null')
	else:
		continue



wtr = csv.writer(open ('structidnull.csv', 'w'),  lineterminator='\n')
for x in results : wtr.writerow (x)
