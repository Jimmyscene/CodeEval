import math
import sys

def lcm(x,y):
	return (y*math.ceil(x/y))

if __name__ == "__main__":
	for line in open(sys.argv[1]):
		x,y = [int(var) for var in line.split(",")]
		print(lcm(x,y))