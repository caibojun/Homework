class Maze(object):
	"""
    Attributes:
        shape: A string contains maze's size.
        connectionship: A string contains connection relationship along roads.
        wall: A string represent for 'Wall'.
        road: A string represent for 'Road'.
        cp: A list contains connection pairs of maze.
    """

	def __init__(self):
		super(Maze, self).__init__()
		self.shape = raw_input("Input Your Maze's Shape :")
		self.connectionship = raw_input("Input Connectionship :")
		self.wall = '[W]'
		self.road = '[R]'
		self.cp = []
		try:
			connect_pair = self.connectionship.split(';')
			for pair in connect_pair:
				pairset=pair.split(' ')
				self.cp.append([[int(pairset[0].split(',')[0]),int(pairset[0].split(',')[1])],\
					[int(pairset[1].split(',')[0]),int(pairset[1].split(',')[1])]])
		except(ValueError,IndexError,AttributeError):
			print "Incorrect command format ."
			return self.__del__()
		return self.Error_detect()
		

	def __del__(self):
		return

	def Error_detect(self):
		try:
			r, c = self.shape.split(' ')
			self.row = int(r); self.column = int(c)
		except ValueError:
			print "Invalid number format ."
			return self.__del__()
		if (self.row*self.column<=0)&(self.row+self.column>=0):
			print "Number out of range"
			return self.__del__()		
		return self.generate_maze()

	def generate_maze(self):
		mask = []
		for i in xrange(2*self.row+1):
			if i%2==0:
				mask.append([0]*(2*self.column+1))
			else:
				mask.append([0,1]*self.column+[0])
		for j in self.cp:
			x = 2*min(j[0][0],j[1][0])+1; y = 2*min(j[0][1],j[1][1])+1
			delta = [abs(j[0][0]-j[1][0]),abs(j[0][1]-j[1][1])]
			if sum(delta)>1:
				print "Maze format error."
				return self.__del__()
			x += delta[0]; y += delta[1]
			if (x>2*self.row-1) or (y>2*self.column-1):
				print "Number out of range"
				return self.__del__()
			else:
				mask[x][y] = 1
		self.maze = ''
		for n in xrange(len(mask)):
			row_element = ''
			for m in xrange(len(mask[0])):
				if mask[n][m] == 0:
					row_element += self.wall
				else:
					row_element += self.road
			row_element += '\n'
			self.maze += row_element
		return

if __name__ == '__main__':
	sample = Maze()
	try:
		print sample.maze
	except AttributeError:
		pass

		