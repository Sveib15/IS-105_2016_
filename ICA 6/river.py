
class River:
	leftSide = []
	rightSide = []
	boat = []
	boatIsLeft = True
	
	def __init__(self):
		self.leftSide = ["man", "chicken", "grain", "fox"]

	def load(self,item):
		if len(self.boat) < 2:
			if item not in self.boat:
				if self.boatIsLeft == True:
					if item in self.leftSide:
						self.boat.append(item)
						self.leftSide.remove(item)
				else:
					if item in self.rightSide:
						self.boat.append(item)
						self.rightSide.remove(item)
						
	def unload(self,item):
		if item in self.boat:
			if self.boatIsLeft == True:
				self.leftSide.append(item)
				self.boat.remove(item)
			else:
				self.rightSide.append(item)
				self.boat.remove(item)
				
	def cross(self):
		if "man" in self.boat:
			if self.boatIsLeft == True:
				self.boatIsLeft = False
			else:
				self.boatIsLeft = True
				
	def reset(self):
		self.leftSide = ["man", "chicken", "grain", "fox"]
		self.rightSide = []
		self.boat = []
		self.boatIsLeft = True
		
	def updatePicture(self):
		picture = ""
		leftLand = "---\__"
		rightLand = "__/---"
		leftBoatSide = "\_"
		rightBoatSide = "_/"
		river = "_____________________"
		
		for item in self.leftSide:
			picture += item + " "
		
		picture += leftLand
		
		if self.boatIsLeft == True:
			picture += leftBoatSide			
			for item in self.boat:
				picture += item + " "				
			picture += rightBoatSide + river + rightLand		
		else:
			picture += river + leftBoatSide
			
			for item in self.boat:
				picture += item + " "
				
			picture += rightBoatSide + rightLand
		
		for item in self.rightSide:
			picture += item + " "
			
		return picture
