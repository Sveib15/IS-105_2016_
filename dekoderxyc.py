codeCode = input("what is the code");
indeksB = 0

L = list(codeCode)


while (indeksB<=len(L)):
    if (L[indeksB] == "0"):
        print "x"
        indeksB=indeksB+1

    elif (L[indeksB] == "1"):
        indeksB=indeksB+1

        if (L[indeksB] == "0"):
            print "y"
            indeksB=indeksB+1

        elif (L[indeksB] == "1"):
            print "c"
            indeksB=indeksB+1
        elif (L[indeksB] !="1" and L[indeksB] !="0"):
            print "invalid input"
            indeksB=indeksB+1

    elif (L[indeksB] !="1" and L[indeksB] !="0"):
        print "invalid input"
        indeksB=indeksB+1


