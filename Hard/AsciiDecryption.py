import sys
def getWord(length, msg, letter):
	dups = []
	for x in range(len(msg) - length):
		for y in range(x+1,len(msg) - length):
			if( msg[x:x+length] == msg[y:y+length]):
				dups.append(msg[x:x+length])
	for word in dups:
		x = word[-1] - ord(letter) 
		decrypted = "".join([ chr(letter-x) for letter in msg ])
		try:
			if(" " in decrypted):
				print(decrypted)
		except UnicodeEncodeError:
			pass
		
				
if __name__ == '__main__':
	for line in open(sys.argv[1]):
		length,letter, msg = [ x.strip() for x in line.split("|")]
		length = int(length)
		msg = [ int(num) for num in msg.split()]
		getWord(length,msg, letter)
		