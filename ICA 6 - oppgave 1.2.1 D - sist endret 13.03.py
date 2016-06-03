boat = []
boatLeftSide = True
leftSide = ["man", "chicken", "grain", "fox"]
rightSide = []
playing = True

def loadBoat(item):
    global playing
    
    if item in boat:
        print("")
        print("> The " + item + " is allready in the boat.")
        print("")
        
    else:
        if len(boat) <= 1:
        
            if boatLeftSide == True:
                if item in leftSide:
                    boat.append(item)
                    leftSide.remove(item)

                else:
                    if item in rightSide:
                        print("> The" + item + " is on the other side.")
                        print("")
                    else:              
                        print("> This item does not exist")
                        print("")
                      
            else:
                if item in rightSide:
                    boat.append(item)
                    rightSide.remove(item)
                
                else:
                    if item in leftSide:
                        print("> The " + item + " is on the other side.")
                        print("")
                    else:
                        print("> This item does not exist")
                        print("")
        else:
            print("> There is only room for two in the boat.")
            print("")
            
    if checkIfEat(leftSide) == True or checkIfEat(rightSide) == True or checkIfEat(boat) == True: 
        paint()
        print("")
        print("> You lost!")
        print("")
        
        prompt = raw_input("> Would you like to play again? (y/n): ")
        str(prompt)
        
        if prompt == "y":
            restart()
        if prompt == "n":
            playing = False        
    
    else:
        if "man" in rightSide and "chicken" in rightSide and "grain" in rightSide and "fox" in rightSide:
            paint()
            print("")
            printPokal()
            print("")
            print("> You won!")
            print("")
            
            prompt = input("> Would you like to play again? (y/n): ")
            
            if prompt == "y":
                restart()
            if prompt == "n":
                playing = False              
                 
        else:
            paint()
            
def unloadBoat(item):   
    global playing
    
    if boatLeftSide == True:
        if item in boat:
            boat.remove(item)
            leftSide.append(item)
            
        else:
            print("> There is no " + item + " in your boat")
            print("")
            
    else:
        if item in boat:
            boat.remove(item)
            rightSide.append(item)
            
        else:
            print("> There is no " + item + " in your boat")
            print("")
            
    if checkIfEat(leftSide) == True or checkIfEat(rightSide) == True or checkIfEat(boat) == True:  
        paint()
        print("")
        print("> You lost!")
        print("")
        
        prompt = raw_input("> Would you like to play again? (y/n): ")
        str(prompt)
        
        if prompt == "y":
            restart()
        if prompt == "n":
            playing = False
                              
    else:
        if "man" in rightSide and "chicken" in rightSide and "grain" in rightSide and "fox" in rightSide:          
            paint()
            print("")
            printPokal()
            print("")
            print("> You won!")
            print("")
            
            prompt = raw_input("> Would you like to play again? (y/n): ")
            str(prompt)
            
            if prompt == "y":
                restart()
            if prompt == "n":
                playing = False              
            
        else:
            paint()
    
def crossRiver():    
    global boatLeftSide
    
    if "man" in boat:
        
        if boatLeftSide == True:
            boatLeftSide = False      
        
        else:
            boatLeftSide = True   
    else:
        print("> Who is going to drive the boat...?")
        
    print("")
    paint()
                
def paint(): 
    painting = ""
    
    for i in leftSide:
        painting += i + " "
    
    painting += "||_"
    
    if boatLeftSide == True:
        painting += "\_"
        for i in boat:
            painting += " " + i
            
        painting += "_/__________||"
        
    else:
        painting += "__________\_"
        for i in boat:
            painting += " " + i
            
        painting += "_/_||"
        
    for i in rightSide:
        painting += " " + i
                
    print(painting)
       
def checkIfEat(alist):   
    youLoose = False
    
    if "man" not in alist:
        
        if "chicken" in alist and "grain" in alist:
            youLoose = True
            
        if "fox" in alist and "chicken" in alist:
            youLoose = True
            
    return youLoose

def checkIfWin():
    win = False
    global rightSide
    
    if "man" in rightSide and "chicken" in rightSide and "grain" in rightSide and "fox" in rightSide:
        win = True
        
    return win

def restart():
    global boat
    global boatLeftSide
    global leftSide
    global rightSide
    global playing
    
    boat = []
    boatLeftSide = True
    leftSide = ["man", "chicken", "grain", "fox"]
    rightSide = []
    playing = True 
    
    howTo()
       
def howTo():
    print("")
    print("Get all items to the other side of the river.")
    print("The chicken will eat the grain if the man is not present.")
    print("The fox will eat the chicken if the man is not present.")
    print("")
    print("Controls:")
    print("Load item:   'l + <item>'")
    print("Unload item: 'u + <item>'")
    print("Cross river: 'c'")
    print("Quit:        'q'")
    print("Restart:     'r'")
    print("")
    print("'help' to show controls")
    print("")
    paint()
    print("")    
    
def printPokal():
    print("  ___________")
    print(" '._==_==_=_.'")
    print(" .-\:      /-.")
    print("| (|:.     |) |")
    print(" '-|:.     |-'")
    print("   \::.    /")
    print("    '::. .'")
    print("      ) (")
    print("    _.' '._")
    
    
def play():    
    howTo()
    
    global playing
    
    while playing:
        prompt = raw_input("Your action: ")
        str(prompt)
            
        if prompt == "c":
            crossRiver()
            print("")
            
        elif prompt == "q":
            playing = False
            
        elif prompt == "r":
            restart()
            
        elif prompt[0] == "l":
            print("")
            loadBoat(str(prompt[2:len(prompt)]))
            print("")
            
        elif prompt[0] == "u":
            print("")
            unloadBoat(str(prompt[2:len(prompt)]))
            print("")
            
        elif prompt == "help":
            print("")
            print("Controls:")
            print("Load item:   'l + <item>'")
            print("Unload item: 'u + <item>'")
            print("Cross river: 'c'")
            print("Quit:        'q'")
            print("Restart:     'r'")
            print("")
            print("'help' to show controls")
            print("")
            paint()
            print("")
        else:
            print("")
            print("> Invalid action. Type 'help' too see the controls.")
            print("")
            
play()
        
        
            
    
    
    



        
    
            
    
        
