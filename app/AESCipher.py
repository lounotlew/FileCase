#####################################################################
# AES Cipher class for encrypting file content.                     #
#                                                                   #
# Written by github user @gustavohenrique, with edits written by    #
# Lewis Kim to integrate to FileCase.                               #
#####################################################################

from hashlib import md5
from base64 import b64decode
from base64 import b64encode
from Crypto import Random
from Crypto.Cipher import AES
import os

BLOCK_SIZE = 16  # Bytes
pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * \
                chr(BLOCK_SIZE - len(s) % BLOCK_SIZE)
unpad = lambda s: s[:-ord(s[len(s) - 1:])]


#
class AESCipher:

    """."""
    def __init__(self, key):
        self.key = md5(key.encode('utf8')).hexdigest()

    """."""
    def encrypt(self, raw):
        raw = pad(raw)
        bs = AES.block_size
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CFB, iv)

        return b64encode(iv + cipher.encrypt(raw))

    """."""
    def decrypt(self, enc):
        enc = b64decode(enc)
        iv = enc[:16]
        cipher = AES.new(self.key, AES.MODE_CFB, iv)
        return unpad(cipher.decrypt(enc[16:])).decode('utf8')

