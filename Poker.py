from random import randint       
# -*- coding: utf-8 -*-

# Generer en kortstokk (liste med koder). Koden er tresifret hvor første tall representerer fargen( 1 = spar, 2 = kløver, 3 = ruter, 4 = hjerter). De to neste tallene er kortets valør (2 til 14)       
def newDeck():

    deck = []
    
    i = 2
    
    x = 1
    
    count = 0
    
    while count < 52:
        
            
        if i == 15:
            i = 2
            x += 1
            
        verdi = i
        
        if verdi < 10:
            verdi = "0" + str(verdi)
            
        deck.append(str(x) + str(verdi))
        
        i += 1
        count += 1  

    return deck


# genererer en liste med x andtall lister (en for hver spiller), hvor hver liste inni listen holder koder for spillerenes kort
def deal(numberOfPlayers):

    if numberOfPlayers < 10:
        
        deck = newDeck()
       
        allHands = [[] for x in range(0, numberOfPlayers)]  

        for i in allHands:
            for x in range(0,5):
                card = deck[randint(0,len(deck) - 1)]
                i.append(card)
                deck.remove(str(card))

        return allHands
    
    else:
        print("Too many players!")
        

# konverterer listen generert med deal-funksjonen slik at spillerenes kort vises med tekst istedet for kode
def code2text(hand):
    
    handInText = [[] for x in range(0, len(hand))]
    
    types = ["", "Spades", "Clubs", "Diamonds", "Hearts"]
    
    values = ["", "Jack", "Queen", "King", "Ace"]
    
    count = 0
    
    for l in hand:
        
        for i in l:
            value = ""
            card = ""
            
            type = types[int(i[0])]
            
            if i[1] == "0":
                value = i[2]
            
            else:  
                value = i[1] + i[2]
            
            
            if int(value) < 11:
                card = str(value) + " of " + type
            
            else:
                numb = int(value[1])
                value = values[numb]
                
            card = str(value) + " of " + type
            
            handInText[count].append(card)
            
        count += 1
        
    return handInText
                    

# sjekker om en liste inneholder fem kort av samme farge
def checkFlush(hand):
    
    equals = 0
    tempHand = []
    score = 0
    
    for i in hand:
        tempHand.append(i[0])
    
    for i in range(0,len(tempHand)):
        if tempHand[0] == tempHand[i]:
            equals += 1
            
    if equals == 5:
        score += 90
    return score

# sjekker om en hånd har straight
def checkStraight(hand):
    score = 0
    
    values = []
    
    for i in hand:
        value = ""
        
        if i[1] == "0":
            value = int(i[2])
        else:
            value = int(str(i[1] + i[2]))
            
        values.append(value)
    
    sortedValues = sorted(values, key=int)
    
    count = 0
    
    x = 0
    
    while count < 4:
        
        if (sortedValues[count] + 1) == (sortedValues[count + 1]):
            x += 1
            
        count += 1
    
    
    if x == 4:
        score = 70
    else:
        score = 0
        
    return score
            
        
    

# sjekker om en liste har kort av like valører: par, to par, tres og fire like
def checkPar(hand):
    
    values = []
    
    score = 0
    par = 0
    topar = 0
    tres = 0
    four = 0
    
    for i in hand:
        value = str(i[1] + i[2])
        
        values.append(value)
    
    counted = [[x,values.count(x)] for x in set(values)]
    
    for i in counted:
        if i[1] == 2 and par > 0:
            if int(i[0]) > par:
                topar += int(i[0])
            else:
                topar = par      
        if i[1] == 2:
            par += int(i[0])
        if i[1] == 3:
            tres += int(i[0])
        if i[1] == 4:
            four += int(i[0])
    
    
    if par > 0 and tres == 0 and four == 0 and topar == 0:
        score = 10 + par
        
    if tres > 0 and par == 0 and four == 0 and topar == 0:
        score = 50 + tres
        
    if topar > 0 and tres == 0 and four == 0:
        score = 30 + topar
    
    if four > 0 and par == 0 and tres == 0 and topar == 0:
        score = 110 + four
        
    return score

# finner det høyeste kortet i en hånd
def highestCard(hands):
    
    tempHands = []
    
    for i in hands:
        value = ""
        
        if i[1] == "0":
            value = i[2]
        
        else:  
            value = i[1] + i[2]
            
        tempHands.append(value)
    
    sortedValues = sorted(tempHands, key=int)
    
    return sortedValues[len(sortedValues) - 1]
    
    
# sjekker en liste med hender og finner en vinner
def whoWins(hands):
    
    scores = []
    highCard = []
    winnerMessage = ""
    
    for i in hands:
        flushScore = checkFlush(i)
        straightScore = checkStraight(i)
        parScore = checkPar(i)
        
        totalScore = flushScore + straightScore + parScore
        
        scores.append(totalScore)
        
    if sum(scores) == 0:
        for i in hands:
            highCard.append(highestCard(i))
            
        sortedHighCards = sorted(highCard, key=int)
        winnerHigh = sortedHighCards[len(sortedHighCards) - 1]
        winnerPlayerHigh = highCard.index(winnerHigh) + 1
        winnerMessage = "Player " + str(winnerPlayerHigh) + " wins: highest card(" + str(winnerHigh) + ")"
        
    else:
            
        sortedScores = sorted(scores, key=int)
        winnerScore = sortedScores[len(sortedScores) - 1]
        winnerPlayer = scores.index(winnerScore) + 1
        
        if 10 < winnerScore < 30:
            card = winnerScore - 10
            winnerMessage = "Player " + str(winnerPlayer) + " wins: pair in " + str(card)
        
        if 30 < winnerScore < 50:
            card = winnerScore - 30
            winnerMessage = "Player " + str(winnerPlayer) + " wins: two pair (highest pair: " + str(card) + ")"
            
        if 50 < winnerScore < 70:
            card = winnerScore - 50
            winnerMessage = "Player " + str(winnerPlayer) + " wins: three of a kind (" + str(card) + ")"
        if 70 < winnerScore < 90:
            winnerMessage = "Player " + str(winnerPlayer) + " wins: straight"
        if 90 < winnerScore < 110:
            winnerMessage = "Player " + str(winnerPlayer) + " wins: flush"
        if 110 < winnerScore:
            card = winnerScore - 110
            winnerMessage = "Player " + str(winnerPlayer) + " wins: four of a kind (" + str(card) + ")"
            
    return winnerMessage
            
# spiller en runde med fem korts poker           
def playGame(numberOfPlayers):
    
    print("")
    print("Five hand poker, " + str(numberOfPlayers) + " players")
    hands = deal(numberOfPlayers)
    
    print("")
    print("Hands: ")
    print("")
    
    theHands = code2text(hands)
    
    for i in range(0,len(theHands)):
        print("Player " + str(i + 1) + ": ")
        print(theHands[i])
        print("")
    
    print(whoWins(hands))
    
    
number = input("Choose a number of players:")
playGame(int(number))



