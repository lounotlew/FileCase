import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import simpledialog
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showerror
from tkinter.messagebox import showinfo





#?
import pickle

# class Compressor:







# Run the application.
root = Tk()
root.title("FileCase: Lossless File Compression and Encyption")
app = Compressor(root)

while True:
	try:
		root.mainloop()
		break
	except UnicodeDecodeError: # Added to avoid the program crashing when scrolling.
		pass