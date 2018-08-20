#####
# Misc. utility helper functions used in gui.py or huffman.py.
#
# Written by Lewis Kim.
#

import glob
import os

"""."""
def containsDirectory(dir1, dir2):
	if dir2 in [name for name in os.listdir(dir1)]:
		return True

	return False