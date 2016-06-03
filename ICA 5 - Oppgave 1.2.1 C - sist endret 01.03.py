from matplotlib import pyplot as plt
from random import randint
from timeit import Timer
import numpy as np
from scipy.interpolate import spline


def setUpList(length):
    numberList = []
    
    for i in range(0, length):
        numberList.append(randint(0,100))
               
    return numberList

def setUpWordList(length):
    wordlist = []
    
    for i in range(0, length):
        wordlist.append("word" + str(randint(0,100)))
        
    return wordlist


def search_fast(Haystack, needle):

    for item in Haystack:
        if item == needle:
            print "FAST IS TRUE"
            return True
    print "FAST IS FALSE"
    return False


def search_slow(haystack, needle):
    return_value = False
    for item in haystack:
        if item == needle:
            print "SLOW IS TRUE"
            return_value = True
    print "SLOW IS FALSE"
    return return_value
    
    
def run(listRange):

    graph = plt
    
    xvaluesFast = []
    yvaluesFast = []
    
    xvaluesSlow = []
    yvaluesSlow = []
    
    xwordValuesFast = []
    ywordValuesFast = []
    
    xwordValuesSlow = []
    ywordValuesSlow = []
    
    for i in range(1, listRange):
        
        numberValuesFast = []
        numberValuesSlow = []
        
        wordValuesFast = []
        wordValuesSlow = []
        
        for x in range(0,100):
            
            numberHaystack = setUpList(i)  
            wordHaystack = setUpWordList(i)
            
            needle = randint(0, 100)
            wordNeedle = "word" + str(needle)
            
            timerFastNumber = Timer(lambda: search_fast(numberHaystack, needle))
            timerSlowNumber = Timer(lambda: search_slow(numberHaystack, needle)) 
            
            timerFastWord = Timer(lambda: search_fast(wordHaystack, str(wordNeedle)))
            timerSlowWord = Timer(lambda: search_slow(wordHaystack, str(wordNeedle)))
           
            timeFastNumber = timerFastNumber.timeit(number=1)
            timeSlowNumber = timerSlowNumber.timeit(number=1)
            
            timeFastWord = timerFastWord.timeit(number=1)
            timeSlowWord = timerSlowWord.timeit(number=1)
            
            numberValuesFast.append(timeFastNumber)
            numberValuesSlow.append(timeSlowNumber)    
            
            wordValuesFast.append(timeFastWord)
            wordValuesSlow.append(timeSlowWord)
            
        averageFastNumber = sum(numberValuesFast) / len(numberValuesFast)
        averageSlowNumber = sum(numberValuesSlow) / len(numberValuesSlow)
        
        averageFastWord = sum(wordValuesFast) / len(wordValuesFast)
        averageSlowWord = sum(wordValuesSlow) / len(wordValuesSlow)
        
        xvaluesFast.append(i)
        yvaluesFast.append(averageFastNumber)
        
        xvaluesSlow.append(i)
        yvaluesSlow.append(averageSlowNumber)
        
        xwordValuesFast.append(i)
        ywordValuesFast.append(averageFastWord)
        
        xwordValuesSlow.append(i)
        ywordValuesSlow.append(averageSlowWord)
        
    graph.plot(xvaluesFast,yvaluesFast, label= "fast_search number")
    graph.plot(xvaluesSlow,yvaluesSlow, label= "slow_search number")
    graph.plot(xwordValuesFast, ywordValuesFast, label="fast_search word")
    graph.plot(xwordValuesSlow, ywordValuesSlow, label="slow_search word")
    graph.xlabel("Number of elements in list")
    graph.ylabel("Average search time")
    graph.legend()
    graph.show()
    
    
run(500)

        
        
    
    
    
    