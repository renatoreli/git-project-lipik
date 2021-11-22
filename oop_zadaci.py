#1. napravite klasu Zivotinja. unutar klase definirajte konstruktor koji sadrzi atribute za naziv, tip, masu, vrstu ishrane.
#   Definirajte i metodu unutar klase koja ce ispisati navedene atribute. u glavnom potprogramu kreirajte dva razlicita objekta te pozovite kreiranu metodu.
#%%
class Zivotinja:
    def __init__(self,naziv,tip,masa,ishrana) :
        
        self.naziv= naziv
        self.tip = tip
        self.masa = masa 
        self.ishrana = ishrana

    def info(self):
        return '{} {} {} {}'.format(self.naziv,self.tip,self.masa,self.ishrana)

zivotinja1= Zivotinja("Gepard","Macka",50,"Mesojed")
zivotinja2= Zivotinja("Slon","Sisavac",1500,"Biljojed")

print(zivotinja1.info())
print(zivotinja2.info())

#%%
#2. napravite klasu za Obrada_stringa. klasa treba imati mogucnosti da iz nekog stringa napravi sljedece (u obliku metoda):
    #a) svaku rijec spremi u listu
    # b) ispisuje broj velikih i malih slova, brojeva, znakova
    #c) pretvorbu cijelih brojeva u rimske ekvivalente
    #d) unazadno ispisuje rijec po rijec (npr ako je uneseno "ja sam" treba ispisati "aj mas")
    #e) preoblicavanje slova, koja sadrzi sljedece funkcionalnosti: kapitalizacija svakog slova, uppercase cijelog stringa, spajanje stringa u jednu rijec i mijesanje slova
    #f) filtriranje brojeva ili slova, ovisno o trazenom
#napravite objekte, pozovite i testirajte program.

class Obrada_stringa:
    def __init__(self,recenica):

        self.recenica=recenica
        print(recenica)


    def lista(self):
        lista1=[]
        for element in lista1:
             lista1.append(element)
        return lista1

    def brojac(self):
        velika_slova = []
        mala_slova = []
        brojevi = []
        ukupno= []

        for slovo in recenica:
            if slovo.isalpha():
                ukupno.append(slovo)
            elif slovo.isupper():
                velika_slova.append(slovo)
            elif slovo.islower():
                 mala_slova.append(slovo)
            elif slovo.isdigit():
                brojevi.append(brojevi)
        print(f"Velika slova su {len(velika_slova)}")
        print(f"Mala slova su {len(mala_slova)}")
        print(f"Ukupno slova je {len(ukupno)}")
        print(f"Brojeva je {len(brojevi)}")
        	

    def reversed_string(self):
        return recenica[::-1]

recenica=Obrada_stringa('Reli1234')
print(recenica.lista())
print(recenica.brojac())
print(recenica.reversed_string())
# %%

#3. napravite klasu Geometrijski_lik. 
# Klasa treba imati mogucnost proracuna oplosja i obujma kugle, valjka i kvadra te ispis navedenih oplosja te koristenih formula za proracun. ispisite na ekran sve navedeno.
import math

class Geometrijsko_tijelo:
    def __init__(self,a,b,c,r,h):
        self.a = a
        self.b = b
        self.c = c
        self.r = r
        self.h = h

       
    def Obujamkugle(r):
        obujam=4/3*math.pi
        return(obujam)

    def Oplosjekugle(r):
        oplosje=(4*(r**2))*math.pi
        return(oplosje)

    def ObujamValjka(r,h):
        obujamvaljka=(math.pi*r**2*h)
        return(obujamvaljka)

    def OplosjeValjka(r,h):
        oplosjevaljka=2*math.pi*r*(r+h)
        return(oplosjevaljka)

    def OplosjeKvadra(a,b,c):
        oplosjekvadra=2*(a*b+a*c+b*c)
        return(oplosjekvadra)

    def ObujamKvadra(a,b,c):
        obujamvkvadra=a*b*c
        return(obujamvkvadra)


Tijelo=Geometrijsko_tijelo(1,1,1,1,1)

print(Tijelo.Obujamkugle())
print(Tijelo.Oplosjekugle())
print(Tijelo.ObujamValjka())
print(Tijelo.OplosjeValjka())
print(Tijelo.OplosjeKvadra())
print(Tijelo.ObujamKvadra())
### ------------------------------------------------------------------------------------ ###
### krivo shvatio logiku zadatka , preformulirati i definirati tocnije klase i varijable ###
### ------------------------------------------------------------------------------------ ###
# %%
#4. kreirajte klasu Vozilo, koja sadrzi sljedece atribute: marka, model, masa, kilometraza, max brzina, boja, cijena. napravite 2 objekta sa razlicitim atributima.
#   Nakon postavljanja, izmijenite boju u crvenu, kilometrazu postavite na 10000,
#  max brzinu spustite za 15 i cijenu spustite za 10%. usporedite aute te ispisite koji od njih ima vecu max brzinu, kilometrazu i manju cijenu. 

class Vozilo:
    def __init__(self,marka,model,masa,kilometraza,max_brzina,boja,cijena):   #definirao sve atribute vozila
        self.marka= marka
        self.model= model
        self.masa=masa
        self.kilometraza=kilometraza
        self.max_brzina=max_brzina
        self.boja=boja
        self.cijena=cijena

    def info(self):
        return '{} {} {} {} {} {} {}'.format(self.marka,self.model,self.masa,self.kilometraza,self.max_brzina,self.boja,self.cijena) # funkcija za ispisivanje informacije o vozilu

auto1=Vozilo("Mitsubishi","Lancer Evo VIII","1400kg",50000,250,"Black",60000)             # 2 objekta vozila
auto2= Vozilo("Nissan","Skyline R32","1300kg",50000,230,"Grey",50000) 
 

auto1.boja ="Yellow"              #promjena atributa po zadatku
print(auto1.boja)

auto2.boja ="Yellow"
print(auto1.boja)

auto1.kilometraza=10000
print(auto1.kilometraza)

auto2.kilometraza=10000
print(auto1.kilometraza)

auto1.max_brzina=235
print(auto1.max_brzina)

auto2.max_brzina=235
print(auto2.max_brzina)

auto1.cijena=60000-6000
print(auto1.cijena)

auto2.cijena=50000-6000
print(auto2.cijena)

print(auto1.info())                                 #ispis informacija nakon promjene atributa
print(auto2.info())

if auto1.max_brzina > auto2.max_brzina:
    print("Mitsubishi je brzi od Nissana")               #ispitivao uvjete zadane u zadatku te ih ispisao
else:
    print("Nissan je brzi")

if auto1.kilometraza>auto2.kilometraza:
    print("Lancer ima vecu kilometrazu")
else:
    print("R32 ima vecu kilometrazu")

if auto1.cijena > auto2.cijena:
    print("Lancer je skuplji")
else:
    print("R32 je skuplji")
# %%
