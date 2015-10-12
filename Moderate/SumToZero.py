import sys
from itertools import combinations


if __name__ == "__main__":
	for line in open(sys.argv[1]):
		xs = []
		count =0
		[xs.append(int(x)) for x in line.split(",")]
		for x in combinations(xs,4):
			if(sum(x) == 0):
				count +=1
		print(count)
