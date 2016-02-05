inpCode = input("hva er fakultetskoden?")

verdi = 0
indeks = 0

kodeListe = list(inpCode)

ferdig = False


while (indeks<=len(kodeListe)):
    if (ferdig==False):
        if (kodeListe[indeks]=="0"):
            ferdig=True
            indeks += 1
        elif (kodeListe[indeks]=="1"):
            indeks += 1
            verdi += 1
            if (verdi==5 and indeks==len(kodeListe)):
                ferdig=True
            elif (verdi>=6):
                print "Vennligst skriv en akseptabel kode"
                break
        elif (kodeListe[indeks]!="1" or kodeListe[indeks]!="0"):
            print "Vennligst skriv en akseptabel kode"
            break

    elif (ferdig==True):
        if (verdi==0):
            print "Okonomi og samfunnsvitenskap"
            break
        elif (verdi==1):
            print "Teknologi og realfag"
            break
        elif (verdi==2):
            print "Helse- og idrettsfag"
            break
        elif (verdi==3):
            print "Humaniora og pedagogikk"
            break
        elif (verdi==4):
            print "Laererutdanningen"
            break
        elif (verdi==5):
            print "Kunstfag"
            break




