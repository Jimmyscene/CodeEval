import sys
if __name__ == "__main__":
	sum=0
	for line in open(sys.argv[1]):
		sum+=int(line.strip())
	print(sum)