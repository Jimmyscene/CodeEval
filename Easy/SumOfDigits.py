import sys
def sumDigits(x):
	sum=0
	for char in x:
		sum += int(char)
	return sum
if __name__=="__main__":
	for line in open(sys.argv[1]):
		print(sumDigits(line.strip()))