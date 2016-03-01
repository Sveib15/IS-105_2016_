from random import randint
import timeit


numberList = []
wordList = []



for i in range(0, 1000):
    i+= 1
    numberList.append(randint(0, 100))


for i in range (0, 100):
    i+= 1
    wordList.append("Word"+(str)(randint(0, 100)))


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


def fast():
    return search_fast(numberList, 10)
def slow():
    return search_slow(numberList, 10)



timerFast = timeit.Timer(stmt='fast', setup='from __main__ import fast')
timerSlow = timeit.Timer(stmt='slow', setup='from __main__ import slow')

def fastStr():
    return search_fast(wordList, "Word10")
def slowStr():
    return search_slow(wordList, "Word10")



timerFastStr = timeit.Timer(stmt='fastStr', setup='from __main__ import fastStr')
timerSlowStr = timeit.Timer(stmt='slowStr', setup='from __main__ import slowStr')

print "Fast int:"
print timerFast.timeit(number=100000)
print "Slow int:"
print timerSlow.timeit(number=100000)
print "Fast string:"
print timerFastStr.timeit(number=100000)
print "Slow string:"
print timerSlowStr.timeit(number=100000)
