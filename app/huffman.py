####################################################################
# Implementation of the Huffman Coding Algorithm.                  #
# Parts of this implementation were borrowed from other sources.   #
# See specific comments for who authored what.                     #
#                                                                  #
# Written by Lewis Kim.                                            #
####################################################################

from itertools import groupby
from heapq import *
import os
from bitstring import BitArray, BitStream
from bitarray import bitarray

from docx import Document
import io


# Node class that makes up a binary tree. Used to constuct a Huffman Tree.
class Node:
	left = None
	right = None
	item = None
	value = 0

	def __init__(self, item, value):
		self.item = item
		self.value = value

	def set_children(self, left_node, right_node):
		self.left = left_node
		self.right = right_node

	def __lt__(self, other):
		return self.value < other.value


# Huffman Coder that encodes file content, and compresses/decompresses it.
class HuffmanCoder:

	"""Create a new instance of HuffmanCoder with a FILEPATH of a text file.

	   class variables:
	   - self.filepath: Filepath of the file to be encoded/compress.
	   - self.bit_length: Length of the encoded file content (i.e. length of bit string).
	   - self.char_to_code: Dictionary of the Huffman Codes. Keys are characters appearing
	     in the file, and the values are the codes associated with those characters.
	   - self.code_to_char: key:value reversal of self.char_to_code.
	   - self.content: Text content of the selected file.
	   - self.freq_tree: Dictionary whose keys are characters of the content of the file.
	     and values the frequencies of those characters."""
	def __init__(self, filepath):
		self.filepath = filepath
		self.file_ext = os.path.splitext(filepath)[1]
		self.bit_length = 0

		self.char_to_code = {}
		self.code_to_char = {}

		self.content = ""

		if self.file_ext == ".txt":
			with open(self.filepath, 'r+') as file:
				self.content = file.read()

		elif self.file_ext == ".docx":
			document = Document(filepath)

			for para in document.paragraphs:
				self.content += para.text

		elif self.file_ext == ".jpg" or self.file_ext == ".jpeg":
			return

		else:
			raise ValueError("Wrong File Type for Huffman Coding.")
			return


		self.freq_tree = self.build_freq_tree(self.content)


	"""Build a character frequency dictionary, whose keys are the characters of the string
	   CONTENT, and values are the frequency of those characters in CONTENT."""
	def build_freq_tree(self, content):
		freq = {}
		#
		for char in content:
			if not char in freq:
				freq[char] = 0

			freq[char] += 1

		return freq


	"""Encode the contents of self.filepath (i.e. self.content) using the Huffman Coding Algorithm.
	   This function constructs a Huffman Tree, and returns a dictionary whose keys are characters
	   in self.content, and values are the bit code associated with that character.

	   Help From: https://www.techrepublic.com/article/huffman-coding-in-python/"""
	def encode(self):
		codes = {}

		def codeIt(s, node):
			if node.item:
				if not s:
					codes[node.item] = "0"
				else:
					codes[node.item] = s
			else:
				codeIt(s+"0", node.left)
				codeIt(s+"1", node.right)

		queue = [Node(a, len(list(b))) for a, b in groupby(sorted(self.content))]
		heapify(queue)

		while len(queue) > 1:
			left = heappop(queue)
			right = heappop(queue)

			node = Node(None, right.value + left.value)
			node.set_children(left, right)
			heappush(queue, node)

		codeIt("", queue[0])

		return codes


	"""."""
	def compress(self):
		self.char_to_code = self.encode()
		self.code_to_char = {value:key for key, value in self.char_to_code.items()}

		compressed_filepath = os.path.splitext(self.filepath)[0] + ".bin"

		encoded_content = "".join([self.char_to_code[a] for a in self.content])

		self.bit_length = len(encoded_content)

		bit_array = BitArray(bin = encoded_content)

		with open(compressed_filepath, 'wb') as compressed_file:
			compressed_file.write(bit_array.tobytes())
			compressed_file.close()


	"""."""
	def decompress(self):
		decompressed_filepath = os.path.splitext(self.filepath)[0] + "-decompressed" + ".txt"

		bits = BitArray(filename = os.path.splitext(self.filepath)[0] + ".bin")

		encoded_content = bits.bin[0:self.bit_length]
		decoder = {k:bitarray(v) for k, v in self.char_to_code.items()}

		decoded_chars = bitarray(encoded_content).decode(decoder)
		decoded_content = ''.join(x for x in decoded_chars)

		with open(decompressed_filepath, 'w+') as decompressed_file:
			decompressed_file.write(decoded_content)
			decompressed_file.close()


	"""Print all ATTRS of this instance of HuffmanEncoder. Used for testing purposes to see
	   if attrs point properly to the correct data."""
	def print_attrs(self):
		print("Filepath: " + self.filepath)
		print("File Extension: " + self.file_ext)
		print("Content: " + self.content)
		print(self.freq_tree)

