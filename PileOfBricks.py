'''
https://www.codeeval.com/open_challenges/117/
'''
import math
import re
import sys
class hole():
	def __init__(self,point_1,point_2):
		self.dims = sorted([x for x in getSize(point_1,point_2)])
		self.passed = []
	
	def isPassable(self,brick):
		brickDims = brick.getDims()
		if( ( brickDims[0] <= self.dims[0] ) and ( brickDims[1] <= self.dims[1] ) ):
			self.passed.append(brick.index)
			return True
		else:
			return False
	def getPassed(self):
		if(len(self.passed) == 0):
			print("-")
		else:
			passStr = ""
			for x in sorted(self.passed):
				passStr += str(x)+","
			print(passStr[:-1])
class brick():
	def __init__(self,index,point_1,point_2):
		self.index = index
		self.dims = sorted([x for x in getSize(point_1,point_2)])
	def getDims(self):
		return self.dims
	
def getSize(point_1,point_2):
		if( len(point_1) == len(point_2) ):
			return [math.fabs(point_1[x]-point_2[x]) for x in range(len(point_1))]
		else:
			print("Values are not same dimension")
			raise IndexError	

if __name__ =='__main__':
# 	print(hole([4,3],[3,-3]).isPassable(getSize([10,9,4],[9,4,2])))
	regexMain = r"(?P<hole>\[\-?\d+\,\-?\d+\] \[\-?\d+\,\-?\d+\])\|(?P<bricks>(\(\d+ \[\-?\d+\,\-?\d+\,\-?\d+\] \[\-?\d+\,\-?\d+\,\-?\d+\]\);?)*)"
	regexHole = r"(\[(?P<a>\-?\d+)\,(?P<b>\-?\d+)\] \[(?P<c>\-?\d+)\,(?P<d>\-?\d+)\])"
	regexBrick = r"\((?P<index>\d+) \[(?P<a>\-?\d+)\,(?P<b>\-?\d+)\,(?P<c>\-?\d+)\] \[(?P<d>\-?\d+)\,(?P<e>\-?\d+)\,(?P<f>\-?\d+)\]\)"
	for line in open(sys.argv[1]):
		if(line == "\n"):
			pass
		else:
			m = re.match(regexMain, line)
			holeStr = m.group("hole")
			bricksStr = m.group("bricks")
			m = re.match(regexHole, holeStr)
			holePoint_1 = [int(m.group("a")),int(m.group("b"))]
			holePoint_2 = [int(m.group("c")),int(m.group("d"))]
			bricks = []
			for brickStr in bricksStr.split(";"):
				m = re.match(regexBrick, brickStr)
				brickPoint_1 = [int(m.group("a")),int(m.group("b")), int(m.group("c"))]
				brickPoint_2 = [int(m.group("d")),int(m.group("e")), int(m.group("f"))]
				brickIndex = int(m.group("index"))
				bricks.append(brick(brickIndex,brickPoint_1,brickPoint_2))
			myHole = hole(holePoint_1,holePoint_2)
			for myBrick in bricks:
				myHole.isPassable(myBrick)
			myHole.getPassed()
		
		
	
	
	
	
	
	