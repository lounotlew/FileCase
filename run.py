import tkinter as tk
from tkinter import *

from app.gui import FileCase

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