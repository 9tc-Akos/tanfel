#ver1
# tanargyFelosztas=[]
# with open("beosztas.txt","r",encoding="UTF-8")as fin:
#     for sor in fin:
#         tanargyFelosztas.append(sor.strip())

# for elem in tanargyFelosztas:
#     print(f"{elem},")
    
# print(f"A listában {int(len(tanargyFelosztas)/4)}elem van")


#ver2


tanarok=[]
tantargyak=[]
osztalyok=[]
oraszamok=[]

rekord=[]


with open("beosztas.txt","r",encoding="UTF-8")as fin:
    for sor in fin:
        rekord.append(sor.strip())
        if len(rekord)==4:
            tanarok.append(rekord[0])
            tantargyak.append(rekord[1])
            osztalyok.append(rekord[2])
            oraszamok.append(int(rekord[3]))
            rekord=[]
            
for i in range(len(tanarok)):
    print(f"{tanarok[i]}, {tantargyak[i]}, {osztalyok[i]}, {oraszamok[i]}" )
    
    
print("2.feladat")
print(f"A bejegyzések száma: {len(tanarok)}")

print("3.feladat")
print(f"Az ikolában a heti összóraszám: {sum(oraszamok)}")    

def osszegzes(beTanar,tanarok,oraszamok):
    osszOraszam=0
    for i in range(len(tanarok)):
        if tanarok[i]==beTanar:
            osszOraszam+=oraszamok[i]
        return osszOraszam
print("4.feladat")
beTanar=input("Egy tanár neve= ") or "Albatrosz Aladin"
print(f"A tanár heti óraszáma: {osszegzes(beTanar,tanarok,oraszamok)}")

print("6. feladat")
def eldontes(beOsztaly,beTantargy,tantargyak,osztalyok):
    i=0
    while(i<len(tantargyak) and not (beTantargy==tantargyak[i] and "x"in osztalyok[i] and beOsztaly.split(".")[0]==osztalyok[i].split)):
        i+=1
    if i<len(tantargyak):
        return i<len(tantargyak)
beOsztaly=input("Osztály= ") or "10.b"
beTantargy= ("Tantárgy= ") or "kemia"
if eldontes(beOsztaly,beTantargy,osztalyok):
    print("Csoportbontásban tanulják.")
else:
    print("Nem tanulják csoportban")
print(f"")

print("7.feladat")
tanarokEgyedi=[]
for tanar in tanarok:
    if tanar not in tanarokEgyedi:
        tanarokEgyedi.append(tanar)
        
print(tanarokEgyedi)        

        