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

print timerFast.timeit(number=10)
print timerSlow.timeit(number=10)