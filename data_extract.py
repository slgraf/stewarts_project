import csv
import homes as h

#notes:  
# skip first row of csv containing headers of each column when calling api
# also pull list price
# allow file path to change from GUI input
# need to add a list of home objects

file = open('textexport.csv') 

homes = []
addresses = []
zipcodes = []
listprices = []

csv_file = csv.reader(file)
	
for row in csv_file:
	#print row[33]
	#print row[33, 35, 36]
	
	addr = (row[33], row[35], row[36], row[39])
	addr = ' '.join(addr)
	#addresses.append(addr)

	zipcode = (row[45])
	#zipcodes.append(zipcode)

	price = (row[24])
	#listprices.append(price)

	home = h.Home(addr, zipcode, price)


#print addresses

print home.addr

file.close()