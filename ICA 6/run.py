from gameMechanics import Game

playing = True
game = Game()

def startScreen():
	global playing
	global game
	
	game.printDescription()	
	con = raw_input("")
	if con == "q":
		playing = False
	if playing == True:
		game.updateDisplay()
		
def userInput():
	global playing
	global game
	
	print("")
	prompt = raw_input()
	if prompt == "q":
		playing = False
	else:
		game.userAction(prompt)

def win():
	global playing
	global game
	
	if game.checkIfWin() == True:
		game.printWinnerMessage()
		print("")
		prompt = raw_input("You won! Play again(y/n)? ")
		if prompt == "y":
			game.playAgain()
			prompt = raw_input()
			if prompt == "q":
				playing = False
		else:
			playing = False

def lose():
	global playing
	global game
	
	if game.checkIfLose() == True:
		game.printLoserMessage()
		print("")
		game.printCurrentState()
		print("")
		if game.chickenAte == True:
			print("> The chicken ate the grain.")
		if game.foxAte == True:
			print("> The fox ate the chicken.")	
		print ("")
		prompt = raw_input("Play again(y/n)? ")
		if prompt == "y":
			game.playAgain()
			prompt = raw_input()
			if prompt == "q":
				playing = False
		else:
			playing = False

def update():
	global game
	game.updateDisplay()
	
		
def gameLoop():
	global playing
	global game
	
	while playing:
		userInput()		
		win()
		lose()
		if playing == False:
			break
		else:
			update()
		
def main():
	startScreen()
	gameLoop()

if __name__ == "__main__": main()
