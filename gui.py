import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import simpledialog
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showerror
from tkinter.messagebox import showinfo

from huffman import HuffmanCoder

import pickle


#
class FileCase:

	"""."""
	def __init__(self, master):
		self.filename = ""





		# Frames for the home window of FileCase.
		frame1 = Frame(master)
		frame2 = Frame(master)
		frame3 = Frame(master)
		frame4 = Frame(master)
		frame5 = Frame(master)
		frame1.pack()
		frame2.pack()
		frame3.pack()
		frame4.pack()
		frame5.pack()

		# A welcome label.
		self.welcomeLabel = Label(frame1, text = "FileCase: Lossless File Compressor and Encryptor", font = ("Helvetica", 16))
		self.welcomeLabel.grid(row = 0)

		# A label for the loaded filename. Initialized as "You have not selected a file yet." until the user selects a file.
		self.filenameLabel = Label(frame2, text = "You have not selected a file yet.", font = ("Helvetica", 14))
		self.filenameLabel.grid(row = 1)

		# A Button that opens a file select window for the user to select a file to compress/encrypt.
		self.loadfileButton = Button(frame3, text = "Load File", font = ("Helvetica", 13), command = self.load_file)
		self.loadfileButton.grid(row = 2)

		# A Button that opens a file select window for the user to select a file to compress/encrypt.
		self.compressButton = Button(frame4, text = "Compress File", font = ("Helvetica", 13), command = self.load_file)
		self.compressButton.grid(row = 3, column = 0)

		# A Button that opens a file select window for the user to select a file to decompress/decrypt.
		self.decompressButton = Button(frame4, text = "Decompress File", font = ("Helvetica", 13), command = self.load_file)
		self.decompressButton.grid(row = 3, column = 1)

		# Checkbox that determines whether to encrypt the file being compressed or not.
		self.encryptBoolean = IntVar()
		self.encryptBooleanCheckbox = Checkbutton(frame5, text = "Encrypt the File to Compress", variable = self.encryptBoolean)
		self.encryptBooleanCheckbox.grid(row = 4)




	"""."""
	def load_file(self):
		return


	"""."""
	def updateFilenameLabel(self):
		return


	"""."""
	def compress(self):
		if self.encryptBoolean.get():
			print("checked")

		else:
			print("not checked")

		return







	"""."""
	def decompress(self):
		return


	"""."""





# Run the application.
root = Tk()
root.title("FileCase: Lossless File Compression and Encyption")
app = FileCase(root)

while True:
	try:
		root.mainloop()
		break
	except UnicodeDecodeError: # Added to avoid the program crashing when scrolling.
		pass