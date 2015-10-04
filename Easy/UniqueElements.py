import sys

def uniqueElements(line):
	myList = []
	line = line.strip()
	for x in line.split(","):
		if( x not in myList):
			myList.append(x)
	return(",".join(myList))

if __name__ == "__main__":
	for line in open(sys.argv[1]):
		print(uniqueElements(line))