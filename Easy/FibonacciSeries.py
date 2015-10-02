import sys

def getFib(num):
	if(num == 0):
		return 0
	if(num == 1):
		return 1
	else:
		return getFib(num-1)+getFib(num-2)

if __name__ == "__main__":
	for line in open(sys.argv[1]):
		print(getFib(int(line.strip())))
		