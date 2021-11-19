#%%
#1. Napiši program koji učitava listu i briše sve duplikate iz te liste te ispisuje novu listu s 
#obrisanim duplikatima.

lista=[1,2,2,3,3,4,5,6,7,7]
duplikati=[]

for i in lista:
    if i not in duplikati:
        duplikati.append(i)
print(lista)
print(duplikati)
# %%
#2. Napravi obrtaljku
# od unesenog stringa te na svakom drugom mjestu pridruzi nasumičan broj.
import random
txt  = input('Unesi neki string')
new_string=[]
index = len(txt)
while index:
    index -= 1
    x = str(random.randint(0,9))
    new_string.append(txt[index])
    new_string.append(x)
print(''.join(new_string))


# %%
#3.  Napiši program koji upisuje bodove n plesnih natjecanja. Ispiši zbroj svih bodova tako da odbaciš 
#    najbolji i najlošiji rezultat.
bodovi=[22,33,44,55,66]
bodovi.remove(min(bodovi))
bodovi.remove(max(bodovi))
print(bodovi)
print(sum(bodovi))


#%%
#4. Kreiraj listu brojeva i pretvori svaki element u listi u njegov kvadrat
lista=[2,4,6,8,10,12]
kvadrat=[broj**2 for broj in lista]
print(kvadrat)

# %%
#5 Kreiraj listu koja se sastoji od stringova i brojeva, te odvoji brojeve i stringove u zasebne liste

lista=[1,2,3,"a","b","c"]
brojevi=[]
string=[]
for i in lista:
    if type(i)== str:
        string.append(i)
    elif type(i) == int or type(i) == float:
        brojevi.append(i)
print(brojevi)
print(string)
# %%
#6  S tipkovnice učitavajte cijele brojeve. Prvi upisani broj može biti bilo koji cijeli broj. Učitavanje ponavljati dok god je upisani broj strogo
#veći od prethodno upisanog broja. Ispisati sumu svih učitanih brojeva
#osim broja zbog kojeg je prekinuto učitavanje.


def _sum_all_nums():
    tmp_a = 0
    all_nums = []
    while True:
        a = int(input("unesi broj"))

        if a < tmp_a:
            break

        all_nums.append(a)
        tmp_a = a

    print(sum(all_nums))
_sum_all_nums()

#%%
#7 Učitajte s tipkovnice 2 niza znakova, svaki od tih nizova znakova
#spremite u zasebnu varijablu. Ispišite indekse na kojima se pojavljuju
#ista slova neovisno o veličini ('a' i 'A' tretirati jednako)."""
a="lagan"
b="oblatna"

for index,char in enumerate(b):
    print(index, char)

    for index_2,char_2 in enumerate(a):
        print(index_2,char_2)
#%%
#8 Napišite program koji s tipkovnice učitava proizvoljni cijeli 
#troznamenkasti broj. Ako učitani broj nije troznamenkasti, ispišite 
#poruku o greški i prekinite daljnje izvođenje programa. U slučaju da 
#je učitani broj ispravan, ispišite prvi sljedeći troznamenkasti 
#palindrom. Na primjer, ako je učitani broj 120, prvi sljedeći palindrom  je 121.
def print_next_palindrom(str_number):
    if str_number == str_number[::-1]:
        print("Palindrom je")
    else:   
        int_number= int(str_number)+1
        new_str=str(int_number)
        print_next_palindrom(str(int_number))
    

a =input("unesi broj: ")
if len(a) ==1:
    print_next_palindrom(a)
#%%
#9 Napišite program koji učitava cijele brojeve sve dok je unesena 
#vrijednost veća od 0. Pronađite koji od učitanih brojeva ima najmanju sumu znamenki te ispišite taj broj i sumu."
num_list=[]
while True:
    a = int(input("Unesi broj"))
    if a <=0:
        break
    
    num_list.append(a)


max_sum=0
min_sum = 99999
for number in num_list:
    num_sum=0
    num_str = str(number)
    for character in num_str:
        num_sum+= int(character)
        if min_sum>num_sum:
            min_sum= num_sum
    #print(num_sum)
print(min_sum)
#%%
#10. S tipkovnice učitajte proizvoljni niz znakova. Kreirajte novi niz znakova koji će sadržavati naizmjence velika i mala slova iz ulaznog 
#niza, redom kako se pojavljuju u ulaznom nizu: prvo veliko slovo u ulaznom nizu, prvo sljedeće malo slovo u nastavku ulaznog niza, 
#prvo sljedeće veliko slovo u nastavku ulaznog niza itd. Novokreirani  niz ispišite na zaslon. U nastavku se nalazi primjer




#%%

#11 apišite program koji s tipkovnice učitava cijeli broj n iz intervala [3,  20]. U slučaju da je unesena vrijednost neispravna, ispisati prikladnu 
#poruku na ekran te zatražiti ponovni unos cijelog broja. Nakon učitane vrijednosti n, učitajte n parova cijelih brojeva. Nakon što je n
#parova brojeva učitano, ispišite parove brojeva koji imaju najveću sumu.

def insert_numbers_into_all_pairs():
     pairs = []
     pairs.append(int(input("prvi broj: ")))
     pairs.append(int(input("drugi broj: ")))
     all_pairs.append(pairs)

while True:
     n = int(input("unesi broj: "))
     if n < 1 or n > 3:
         print("error")
         break
     all_pairs = []  # globalna varijabla
     for i in range(n):
         insert_numbers_into_all_pairs()

     max_sum = 0
     num_index = 0
     for index in range(len(all_pairs)):
         if max_sum < sum(all_pairs[index]):
             max_sum = sum(all_pairs[index])
             num_index = index
     print(max_sum, all_pairs[num_index])

#%%
#12 Napišite program koji s tipkovnice učitava proizvoljni niz znakova. 
#Nad učitanim nizom znakova napravite analizu je li taj niz palindrom 
#ili nije. Niz je palindrom ako se isto čita slijeva nadesno ili pak zdesna nalijevo.
string=input(("Unesi string"))
if(string==string[::-1]):
      print("Ovo je palindrom")
else:
      print("Nije palindrome")
#%%
#13 Napišite program koji će inicijalizirati varijablu n na proizvoljnu 
#cjelobrojnu vrijednost. Vrijednost varijable n neka predstavlja red 
#tablice. Ispisati tablicu veličine n redaka i n stupaca. Vrijednost 1 
#neka se nalazi na glavnoj dijagonali, a vrijednost 0 na svim ostalim mjestima. U nastavku slijedi primjer za n=5:
#1 0 0 0 0
#0 1 0 0 0
#0 0 1 0 0
#0 0 0 1 0
#0 0 0 0 1

n=int(input("Unesi broj "))
for i in range(1,n+1):
    for j in range(1,n+1):
        if j==i:
            print(1,end="")
        else:
            print("0",end="")
    print()





#%%
#15
x=int(input("Unesi prvi broj"))
y= int(input("unesi drugi broj"))
for num in range(x, y + 1):
      if num % 2 != 0:
        print(num, end = " ")
#%%
#16 Napišite program koji sadrži varijablu u kojoj je upisan proizvoljni 
#niz znakova i brojčanu varijablu n. Provjerite je li vrijednost varijable 
#n manja od broja znakova u nizu. Ako je vrijednost varijable n veća 
#ispišite informaciju o grešci. Ispišite iz niza znakova svako n-to 
#slovo. Na primjer, ulazni niz je "ABCDEFGH", n je 2, tada je izlaz "ACEG"

string=input("Unesi string: ")
n= int(input("Unesi broj"))
b=""

print(len(string))
if len(string) > n:
    print("greška")
for n in range(len(string)):
   if (n % 2) == 0:
      b += string[n]
print(b)
#%%
#17 Napišite program koji sadrži varijablu u kojoj je upisan proizvoljni niz znakova. Ispišite koliko velikih slova se nalazi u nizu. Ako je neko od 
#unesenih slova u nizu "A", brojanje velikih slova je potrebno prekinuti  i ispisati informaciju da je veliko slovo "A" pronađeno.

string=(input("Unesi string"))

velika=[char for char in string if char.isupper()]

while True:
    if "A" in string:
        print("Pronaden je A")
        break
    else:
        print(str(velika))
#%%
#18. Ispišite sve parne brojeve između 1 i 1000 koju su istovremeno djeljivi i s 5 i s 13.

for i in range(1000):
    if i%2==0 and i%5==0 and i%13==0:
        print(i)
#%%
#19 Napisi program koji unosi n brojeva i od znamenke desetice svakog broja stvara novi broj.
n=int(input("unesi bro:j"))
g=""
for i in range(n):
    a = int(input("unesi neki broj: "))
    g += str((a%100) // 10)
print(g)

#%%
#20. Napisi program koji unosi n brojeva i sastavlja novi broj od najvece znamenke u svakom od brojeva 

new_number=""
while True:
    n=(input("Unos: "))
    if n=="0":
        break

    new_number+=max(n)
print(new_number)
#%%

#21b
a=1
b=2
while a<= 5 and b>=0:
    print(b*" "+a*"*")
    a+=2
    b-=1
    if a ==7 and b==-1:
        a=3
        b=1
        while a >=1 and b<=2:
            print(b*" "+a*"*")
            b+=1
            a-=2

        break



#%%
#%%
#22. Napišite program za koji traži najveći zajednički djelitelj dvaju brojeva

def djelitelj(a, b):
    if(b == 0):
        return a
    else:
        return djelitelj(b, a % b)
  
a = int(input())
b = int(input())
  
print("Najveci zajednicki djelitelj je ", end="")
print(djelitelj(a,b))
# %%
#23
T = 1000
def isplata(t,w):
    t = t-w
    return t

def uplata(t,d):
    t=t+d
    return t

while True:
    izbor=input("Dobrodosli na bankomat\n Odaberite 1 za podizanje novca, a 2 za uplaćivanje")
    if izbor=="1":
        W=int(input("Koliki je iznos isplate? "))
        T = isplata(T,W)
        a = input("Zelite li vidjeti novo stanje racuna? ")
        if a =="da":
            print(T)
    elif izbor=="2":
        D= int(input("Kolik je iznos uplate? "))
        T=uplata(T,D)
        b=input("Zelite li vidjeti novo stanje racuna? ")
        if b=="da":
            print(T)
    elif izbor=="quit":
        break

#%%
#25

proizvodi = []

def polica(predmet, cijena, kolicina):
    d1 ={}
    d1.setdefault('predmet', predmet)
    d1.setdefault('cijena', cijena)
    d1.setdefault('kolicina', kolicina)
    proizvodi = [d1]
    print(proizvodi)

predmet= input('unesi predmet')
cijena=input('unesi cijenu ')
kolicina=input('unesi kolicinu')

polica(predmet,cijena,kolicina)

#%%
#28
import random
recenice=["danas je petak","nebo se plavi","lagan kao oblatna","nesto random ne znam"]
while True:
    unos=input("Unesi string kako bi dobio povratnu informaciju")
    if unos.isalpha():
        a=(random.choice(recenice))
        print(a)
    elif unos== "-1":
        break
# %%
#24. zadan je rjecnik:
#automobil = {
#    'kilometri' : 230000,
#    'oprema' : ['zimske gume', 'zracni jastuk', 'protuprovalni bacac plamena'],

#}
 #   a) kilometre preuredite tako da dodatno broji i kilometre do servisa. postavite vrijednost na 300.
  #  b) iz opreme, promijenite "zimske gume" u "ljetne gume" te "zracni jastuk" u "zracni balon"
   # c) dodajte polje za unos specifikacije koja sadrzi godinu proizvodnje (1976.), potrosnju (15 litara) i max. brzinu (178 km/h)
    #d) dodajte cijenu i postavite je na 45000
    #e) dodajte osiguranje (npr. croatia) te postavite vrijednost na True
    #f) kada se pozove funkcija 'servis', znaci da se automobil servisirao i promijenile su se sljedece vrijednosti:
     #   - kilometri do servisa su se postavili na 2000
      #  - zracni balon postao je 'novi zracni jastuk'
       # - ljetne gume promijenjene su na 'cjelogodisnje gume'
        #- cijenu uvecajte za 2000
    
automobil = {'kilometri' : 230000,'oprema' : ['zimske gume', 'zracni jastuk', 'protuprovalni bacac plamena']}
#b
automobil['oprema'].append('ljetne gume')
print(automobil)
del automobil['oprema'][0]
print(automobil)
#d
automobil.update({"cijena":'45000'})
print(automobil)
#e
automobil.update({"Croatia osiguranje": True})
print(automobil)


# %%


#chatbot

bot={"bok":"bok", "kako si":"dobro sam a ti?",
"kako se zoves":"zovem se Random Bot","sto ti je funkcija":"odrzavanje razgovora s tobom"
,"u kojem programskom jeziku si napravljen":"u pythonu"}

while True:
    odgovor = input()
    
    if odgovor == "quit":
        break

    else:
        print(bot[odgovor])

# %%
# nisam stigao chatbota usavrsiti planiram sa Zbirkom odgovora u listi