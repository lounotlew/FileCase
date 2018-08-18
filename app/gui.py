import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import simpledialog
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showerror
from tkinter.messagebox import showinfo

from app.huffman import HuffmanCoder

import os
import pickle


#
class FileCase:

	"""


	   Attributes (outside of tkinter buttons/labels):
	   - self.filename:
	   - self.file_ext:
	   - self.filepath: 


	"""
	def __init__(self, master):
		self.filename = ""
		self.file_ext = ""
		self.filepath = ""

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
		self.compressButton = Button(frame4, text = "Compress File", font = ("Helvetica", 13), command = self.compress_file)
		self.compressButton.grid(row = 3, column = 0)

		# A Button that opens a file select window for the user to select a file to decompress/decrypt.
		self.decompressButton = Button(frame4, text = "Decompress File", font = ("Helvetica", 13), command = self.decompress_file)
		self.decompressButton.grid(row = 3, column = 1)

		# Checkbox that determines whether to encrypt the file being compressed or not.
		self.encryptBoolean = IntVar()
		self.encryptBooleanCheckbox = Checkbutton(frame5, text = "Encrypt the File to Compress", variable = self.encryptBoolean)
		self.encryptBooleanCheckbox.grid(row = 4)




	"""."""
	def load_file(self):
		self.filepath = askopenfilename(title = "Choose a file to compress.",
			filetypes = (("text files","*.txt"), ("doc files","*.docx"), ("jpg files","*.jpg"), ("jpeg files","*.jpeg")))

		if self.filepath == "" or None:
			return

		self.filename = self.filepath.split("/")[-1]
		self.file_ext = os.path.splitext(self.filepath)[1]

		if self.file_ext == ".docx":
			showinfo("Warning", "You have selected a Word document. Please make sure the file does not contain any images.")
			self.updateFilenameLabel()
			return

		# Image if:

		self.updateFilenameLabel()
		return




	"""."""
	def updateFilenameLabel(self):
		self.filenameLabel['text'] = self.filename

		return

	"""."""
	def compress_file(self):
		if self.filepath == "" or None:
			showinfo("Compression Error", "Please load a file first.")
			return

		if self.encryptBoolean.get():
			print("checked")

		else:
			huffmanCoder = HuffmanCoder(self.filepath)
			huffmanCoder.print_attrs()

		return







	"""."""
	def decompress_file(self):
		return


	"""."""
