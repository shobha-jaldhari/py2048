import random
import copy
import os
import msvcrt
import time

boardSize= int(input("enter the value of n")) #for given value of n it will give a board of n*n

x = int(input("enter the win value"))
board = []
for i in range(boardSize):
	row = []
	for j in range(boardSize):
		row.append(0)
	board.append(row)



def display():
	largest=board[0][0]
	for row in board:
		for element in row:
			if element > largest:
				largest = element

	numSpaces = len(str(largest))

	for row in board:
		currRow = "|"
		for element in row:
			if element == 0:
				currRow += " " * numSpaces + "|"
			else:
				currRow += (" " * (numSpaces -len(str(element)))) + str(element) + "|"

		print(currRow)

	print()





def mergeOneRowL(row):
	for j in range(boardSize-1):
		for i in range(boardSize-1,0,-1):
			if row[i-1] == 0:
				row[i-1] = row[i]
				row[i] = 0

	for i in range(boardSize-1):
		if row[i] == row[i+1]:
			row[i] *= 2
			row[i+1] = 0



	for i in range(boardSize-1,0,-1):
		if row[i-1] == 0:
			row[i-1] = row[i]
			row[i] = 0

	return row


def merge_left(currentBoard):
	for i in range(boardSize):
		currentBoard[i] = mergeOneRowL(currentBoard[i])
	
	return currentBoard


def reverse(row):
	new =[]
	for i in range(boardSize-1, -1, -1):
		new.append(row[i])
	return new

def merge_right(currentBoard):
	for i in range (boardSize):

		currentBoard[i] = reverse(currentBoard[i])
		currentBoard[i] = mergeOneRowL(currentBoard[i])
		currentBoard[i] = reverse(currentBoard[i])
	
	return currentBoard


def transpose(currentBoard):
	for j in range(boardSize):
		for i in range (j,boardSize):
			if not i == j:
				temp = currentBoard[j][i]
				currentBoard[j][i] = currentBoard[i][j]
				currentBoard[i][j] = temp
	return currentBoard


def merge_up(currentBoard):
	currentBoard = transpose(currentBoard)
	currentBoard = merge_left(currentBoard)
	currentBoard = transpose(currentBoard)
	
	return currentBoard

def merge_down(currentBoard):
	currentBoard = transpose(currentBoard)
	currentBoard = merge_right(currentBoard)
	currentBoard =  transpose(currentBoard)
	
	return currentBoard


def pickNewValue():
	return 2

def won():
	for row in board:
		if x in row:
			return True
	return False

def noMoves():
	tempBoard1 = copy.deepcopy(board)
	tempBoard2 = copy.deepcopy(board)

	tempBoard1 = merge_down(tempBoard1)
	if tempBoard1 == tempBoard2:
		tempBoard1 = merge_up(tempBoard1)
		if tempBoard1 == tempBoard2:
			tempBoard1 = merge_left(tempBoard1)
			if tempBoard1 == tempBoard2:
				tempBoard1 = merge_right(tempBoard1)
				if tempBoard1 == tempBoard2:
					return True
	return False



def addNewValue():
	rowNum = random.randint(0,boardSize-1)
	colNum = random.randint(0,boardSize-1)

	while not board[rowNum][colNum] == 0:
		rowNum = random.randint(0,boardSize-1)
		colNum = random.randint(0,boardSize-1)
	board[rowNum][colNum] = pickNewValue()


numNeeded = 1
while numNeeded > 0:
	rowNum = random.randint(0,boardSize-1)
	colNum = random.randint(0,boardSize-1)

	if board[rowNum][colNum] == 0:
		board[rowNum][colNum] = pickNewValue()
		numNeeded -= 1

print("welcome to game....this is your gameboard")


display()

print("start entering the keys")


gameOver = False
while not gameOver:
	if msvcrt.kbhit():
		move = msvcrt.getch()
		validinput = True

		tempBoard = copy.deepcopy(board)

		if move == b"d":
			os.system('cls')
			board = merge_right(board)

		elif  move == b"w" :
			os.system('cls')
			board = merge_up(board)

		elif move == b"a":
			os.system('cls')
			board = merge_left(board)

		elif move == b"s" :
			os.system('cls')
			board = merge_down(board)

		else:
			validinput = False

		if not validinput:
			print("please enter valid key")



			
		else:
			if boardSize == 1 and x==2:
				display()
				print("you won")
				time.sleep(1)
				gameOver = True
			elif boardSize ==1 and x!=2:
				display()
				print("you lose")
				time.sleep(1)
				gameOver= True





			elif board == tempBoard:
				display()
				print("invalid move")

			else:

				if won():
							
					display()
					print("you won")
					time.sleep(1)
					gameOver = True

				else:
					addNewValue()
							
					display()

					if noMoves():
						print("no more moves available...Game Over")
						time.sleep(1)
						gameOver = True


				

						
							


				