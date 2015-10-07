import sys

def getRotations(string):
	rotations = []	
	for x in range(len(string)):
		rotations.append( string[x:]  + string[0:x])
	return rotations

if __name__ == "__main__":
	for line in open(sys.argv[1]):
		line = line.strip("\n")
		word,test = line.split(",")
		
	
		if test in getRotations(word):
			print("True")
		else:
			print("False")