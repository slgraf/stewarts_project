import Tkinter, tkFileDialog
from FileBrowser import *
import os

global filepath
filepath = ''

class Tk_GUI():
	def __init__(self):
		self.root = Tkinter.Tk()
		self.markup = ''

		# define frames
		main_frame = Tkinter.Frame(self.root, height=300, width=500)
		main_frame.pack()

		top_frame = Tkinter.Frame(main_frame, height=150, width=500)
		top_frame.pack(side=Tkinter.TOP)

		bot_frame = Tkinter.Frame(main_frame, height=150, width=500)
		bot_frame.pack(side=Tkinter.BOTTOM)

		left_frame = Tkinter.Frame(top_frame, height=10, width=100)
		left_frame.pack(side=Tkinter.LEFT)

		right_frame = Tkinter.Frame(top_frame, height=10, width=100)
		right_frame.pack(side=Tkinter.RIGHT)

		inside_right_frame = Tkinter.Frame(right_frame, height=10, width=100)
		inside_right_frame.pack(side=Tkinter.RIGHT)
		
		self.filepath_entry = Tkinter.Entry(left_frame, width=75, state='normal', text=filepath)
		self.filepath_entry.pack(side=Tkinter.LEFT)

		self.filebrowser_btn = Tkinter.Button(left_frame, text='Browse Files', command=self.open_browser, padx=5)
		self.filebrowser_btn.pack(side=Tkinter.RIGHT)

		self.markup_label = Tkinter.Label(right_frame, text='	Markup: ')
		self.markup_label.pack(side=Tkinter.LEFT)

		self.markup_entry = Tkinter.Entry(inside_right_frame, width=5, state='normal', text=self.markup)
		self.markup_entry.pack(side=Tkinter.LEFT)

		self.markup_btn = Tkinter.Button(inside_right_frame, padx=3, text='Enter', command=self.setup)
		self.markup_btn.pack(side=Tkinter.RIGHT)

	def open_browser(self):
		browser = FileBrowser()
		filepath = browser.openfile()
		self.filepath_entry.insert(0, filepath)

	def run(self):
		self.root.mainloop()

	def setup(self):
		self.markup = int(self.markup_entry.get())
		self.filepath = self.filepath_entry.get()

if __name__ == '__main__':
	t = Tk_GUI()
	t.run()
