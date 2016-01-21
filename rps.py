import random;

print ('Welcome to RPS')

draw = "It's a draw!"
win = "You won! Well done!"
lose = "You lost. Poor choice."

def player(): #Function for spillerens valg
        global choice
        choice = raw_input("Choose between Rock, Paper or Scissors");
        choice = choice.lower();
            
        if (choice == "rock"):
                choice = 0;
                print ("You chose rock");
                computer();
        elif (choice == "paper"):
                choice = 1;
                print ("You chose paper");
                computer();
        elif (choice == "scissors"):
                choice = 2;
                print ("You chose scissors");
                computer();
        else:
                choice = choice.upper();
                print (choice+" is an invalid choice");
                player();

def computer(): #Function for computerens valg
        global cpu
        cpu = random.randint (0,2);
        if (cpu == 0):
                print ("Computer picks rock");
                result();
        elif (cpu == 1):
                print ("Computer picks paper");
                result();
        elif (cpu == 2):
                print ("Computer picks scissors");
                result();
    

def result(): #Function for å avgjøre hvem som vinner
        if (choice == 0):
                if (cpu == 0):
                        print (draw)
                        playAgain();
                elif (cpu == 1):
                        print (lose)
                        playAgain();
                elif (cpu == 2):
                        print (win)
                        playAgain();
        elif (choice == 1):
                if (cpu == 0):
                        print (win)
                        playAgain();
                elif (cpu == 1):
                        print (draw)
                        playAgain();
                elif (cpu == 2):
                        print (lose)
                        playAgain();
        elif (choice == 2):
                if (cpu == 0):
                        print (lose)
                        playAgain();
                elif (cpu == 1):
                        print (win)
                        playAgain();
                elif (cpu == 2):
                        print (draw)
                        playAgain();

def playAgain(): #Function for å spille igjen ved riktig input
        replay = raw_input("Do you want to play again? Y/N")
        replay = replay.lower();
        if (replay == "y"):
                player();
        elif (replay == "n"):
                print ("Thanks for playing!");
        else: 
                print ("Y to play again, N to stop playing")
                playAgain();

player();



    
