class File:
	def __init__(self, name, path):
		self.name = name
		self.content = ""
		self.path = path
		
	def isFolder(self):
		return False
		
	def setName(self, newName):
		self.name = newName
	
	def getName(self):
		return self.name
		
	def read(self):
		print(self.name + ":")
		print self.content
		
	def write(self):
		print(self.name + ":")
		prompt = raw_input()
		self.content = prompt
		
class Folder:
	def __init__(self, name, path):
		self.name = name
		self.content = {}
		self.path = path
		
	def isFolder(self):
		return True
		
	def setName(self, newName):
		self.name = newName
		
	def getName(self):
		return self.name
		
	def add(self, key, value):
		self.content[key] = value
	
	def remove(self, key):
		del self.content[key]
	
	def ls(self):
		for i in self.content:
			if self.content[i].isFolder() == True:
				print self.content[i].getName() + " [Folder]"
			else:
				print self.content[i].getName()

class Dir:
	def __init__(self):
		self.maindir = Folder("home", "/home")
		self.currentFolder = self.maindir
		self.allFolders = [self.maindir]
		self.allFiles = []
		
	def mkdir(self, f):
		newFolder = Folder(f,self.currentFolder.path + "/" + f)
		self.currentFolder.add(f, newFolder)
		self.allFolders.append(newFolder)
		
	def rmdir(self, f):
		if f in self.currentFolder.content:
			self.currentFolder.remove(f)
		
	def cd(self, f):
		for i in self.allFolders:
			if f in self.currentFolder.content:
				self.currentFolder = self.currentFolder.content[f]
				break
			elif i.path == f:
				self.currentFolder = i		
	
	def read(self, f):
		if f in self.currentFolder.content:
			self.currentFolder.content[f].read()
	
	def write(self, f):
		if f in self.currentFolder.content:
			self.currentFolder.content[f].write()
		
	def ls(self):
		self.currentFolder.ls()
		
	def create(self, f):
		newFile = File(f, (self.currentFolder.path + "/" + f))
		self.currentFolder.add(f, newFile)
		self.allFiles.append(newFile)
		
	def delete(self, f):
		if f in self.currentFolder.content:
			self.currentFolder.remove(f)	
	
	def getFilepath(self):
		return self.currentFolder.path
	
	def mv(self, f, newName):
		self.currentFolder.content[f].setName(newName)
	
	def cp(self, f):
		copy = self.currentFolder.content[f]
		copy.setName(f + "_kopi")
		self.currentFolder.add((f+"_kopi"), copy)
		
	def get(self, f):
		for fil in self.allFiles:
			if fil.getName() == f:
				fil.read()
				print("")
	
	def showhelp(self):
		print("mkdir  - make folder")
		print("rmdir  - delete folder")
		print("cd     - change directory")
		print("ls     - list of folder content")
		print("create - create file")
		print("read   - read file")
		print("write  - edit file")
		print("mv     - rename")
		print("cp     - copy")
		print("quit   - quit")
		print("help   - shows this list")
		
			
def main():
	testDir = Dir()
	running = True
	while running:
		prompt = raw_input("user ~" + testDir.getFilepath() + " $ ")
		if prompt != "":
			words = prompt.split()
			
			if words[0] == "ls":
				testDir.ls()
			elif words[0] == "read":
				testDir.read(words[1])
			elif words[0] == "write":
				testDir.write(words[1])
			elif words[0] == "mkdir":
				testDir.mkdir(words[1])
			elif words[0] == "cd":
				testDir.cd(words[1])
			elif words[0] == "create":
				testDir.create(words[1])
			elif words[0] == "rm":
				testDir.delete(words[1])
			elif words[0] == "rmdir":
				testDir.rmdir(words[1])
			elif words[0] == "mv":
				testDir.mv(words[1], words[2])
			elif words[0] == "cp":
				testDir.cp(words[1])
			elif words[0] == "help":
				testDir.showhelp()
			elif words[0] == "quit":
				break
			elif words[0] == "get":
				testDir.get(words[1])

if __name__ == "__main__": main()
			
		
		

		
		
	
