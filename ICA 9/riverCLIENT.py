import pygame
import socket
import time

class Boat:
	def __init__(self, imgpath, x, y, startDirY, leftStop, rightStop, topStop, bottomStop, crossSpeed):
		self.img = pygame.image.load(imgpath)
		self.x = x
		self.y = y
		self.leftStop = leftStop
		self.rightStop = rightStop
		self.topStop = topStop
		self.bottomStop = bottomStop
		self.dirx = 0
		self.diry = startDirY
		self.crossSpeed = crossSpeed
		self.isLeft = True
		self.isCrossing = False
		self.passengers = []
	
	def update(self):
		self.x += self.dirx
		self.y += self.diry
		
		if self.isCrossing == True:
			if self.x == self.leftStop:
				self.dirx = 0
				self.isLeft = True
				self.isCrossing = False
			elif self.x == self.rightStop:
				self.dirx = 0
				self.isLeft = False	
				self.isCrossing = False
		
		if self.y <= self.topStop or self.y >= self.bottomStop:
			self.diry = self.diry * -1
		
		for p in self.passengers:
			p.posInBoat(self.x, self.y)
	
	def draw(self, display):
		display.blit(self.img, (self.x, self.y))
				
	def addPassenger(self, p):
		if p.checkIfLoaded() == False and self.isCrossing == False and len(self.passengers) <= 1:
			if p.checkIfLeft() == True and self.isLeft == True or p.checkIfLeft() == False and self.isLeft == False:
				self.passengers.append(p)
				p.load(self.x)
					
	def removePassenger(self, p):
		if p.checkIfLoaded() == True and self.isCrossing == False:
			if self.isLeft == True:
				p.setLeft()
			elif self.isLeft == False:
				p.setRight()
			self.passengers.remove(p)
			p.unload()
	
	def crossRiver(self):
		if self.isLeft == True:
			self.dirx = self.crossSpeed
		else:
			self.dirx = -1* self.crossSpeed
		self.isCrossing = True
	
class Wave:
	def __init__ (self, imgpath, x, y, startDirY, topStop, bottomStop):
		self.img = pygame.image.load(imgpath)
		self.x = x
		self.y = y
		self.diry = startDirY
		self.topStop = topStop
		self.bottomStop = bottomStop
	
	def update(self):
		if self.y <= self.topStop or self.y >= self.bottomStop:
			self.diry = self.diry * -1
		self.y += self.diry
	
	def draw(self, display):
		display.blit(self.img, (self.x, self.y))
		
class Character:
	def __init__(self, imgpath, leftx, rightx, x, y, isMan, boatYoffset):
		self.img = pygame.image.load(imgpath)
		self.leftx = leftx
		self.rightx = rightx
		self.x = x
		self.y = y
		self.landy = y
		self.xdir = 0
		self.ydir = 0
		self.isLoaded = False
		self.isLeft = True
		self.isMan = isMan
		self.boatYoffset = boatYoffset
		
	def update(self):
		self.x += self.xdir
		self.y += self.ydir
	
	def draw(self, display):
		display.blit(self.img, (self.x, self.y))
		
	def posInBoat(self, boatx, boaty):		
		if self.isMan == True:
			self.x = boatx + 5
			self.y = boaty - self.boatYoffset
		else:
			self.x = boatx + 30
			self.y = boaty - self.boatYoffset
	
	def load(self, boatx):
		if self.isMan == True:		
			self.x = boatx + 5
		else:
			self.x = boatx + 30
		self.isLoaded = True
	
	def unload(self):
		self.isLoaded = False
	
	def setLeft(self):
		self.x = self.leftx
		self.y = self.landy
		self.isLeft = True
	
	def setRight(self):
		self.x = self.rightx
		self.y = self.landy
		self.isLeft = False
	
	def checkIfLoaded(self):
		return self.isLoaded
	
	def checkIfLeft(self):
		return self.isLeft

class StillImage:
	def __init__(self, imgpath, x, y):
		self.img = pygame.image.load(imgpath)
		self.x = x
		self.y = y
	
	def draw(self, display):
		display.blit(self.img, (self.x, self.y))
	
	def update(self):
		self.x = self.x
		self.y = self.y
		
class Display:
	def __init__(self, display):
		self.game_display = display
		pygame.display.set_caption("River Crossing")
		self.picture = []
		self.menu_text = pygame.image.load("resources/graphics/controls.png")
		self.menu_background = pygame.image.load("resources/graphics/pausebackground.png")
		
	def add(self, o):
		self.picture.append(o)
	
	def update(self):
		for p in self.picture:
			p.update()
	
	def draw(self, paused):
		for p in self.picture:
			p.draw(self.game_display)
		if paused:
			self.game_display.blit(self.menu_background, (0, 0))
			self.game_display.blit(self.menu_text, (0, 0))
		pygame.display.update()

class Game:
	def __init__(self, height, width):
		pygame.mixer.pre_init(44100,16,2,4096)
		pygame.init()
		self.display = pygame.display.set_mode((height, width))
		self.gm = Display(self.display)
		self.clock = pygame.time.Clock()
		
		self.UDP_IP = "192.168.38.102"
		self.UDP_PORT = 5005
		self.MESSAGE = "Test"
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		self.sock.setblocking(0)
		self.serverreply = ""

		self.man = Character("resources/graphics/man.png", -12, 438, -12, 110, True, 50)
		self.fox = Character("resources/graphics/fox.png", 22, 468, 22, 130, False, 25)
		self.grain = Character("resources/graphics/grain.png", 60, 507, 60, 143, False, 13)
		self.chicken = Character("resources/graphics/chicken.png", 88, 529, 88, 145, False, 12)
		self.wave_background = Wave("resources/graphics/wave1.png", 150, 180, -0.1, 178, 182)
		self.wave_foreground = Wave("resources/graphics/frontsea.png", 0, 180, 0.1, 178, 182)
		self.boat = Boat("resources/graphics/log.png", 157, 160, -0.05, 157, 365, 157, 163, 1)
		self.background = StillImage("resources/graphics/background.png", 0, 0)
		self.pause_text = StillImage("resources/graphics/pause.png", 0, 0)
		self.menu_text = StillImage("resources/graphics/controls.png", 0, 0)
		self.menu_background = StillImage("resources/graphics/pausebackground.png", 0, 0)
		self.startscreen = StillImage("resources/graphics/startscreen.png", 0, 0)
		self.bank_left = StillImage("resources/graphics/rock.png", 0, 145)
		self.bank_right = StillImage("resources/graphics/rock2.png", 440, 145)
		self.startscreen = pygame.image.load("resources/graphics/startscreen.png")
		self.lost_text = pygame.image.load("resources/graphics/gameover.png")
		self.gameover_background = pygame.image.load("resources/graphics/gameoverbackground.png")
		self.won_text = pygame.image.load("resources/graphics/youwon.png")
		self.play_again = pygame.image.load("resources/graphics/playagain.png")

		self.gm.add(self.background)
		self.gm.add(self.pause_text)
		self.gm.add(self.wave_background)
		self.gm.add(self.bank_left)
		self.gm.add(self.bank_right)
		self.gm.add(self.boat)
		self.gm.add(self.wave_foreground)
		self.gm.add(self.man)
		self.gm.add(self.fox)
		self.gm.add(self.grain)
		self.gm.add(self.chicken)
		
		self.lost = False
		self.paused = False
		self.playing = True
		self.playagain = True
		
		pygame.mixer.music.load("resources/sound/sang.mp3")
		pygame.mixer.music.set_volume(0.1)
		pygame.mixer.music.play(-1)
	
	def send(self, message):
		self.sock.sendto(message, (self.UDP_IP, self.UDP_PORT))
	
	def recieve(self):
		d = self.sock.recvfrom(1024)
		self.serverreply = d[0]
	
	def gameloop(self):
		print("Connecting...")
		self.send("connected")
		self.display.blit(self.startscreen, (0,0))
		pygame.display.update()
		
		starting = True
		while starting:
			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_RETURN:
						self.send("k")
				elif event.type == pygame.QUIT:
					self.send("disconnected")
					starting = False
					self.playing = False
					self.playagain = False
			if self.serverreply == "k":
				starting = False				
			try:
				self.recieve()
				print("Server: " + self.serverreply)
			except socket.error:
				self.serverreply = ""
		
		while self.playing:
			try:
				self.recieve()
				print("Server: " + self.serverreply)
			except socket.error:
				self.serverreply = ""
				
			if self.man.checkIfLoaded():
				if self.chicken.checkIfLeft() and self.grain.checkIfLeft() or self.chicken.checkIfLeft() == False and self.grain.checkIfLeft() == False:
					if self.chicken.checkIfLoaded() == False and self.grain.checkIfLoaded() == False:
						self.lost = True								
				if self.chicken.checkIfLeft() and self.fox.checkIfLeft() or self.chicken.checkIfLeft() == False and self.fox.checkIfLeft() == False:
					if self.chicken.checkIfLoaded() == False and self.fox.checkIfLoaded() == False:
						self.lost = True
						
			if self.lost == True:
				self.display.blit(self.gameover_background, (0, 0))
				self.display.blit(self.lost_text, (0, 0))
				self.display.blit(self.play_again, (0, 0))
				pygame.display.update()
				pygame.mixer.music.load("resources/sound/gameover.mp3")
				pygame.mixer.music.set_volume(1)
				pygame.mixer.music.play(1)
						
				choosing = True
				while choosing:
					for event in pygame.event.get():
						if event.type == pygame.KEYDOWN:
							if event.key == pygame.K_RETURN:
								self.sock.sendto("y", (self.UDP_IP, self.UDP_PORT))
							elif event.key == pygame.K_ESCAPE:
								choosing = False
								self.playing = False
								self.playagain = False
								self.send("disconnected")
						elif event.type == pygame.QUIT:
							choosing = False
							self.playing = False
							self.playagain = False
							self.send("disconnected")
					try:
						self.recieve()
						print("Server: " + self.serverreply)
					except socket.error:
						self.serverreply = ""	
					if self.serverreply == "y":
						choosing = False
		
								
			if self.man.checkIfLoaded() == False and self.fox.checkIfLoaded() == False and self.grain.checkIfLoaded() == False and self.chicken.checkIfLoaded() == False:
				if self.man.checkIfLeft() == False and self.fox.checkIfLeft() == False and self.grain.checkIfLeft() == False and self.chicken.checkIfLeft() == False:
						self.display.blit(self.gameover_background, (0, 0))
						self.display.blit(self.won_text, (0, 0))
						self.display.blit(self.play_again, (0, 0))
						pygame.display.update()
						pygame.mixer.music.load("resources/sound/winningsound.mp3")
						pygame.mixer.music.set_volume(0.3)
						pygame.mixer.music.play(1)
						
						choosing = True
						while choosing:
							for event in pygame.event.get():
								if event.type == pygame.KEYDOWN:
									if event.key == pygame.K_RETURN:
										self.sock.sendto("y", (self.UDP_IP, self.UDP_PORT))
									elif event.key == pygame.K_ESCAPE:
										choosing = False
										self.playing = False
										self.playagain = False
										self.send("disconnected")
								elif event.type == pygame.QUIT:
									choosing = False
									self.playing = False
									self.playagain = False
									self.send("disconnected")
							try:
								self.recieve()
								print("Server: " + self.serverreply)
							except socket.error:
								self.serverreply = ""	
							if self.serverreply == "y":
								choosing = False
				
			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					if self.paused == False:
						if event.key == pygame.K_SPACE:
							self.send("s")
								
						elif event.key == pygame.K_m:
							self.send("m")
								
						elif event.key == pygame.K_f:
							self.send("f")

						elif event.key == pygame.K_g:
							self.send("g")
								
						elif event.key == pygame.K_c:
							self.send("c")
							
					if event.key == pygame.K_p:
							self.send("p")
									
				elif event.type == pygame.QUIT:
					self.playing = False
					self.playagain = False
					self.send("disconnected")
					
			if self.serverreply == "s": #Cross
				if self.man.checkIfLoaded():
					self.boat.crossRiver()
					
			elif self.serverreply == "m": #Man
				if self.man.checkIfLoaded():
					self.boat.removePassenger(self.man)
				else:
					self.boat.addPassenger(self.man)
						
			elif self.serverreply == "g": #Grain
				if self.chicken.checkIfLoaded() == False and self.fox.checkIfLoaded() == False:
					if self.grain.checkIfLoaded():
						self.boat.removePassenger(self.grain)
					else:
						self.boat.addPassenger(self.grain)
					
			elif self.serverreply == "f": #Fox
				if self.chicken.checkIfLoaded() == False and self.grain.checkIfLoaded() == False:
					if self.fox.checkIfLoaded():
						self.boat.removePassenger(self.fox)
					else:
						self.boat.addPassenger(self.fox)
					
			elif self.serverreply == "c": #Chicken
				if self.fox.checkIfLoaded() == False and self.grain.checkIfLoaded() == False:
					if self.chicken.checkIfLoaded():
						self.boat.removePassenger(self.chicken)
					else:
						self.boat.addPassenger(self.chicken)
							
			elif self.serverreply == "p": #Pause
				if self.paused == True:
					self.paused = False
				else:
					self.paused = True
			
			elif self.serverreply == "y": #Play again
				self.send("disconnected")
				self.playagain = True
				self.playing = False
				
			self.gm.update()
			self.gm.draw(self.paused)
			self.clock.tick(120)

def main():
	running = True
	while running:
		game = Game(600,200)
		game.gameloop()
		if game.playagain == False:
			running = False
	
if __name__=="__main__": main()
