import csv

csvfile = open('data-text.csv', 'r')
reader = csv.reader(csvfile)

for row in reader:
	print (row)

