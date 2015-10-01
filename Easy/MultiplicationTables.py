def multiplicationTable(num):
	table = [[x*y for x in range(1,num+1)] for y in range(1,num+1)]
	for row in table:
		print("    ".join(str(row)).strip())


if __name__ == "__main__":
	multiplicationTable(12)