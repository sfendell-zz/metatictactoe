from random import randint
players = ['X','O']
numPlayers = len(players)
def nextPlayer(player):
	return players[players.index(player)+1 % numPlayers]

class Board(object):
	"""represents a n-dimensional board object"""

	def __init__(self, dimension, size, parent=None, pos=None):
		self.dimension = dimension
		self.size = size
		self.state = -1 #indicates an unwon square
		self.parent = parent
		self.pos = pos
		if dimension>0: #recursively generate child boards
			self.children = [[Board(dimension-1,size,self,(row,col)) for col in range(size)] for row in range(size)]

	"""Takes in player (one letter from the player array) and 2*dimension arguments representing a 0-d square on the board, places the 
	correct marking there, then updates all the children's states correctly and checks if that move wins the game"""
	def move(self, player, turn):
		if len(turn)!=self.dimension: #turn is a tuple of tuples, each of which specifies coordinates in a board
			raise Exception('move has wrong number of indices: should be %s, is %s' % (self.dimension, len(turn))) #should never be thrown
		if self.state != -1:
			raise Exception('square of dimension %s has already been won!' % self.dimension)
		print '%s is the dimension this is getting to\n' % self.dimension
		if self.dimension==0:
			self.state=player
			return self.parent.checkwin(player,self.pos)
		else:
			return self.children[turn[0][0]][turn[0][1]].move(player,*turn[1:])

	"""After player wins the pos box of the board, check if the board has been won, set state appropriately, and alert its parent.
		Return the max dimension won by the play (minimum 1, maximum [dimension])"""
	def checkwin(self,player,pos):
		children = self.children
		parent = self.parent
		size = self.size
		if (self.dimension == 0 or
		[children[pos[0]][i].state for i in range(size)].count(player)==size or #winning in a column
		[children[i][pos[1]].state for i in range(size)].count(player)==size or #winning in a row
		(pos[0] == pos[1] and [children[i][i].state for i in range(size)].count(player)==size) or #winning in diagonal (topleft to bottomright)
		(pos[0] + pos[1] ==size-1 and [children[i][size-1-i].state for i in range(size)].count(player)==size)): #winning in cross diagonal
			self.state = player
			return 1+((parent != None) and parent.checkwin(player,self.pos))
		else: #no win indicates that this is the end of the line for the chain of wins
			return 0

	"""Produces a rule based on the last turn played that the next turn must match"""
	def genrule(self, level, turn):
		if len(turn)!=self.dimension:
			raise Exception('move has wrong number of indices: should be %s, is %s' % (self.dimension, len(turn))) #should never be thrown
		return turn[:-level-1] + turn[-level:] + ('x','x')
	
	"""Match a turn to a rule produced by genrule"""
	def matchrule(self, rule, turn):
		if turn==():
			if rule==():
				return True
			else:
				raise Exception('Turn is empty but rule is not!')
		nextboard = self.children[turn[0][0]][turn[0][1]]
		if turn[0]==rule[0] or nextboard.state!=-1:
			nextboard.matchrule(rule[1:], turn[1:])
    
    """Produces a random turn for this board. Only for debugging"""
    def __randturn(self):
        a = ((),)
        for i in range(self.dimension):
            a = a + (randint(0,self.size),randint(0,self.size))
        return a
"""
class Turn(object):
	Object representing a turn; basically just a tuple with n 
	nested tuples of size 2, each entry between 0 and [size]
	def __init__(size,dim):
		self.size=size
		self.turntuple = ((),)*dim
	
	def set(level, pos):
		if len(pos)!=size:
			raise Exception('turn
		self.turntuple[level] = pos

	def get(level):
		return self.turntuple[level]
"""
def startmessage():
	print 'Welcome to funtimes metatictactoe'
	print 'Size?:'

def 
			
if __name__ == "__main__":
	(dim,size) = startmessage()
	
	playgame(Board(dim, size))

def playgame(board, lastplayer='O',lastturn=None)
	print 'Where would you like to go, player %s?:' % 
