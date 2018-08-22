import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import simpledialog
from tkinter import messagebox
from tkinter.filedialog import askopenfilename, askdirectory
from tkinter.messagebox import showerror
from tkinter.messagebox import showinfo

from app.huffman import HuffmanCoder
from app.AESCipher import AESCipher
from app.utils import *

import os
import pickle


# GUI Class for FileCase. Uses HuffmanCoder to compress/decompress.
class FileCase:

	"""GUI Class for FileCase.

	   Attributes (outside of tkinter buttons/labels):
	   - self.filename:
	   - self.file_ext:
	   - self.filepath:
	   - self.destination_path:
	   - self.data_dir:

	   Functions:
	   - load_file():
	   - updateFileNameLabel():
	   - compress_file():
	   - decompress_file():
	"""
	def __init__(self, master):
		self.filename = ""
		self.file_ext = ""
		self.filepath = ""
		self.destination_path = ""
		self.data_dir = ""

		# Frames for the home window of FileCase.
		frame1 = Frame(master)
		frame2 = Frame(master)
		frame3 = Frame(master)
		frame4 = Frame(master)
		frame5 = Frame(master)
		frame6 = Frame(master)
		frame1.pack()
		frame2.pack()
		frame3.pack()
		frame4.pack()
		frame5.pack()
		frame6.pack()

		# A welcome label.
		self.welcomeLabel = Label(frame1, text = "FileCase: Lossless File Compressor and Encrypter", font = ("Helvetica", 16))
		self.welcomeLabel.grid(row = 0)

		# A label for the loaded filename. Initialized as "You have not selected a file yet." until the user selects a file.
		self.filenameLabel = Label(frame2, text = "You have not selected a file yet.", font = ("Helvetica", 14))
		self.filenameLabel.grid(row = 1)

		# A Button that opens a file select window for the user to select a file to compress/encrypt.
		self.loadfileButton = Button(frame3, text = "Load File", font = ("Helvetica", 13), command = self.load_file)
		self.loadfileButton.grid(row = 2)

		# A Button that compresses the loaded file to the user-selected destination path. Only accepts .txt or .docx files.
		self.compressButton = Button(frame4, text = "Compress File", font = ("Helvetica", 13), command = self.compress_file)
		self.compressButton.grid(row = 3, column = 0)

		# A Button that decompresses the loaded file to the user-selected destination path. Only accepts .bin files.
		self.decompressButton = Button(frame4, text = "Decompress File", font = ("Helvetica", 13), command = self.decompress_file)
		self.decompressButton.grid(row = 3, column = 1)

		# A Button that encrypts the loaded file to the user-selected destination path. Only accepts .txt or .docx files.
		self.encryptButton = Button(frame5, text = "Encrypt File", font = ("Helvetica", 13), command = self.encrypt_file)
		self.encryptButton.grid(row = 4, column = 0)

		# A Button that decrypts the loaded file to the user-selected destination path. Only accepts .txt or .docx files.
		self.encryptButton = Button(frame5, text = "Decrypt File", font = ("Helvetica", 13), command = self.decrypt_file)
		self.encryptButton.grid(row = 4, column = 1)

		# Test button.
		self.testButton = Button(frame6, text = "Test", font = ("Helvetica", 13), command = self.test)
		self.testButton.grid(row = 5, column = 0)


	"""Set SELF.FILEPATH and SELF.DESTINATION_PATH to the directory of a file the user selects, i.e. 'load the file'."""
	def load_file(self):
		self.filepath = askopenfilename(title = "Choose a file to compress.",
			filetypes = (("bin files","*.bin"), ("text files","*.txt"), ("doc files","*.docx"), ("jpg files","*.jpg"), ("jpeg files","*.jpeg")))

		if self.filepath == "" or None:
			showinfo("Error", "Please select a valid file.")
			self.filenameLabel['text'] = "You have not selected a file yet."
			return

		showinfo("", "Please select a destination folder to save your compressed or decompressed file to.")
		self.destination_path = askdirectory()

		if self.destination_path == "" or None:
			showinfo("Error", "Please select a valid destination directory.")
			self.filepath == ""
			self.filenameLabel['text'] = "You have not selected a file yet."
			return	

		self.filename = self.filepath.split("/")[-1]
		self.file_ext = os.path.splitext(self.filepath)[1]

		if self.file_ext == ".docx":
			showinfo("Warning", "You have selected a Word document. Please make sure the file does not contain any images.")
			self.updateFilenameLabel()
			return

		self.updateFilenameLabel()
		return


	"""Update self.filenameLabel to display the file name of the selected file, without the direcory
	   (i.e. Users/John/file.txt becomes file.txt)."""
	def updateFilenameLabel(self):
		self.filenameLabel['text'] = self.filename
		return


	"""Create a new instance of HuffmanCoder and compress the file located at self.filepath to self.destination_path."""
	def compress_file(self):
		# Check if the loaded file is a ".bin" file. If True, then it cannot be compressed.
		if self.file_ext == ".bin":
			showinfo("Error", "That file is already compressed. Cannot compress it any further.")
			return

		# Check if the data directory contains a folder with the same name as self.filename,
		# i.e. check if a file with the same name has been compressed previously.
		# File types (.txt, .docx, etc.) matter, i.e. text.txt and text.docx are distinct.
		if containsDirectory(os.getcwd() + "/app/data", self.filename):
			self.data_dir = os.getcwd() + "/app/data/" + self.filename

		else:
			os.makedirs(os.getcwd() + "/app/data/" + self.filename)
			self.data_dir = os.getcwd() + "/app/data/" + self.filename

		if self.filepath == "" or None:
			showinfo("Compression Error", "Please load a file first.")
			return

		huffmanCoder = HuffmanCoder(self.filepath, self.destination_path)

		try:
			compressed_filepath = huffmanCoder.compress()
			showinfo("Success", "Successfully compressed " + self.filename + " to " + compressed_filepath + ". Please do not change the compressed file name.")

			with open(self.data_dir + "/" + self.filename + "-coder.pickle", 'wb') as coder:
				pickle.dump(huffmanCoder, coder, protocol=pickle.HIGHEST_PROTOCOL)

		except:
			showinfo("Error", "Huffman Coding Error.")
			return

		return


	"""Load the existing serialized HuffmanCoder pickle file associated with the binary file at self.filepath.
	   Then, decompress the binary file to self.destination_path."""
	def decompress_file(self):
		# Check if the loaded file isn't a .bin file. If True, then it cannot be decompressed.
		if self.filepath == "":
			showinfo("Please select a file to decompress first.")
			return

		if self.file_ext != ".bin":
			showinfo("Error", "That file is not a .bin file. It cannot be decompressed.")
			return

		# File type to decompress to.
		filetype = self.filepath.split("-")[-1].split(".")[0]

		# Check if the selected binary file was compressed from a .txt or .jpg file.
		# Omit the last 8 characters from the filename string to get the filename without file extension.
		if filetype == "txt" or filetype == "jpg":
			filename = self.filepath.split("/")[-1][0:-8]
			data_dir_name = filename + "." + filetype

			if not containsDirectory(os.getcwd() + "/app/data", data_dir_name):
				showinfo("Decompression Error: Cannot Find Appropriate Huffman Tree. If you changed the file name, please restore it to its original name.")
				return

			with open(os.getcwd() + "/app/data/" + data_dir_name + "/" + data_dir_name + "-coder.pickle", 'rb') as coder:
				huffmanCoder = pickle.load(coder)

		# Check if the selected binary file was compressed from a .docx or .jpeg file.
		# Omit the last 9 characters from the filename string to get the filename without file extension.
		elif filetype == "docx" or filetype == "jpeg":
			filename = self.filepath.split("/")[-1][0:-9]
			data_dir_name = filename + "." + filetype

			if not containsDirectory(os.getcwd() + "/app/data", data_dir_name):
				showinfo("Decompression Error: Cannot Find Appropriate Huffman Tree. If you changed the file name, please restore it to its original name.")
				return

			with open(os.getcwd() + "/app/data/" + data_dir_name + "/" + data_dir_name + "-coder.pickle", 'rb') as coder:
				huffmanCoder = pickle.load(coder)	

		try:
			decompressed_file = huffmanCoder.decompress(compressed_filepath = self.filepath, decompression_path = self.destination_path)
		except:
			showinfo("Error", "HuffmanCoder Decompression Error (201)")
			return

		showinfo("Success", "Successfully decompressed file to " + decompressed_file)
		return


	"""Encrypt the loaded file using AES-256 CFB. Files to be encrypted must be either .txt of .docx files.
	   User-given passwords are not saved or serialized anywhere, and must be remembered by the user.
	   Writes encrypted data to a binary file."""
	def encrypt_file(self):
		if self.filepath == "" or None:
			showinfo("Error", "Please select a file to encrypt first. Files must be .txt or .docx files.")
			return

		if self.file_ext != ".txt" and self.file_ext != ".docx":
			showinfo("Error", "The selected file is not a .txt or .docx file. It cannot be encrypted.")
			return

		password = simpledialog.askstring("Enter a Password", "Please enter a password for your encrypted file. Your password must be 16, 24, or 32 characters long. 32-character passwords are the strongest.")

		if len(password) != 16 and len(password) != 24 and len(password) != 32:
			showinfo("Error", "Wrong password length. Please make sure your password is 16, 24, or 32 characters long.")
			return

		try:
			# Encrypted files will always be named with this format: (original file name w. extention)-encrypted.bin
			encrypted_filename = self.filename + "-encrypted.bin"
			encrypted_filepath = self.destination_path + "/" + encrypted_filename

			file_content = open(self.filepath, 'r').read()

			cipher = AESCipher(password)
			encrypted_content = cipher.encrypt(file_content)

			with open(encrypted_filepath, 'wb') as encrypted_file:
				encrypted_file.write(encrypted_content)
				encrypted_file.close()

			showinfo("Success", "Successfully encrypted " + self.filename + " to encrypted_filepath.")
			return

		except:
			showinfo("Error", "Encryption Error.")
			return


	"""Decrypt the loaded file using AES-256 CFB. Files to be decrypted must be a .bin file.
	   User-given passwords are not saved or serialized anywhere, and must be remembered by the user.
	   Writes decrypted data to a .txt file or .docx file, depending on its original type."""
	def decrypt_file(self):
		if self.filepath == "" or None:
			showinfo("Error", "Please select a file to encrypt first. Files must be .txt or .docx files.")
			return

		if self.file_ext != ".bin":
			showinfo("Error", "The selected file is not a .txt or .docx file. It cannot be encrypted.")
			return

		password = simpledialog.askstring("Enter Your Password", "Please enter the password you used to encrypt this file.")

		if len(password) != 16 and len(password) != 24 and len(password) != 32:
			showinfo("Error", "Wrong password length. Please make sure your password is 16, 24, or 32 characters long.")
			return

		# Extract the encrypted file's extension from the given filepath, e.g.:
		# extract txt from /Users/John/paragraph.txt-encrypted.bin.
		# Encrypted files will always be named with this format: (original file name w. extention)-encrypted.bin
		file_ext = self.filepath.split("/")[-1][:-14].split(".")[1]

		# Decrypted filepath format: (original file name w. extention)_(decrypted).(original file extention)
		decrypted_filepath = self.destination_path + "/" + self.filename.split(".")[0] + "_(decrypted)." + file_ext

		try:
			encrypted_content = open(self.filepath, 'rb').read()
			cipher = AESCipher(password)
			decrypted_content = cipher.decrypt(encrypted_content)
		except:
			showinfo("Error", "Cannot decrypt that file with the given password. Please recheck your password.")
			return

		if file_ext == "txt":
			with open(decrypted_filepath, 'w+') as file:
				file.write(decrypted_content)
				file.close()

			showinfo("Success", "Successfully decrypted selected file to " + decrypted_filepath)
			return

		elif file_ext == "docx":
			document = Document()
			document.add_paragraph(decrypted_content)
			document.save(decrypted_filepath)

		else:
			showinfo("Error", "Cannot decrypt that file. Please make sure you did not change the encrypted file's name, or that the selected file is actually encrypted.")
			return

		return


	"""Test function for printing misc. things, such as FileCase attributes."""
	def test(self):
		# print(self.filepath)
		# print(self.file_ext)
		# print(self.filename)
		return

