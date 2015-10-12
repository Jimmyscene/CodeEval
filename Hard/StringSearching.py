import sys
import re


def isSubstring(string,test):
	test = test.strip("\n")
	for index in reversed(range(len(test) - 1)):
		if( test[index] == "*"):
			if( test[index-1] == "\\"):
				continue
			else:
				test = test[:index] + "." +test[index:]
				continue
	m = re.search('.*' + test + '.*', string)
	if(m == None):
		print("false")
	else:
		print("true")
		

if __name__ == '__main__':
	for line in open(sys.argv[1]):
		if(line != "\n"):
			isSubstring(*line.split(","))