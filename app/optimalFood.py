from math import sqrt
def getFood(moves, occupied, foods, head):
	""" Decides best food based on distance + available space

	Parameters:
	moves (dict): POSSIBLE moves e.g {left: [3,5], up: [4,6]}
	foods (list): xy locations of food pieces e.g [3,5]
	head (list): xy location of head e.g [3,5]

	Returns:
	str: best move

	"""
	minimum = 100000 # smallest distance from head to food
	bestFood = [1000,1000] # arbitrary for initialization
	foodDict = {bestFood: 0} # dictionary of food coord + score e.g {[3,7]: 2, [4,5]: 5}
	
	# Find the best food and give it a score of 1
	for food in foods:
		foodDict.update({food: 0}) # add food to list
		xDist = abs(head[0] - food[0]) # x distance between head and food
		yDist = abs(head[1]- food[1]) # y distance between head and food
		hyp = xDist + yDist #distance between head and food
		if (hyp < minimum):
			foodDict.update({bestFood: 0}) # change the previous best food back to 0
			minimum = hyp 
			bestFood = food # current best food
			foodDict.update({bestFood: 1}) # new best food = 1


	# # Score each move
	# foodMax = 0 # highest food score
	# for food, score in foodDict.items():
	# 	newScore = score += check(food, )



	mini = 100000 # smallest distance from move to food
	bestMove ='up' # arbitrary for initialization
	for move, coord in moves.items(): # e.g move: 'left' and coord: [3,5]
		xDist = abs(coord[0] - bestFood[0]) # x distance between move and food
		yDist = abs(coord[1]- bestFood[1]) # y distance between move and food
		hyp = xDist + yDist #distance between move and food

		# print('move: {}, coord: {}, xDist:{}, yDist:{}, hypotenuse:{}, food:{}'.format(move, coord, xDist, yDist, hyp, food))
		if (hyp < mini):
			mini = hyp
			bestMove = move
		# print('best move is {}'.format(bestMove))

	return bestMove

def check(food, occupied, width, height):
	"""
	_Purpose:
	takes a move coord and returns a score (max 4) based on how many free spaces are directly around the move

	_Parameters:
	move (list): xy coord of the move
	occupied (list): xy coords all occupied spaces on board 
	width (int): width of board
	height (int): height of board

	_Returns:
	score (int): score of move
	"""
	score = 0
	if not (([food[0]-1,food[1]] in occupied) or (food[0]-1 < 0)): #left
		score += 1
	if not (([food[0]+1,move[1]] in occupied) or (food[0]+1 > width-1)): # right
		score += 1
	if not (([food[0],move[1]-1] in occupied) or (food[1]-1 < 0)): # up
		score += 1
	if not (([food[0],food[1]+1] in occupied) or (food[1]+1 > height-1)): #down
		score += 1
	return score