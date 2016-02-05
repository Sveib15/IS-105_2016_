Code = input("hva er fakultetskoden?")

indeks=0
n=5
inpCode=[Code[i:i+n]for i in range(0, len(Code), n)]


while (indeks<len(inpCode)):
    if (inpCode[indeks]=="00000"):
        print "Okonomi og samfunnsvitenskap"
        indeks=indeks+1
    elif (inpCode[indeks]=="10000"):
        print "Teknologi og realfag"
        indeks=indeks+1
    elif (inpCode[indeks]=="11000"):
        print "Helse- og idrettsfag"
        indeks=indeks+1
    elif (inpCode[indeks]=="11100"):
        print "Humaniora og pedagogikk"
        indeks=indeks+1
    elif (inpCode[indeks]=="11110"):
        print "Laererutdanningen"
        indeks=indeks+1
    elif (inpCode[indeks]=="11111"):
        print "Kunstfag"
        indeks=indeks+1
    else :
        print "vennligst skriv en passede kode"
        indeks=indeks+1


