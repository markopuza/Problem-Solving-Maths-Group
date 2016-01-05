import re

filename = raw_input("Enter the name of the file to encrypt: ")
mode = int(raw_input("Enter 0 if decrypting 1 if encrypting: "))
encrypted = ""
word = "aibohphobia"

if (mode):
	with open(filename, "rb") as content:
		for line in content.read():
			for i in range(len(line)):
				encrypted += chr(ord(line[i]) + ord(word[i % len(word)]))
		with open(filename + "Encrypted", "wb") as newfile:
			newfile.write(encrypted)
else:
	with open(filename, "rb") as content:
		for line in content.read():
			for i in range(len(line)):
				encrypted += chr(ord(line[i]) - ord(word[i % len(word)]))
		filenameNew = re.sub("Encrypted", "Decrypted", filename) if re.match("\w*Encrypted", filename) else filename + "Decrypted"
		with open(filenameNew, "wb") as newfile:
			newfile.write(encrypted)
