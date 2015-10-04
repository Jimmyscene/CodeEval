import os
import sys
def getFileSize(path):
	print(os.path.getsize(path))

if __name__ == "__main__":
		getFileSize(sys.argv[1])