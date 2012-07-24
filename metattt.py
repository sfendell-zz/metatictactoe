
players = ['X','O']
numPlayers = len(players)
def nextPlayer(player):
	return players[players.index(player)+1 % numPlayers]

class Board(object):
	"""represents a n-dimensional board object"""
	
	def __init__(self, dimension, size, parent=None, pos=None):
		self.dimension = dimension
		self.size = size
		self.state = -1
		self.parent = parent
		self.pos = pos
		if dimension>0:
			self.children = [[Board(dimension-1,size,self,(row,col)) for col in range(size)] for row in range(size)]
			
	"""Takes in player (one letter from the player array) and 2*dimension arguments representing a 0-d square on the board, places the 
	correct marking there, then updates all the children's states correctly and checks if that move wins the game"""
	def move(self, player, *args):
		if len(args)!=self.dimension:
			raise Exception('move has wrong number of indices: should be %s, is %s' % (self.dimension, len(args))) #should never be thrown
		if self.state != -1:
			raise Exception('square of dimension %s has already been won!' % self.dimension)
		if self.dimension==0:
			self.state=player
			self.parent.checkwin(player,self.row,self.col)
		else:
			self.children[args[0][0]][args[0][1]].move(player,*args[1:])
			
	"""After player wins the (row, col) box of the board, check if the board has been won, set state appropriately, and alert its parent"""
	def checkwin(self,player,coord):
		row = coord[0]
		col = coord[1]
		children = self.children
		parent = self.parent
		size = self.size
		won = True
		if ([children[row][i].state for i in range(size)].count(player)==size or
		[children[i][col].state for i in range(size)].count(player)==size or
		(row == col and [children[i][i].state for i in range(size)].count(player)==size) or
		(row+col==size-1 and [children[i][size-1-i].state for i in range(size)].count(player)==size)):
			self.state = player
			if parent is None:
				return player
			parent.checkwin(player,self.row,self.col)

	def genrule(self, *args)
		if len(args)!=self.dimension:
			raise Exception('move has wrong number of indices: should be %s, is %s' % (self.dimension, len(args))) #should never be thrown
		if self.children(

			

def startmessage():
	print 'Welcome to funtimes metatictactoe'
	print 'Size?:'
	
			
if __name__ == "__main__":
	(dim,size) = startmessage()
	
	playgame(Board(dim, size))

def playgame(board, lastplayer='O',lastturn=None)
