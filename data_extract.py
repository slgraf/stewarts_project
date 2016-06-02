import csv
import homes as h
from pyzillow.pyzillow import ZillowWrapper, GetDeepSearchResults

#notes:  
# skip first row of csv containing headers of each column when calling api
# also pull list price
# allow file path to change from GUI input
# need to add a list of home objects

class DataExtract():



	@staticmethod
	def extractFromCSV( filePath ):

		#test filepath???

		#file = open('textexport.csv') 
		file = open(filePath) 

		csv_file = csv.reader(file)
			
		for row in csv_file:
			#print row[33]
			#print row[33, 35, 36]
			
			addr = (row[33], row[35], row[36], row[39])
			addr = ' '.join(addr)

			zipcode = (row[45])

			price = (row[24])

			home = h.Home(addr, zipcode, price)


		#print address - test only
		#print home.addr

		file.close()

		return home


	@staticmethod
	def apiCall( address, zipcode ):

		#source:
		#https://github.com/hanneshapke/pyzillow

		#address = '2928 W WAGONER RD'
		#zipcode = '85053'

		zillow_data = ZillowWrapper("X1-ZWz1fak7wz8iyz_4lr3d")
		deep_search_response = zillow_data.get_deep_search_results(address, zipcode)
		result = GetDeepSearchResults(deep_search_response)

		result.zillow_id # zillow id, needed for the GetUpdatedPropertyDetails

		#print result

		print result.zillow_id
		print result.home_detail_link

		#print deep_search_response

		#return tuple
		# https://stackoverflow.com/questions/9752958/how-can-i-return-two-values-from-a-function-in-python
		#return (zestimate, home_detail_link)


	@staticmethod
	def test():

		print "5"