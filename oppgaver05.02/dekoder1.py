Code = input("hva er fakultetskoden?")

indeks=0
n=3
inpCode=[Code[i:i+n]for i in range(0, len(Code), n)]


while (indeks<len(inpCode)):
    if (inpCode[indeks]=="000"):
        print "Okonomi og samfunnsvitenskap"
        indeks=indeks+1
    elif (inpCode[indeks]=="100"):
        print "Teknologi og realfag"
        indeks=indeks+1
    elif (inpCode[indeks]=="110"):
        print "Helse- og idrettsfag"
        indeks=indeks+1
    elif (inpCode[indeks]=="111"):
        print "Humaniora og pedagogikk"
        indeks=indeks+1
    elif (inpCode[indeks]=="011"):
        print "Laererutdanningen"
        indeks=indeks+1
    elif (inpCode[indeks]=="001"):
        print "Kunstfag"
        indeks=indeks+1
    else :
        print "vennligst skriv en passede kode"
        indeks=indeks+1



