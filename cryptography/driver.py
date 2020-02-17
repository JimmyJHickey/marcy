###
# Driver Class
# Jimmy Hickey
# 2019-07-14
###

import polyalphabetic

def main():
	key = "hello"
	plain_text = "Once upon a midnight dreary"

	cipher_text = polyalphabetic.encipher(key, plain_text)
	print(cipher_text)

	new_plain_text = polyalphabetic.decipher(key, cipher_text)
	print(new_plain_text) 

if __name__ == "__main__":
	main()
