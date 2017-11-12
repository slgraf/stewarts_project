class Home:
   'Class for homes: store information from the csv and api calls'
   homeCount = 0

   def __init__(self, addr, zipcode, price):
      self.addr = addr
      self.zipcode = zipcode
      self.price = price

      #Home.homeCount += homeCount

   def apicall(self):
      #assign data pulled from api call