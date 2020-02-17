###
# Polyalphabetic Cipher
# Jimmy Hickey
# 2019-07-14
###

def encipher(key, plain_text):
	key_length = len(key)
	count = 0
	cipher_text = ''

	for letter in plain_text:
		cipher_text += chr(ord(letter) + ord(key[count % key_length]))
		count += 1

	return cipher_text

def decipher(key, cipher_text):
	key_length = len(key)
	count = 0
	plain_text = ''

	for letter in cipher_text:
		plain_text += chr(ord(letter) - ord(key[count % key_length]))
		count += 1

	return plain_text
