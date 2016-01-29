codeTxt = input("what is the message");
indeksT = 0

L = list(codeTxt)


while (indeksT<=len(L)):
    if (L[indeksT] == "x"):
        print "0"
        indeksT = indeksT+1

    elif (L[indeksT] == "y"):
        print "10"
        indeksT = indeksT+1

    elif (L[indeksT] == "c"):
        print "11"
        indeksT = indeksT+1

    elif (L[indeksT] !="x" and L[indeksT] !="y" and L[indeksT] !="c"):
        print "invalid input"
        indeksT = indeksT+1

