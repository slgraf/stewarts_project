from Tkinter import Tk
from tkFileDialog import askopenfilename
import os

class FileBrowser():
	def __init__(self):
		Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
		
	def openfile(self):
		return askopenfilename()
		
	def getfilename(self):
		return filename

if __name__ == '__main__':
	f = FileBrowser()
