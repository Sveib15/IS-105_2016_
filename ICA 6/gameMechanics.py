from river import River
import os
import platform

class Game:
	river = River()
	chickenAte = False
	foxAte = False
	
	def userAction(self, userInput):
		validItems = ["man", "chicken", "grain", "fox"]
		validActions = ["l","u"]
		
		if userInput != "":
			action = userInput[0]
			item = userInput[1:len(userInput)]
			
			if userInput == "help":
				self.showHelp()			
			elif userInput == "c":
				self.river.cross()
			else:
				if action in validActions:							
					if item in validItems:				
						if action == "l":
							self.river.load(item)
						elif action == "u":
							self.river.unload(item)
					else:
						self.invalidItem(item)
				else:
					self.invalidAction(action)
						
	def invalidAction(self, action):
		print("")
		print("Can not find command: <" + action + ">")
		print("Type help to see the controls or press ENTER to continue")
		con = raw_input()
		if con == "help":
			self.showHelp()
			
	def invalidItem(self, item):
		print("")
		print("Can not find item: <" + item + ">")
		print("Press ENTER to continue")
		con = raw_input()

	def clearDisplay(self):
		os.system('cls' if os.name == 'nt' else 'clear')
	
	def printCurrentState(self):
		print(self.river.updatePicture())
		
	def updateDisplay(self):
		self.clearDisplay()
		self.printCurrentState()
		
	def checkIfLose(self):
		lists = [self.river.leftSide, self.river.rightSide, self.river.boat]
		lost = False
		
		for l in lists:
			if "man" not in l:
				if "chicken" in l and "grain" in l:
					self.chickenAte = True
					lost = True
				if "chicken" in l and "fox" in l:
					self.foxAte = True
					lost = True
		return lost

	def checkIfWin(self):
		if "man" in self.river.rightSide and "chicken" in self.river.rightSide and "fox" in  self.river.rightSide and "grain" in self.river.rightSide:
			return True
			
	def printDescription(self):
		print(" ____________________________RIVER___________________________")
		print("|                                                            |")
		print("| > Get all items to the other side of the river.            |")
		print("| > The chicken will eat the grain if the man is not present.|")
		print("| > The fox will eat the chicken if the man is not present.  |")
		print("| > There is only room for two in the boat.                  |")
		print("| > The man must be in the boat in order to cross the river. |")
		print("|                                                            |")
		print("| -CONTROLS-                                                 |")
		print("|                                                            |")
		print("| > Load item:    l+item    example: lchicken                |")
		print("| > Unload item:  u+item    example: ufox                    |")
		print("| > Cross river:  c                                          |")
		print("| > Quit:         q                                          |")
		print("|                                                            |")
		print("|                                                            |")
		print("|______________________PRESS ENTER TO PLAY___________________|")
	
	def printWinnerMessage(self):
		self.clearDisplay()		
		print("  ___________")
		print(" '._==_==_=_.'")
		print(" .-\:      /-.")
		print("| (|:.     |) |")
		print(" '-|:.     |-'")
		print("   \::.    /")
		print("    '::. .'")
		print("      ) (")
		print("    _.' '._")
		
	def printLoserMessage(self):
		self.clearDisplay()		
		print(" _____                        _____")
		print("|  __ \                      |  _  |")
		print("| |  \/ __ _ _ __ ___   ___  | | | |_   _____ _ __ ")
		print("| | __ / _` | '_ ` _ \ / _ \ | | | \ \ / / _ \ '__|")
		print("| |_\ \ (_| | | | | | |  __/ \ \_/ /\ V /  __/ |")
		print(" \____/\__,_|_| |_| |_|\___|  \___/  \_/ \___|_|")
		
	def playAgain(self):
		self.river.reset()
		self.chickenAte = False
		self.foxAte = False
		self.clearDisplay()		
		self.printDescription()
		
	def showHelp(self):
		self.clearDisplay()
		self.printDescription()
		con = raw_input()
