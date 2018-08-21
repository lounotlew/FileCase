from AESCipher import AESCipher

content = open('paragraph.txt', 'r').read()

# cipher1 = AESCipher('mysecretpassword')
# encrypted = cipher1.encrypt(string)
# cipher2 = AESCipher('mysecretpassword')
# decrypted = cipher2.decrypt(encrypted)
# print(encrypted)
# print(decrypted)

cipher1 = AESCipher('mysecretpassword')
cipher2 = AESCipher('mysecretpassword')
encrypted = cipher1.encrypt(content)
# decrypted = cipher2.decrypt(encrypted)

with open('paragraph-compressed-encrypted.bin', 'wb') as file:
	file.write(encrypted)
	file.close()