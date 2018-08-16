from huffman import HuffmanCoder

path = "paragraph.txt"

h = HuffmanCoder(path)

h.compress()
h.decompress()