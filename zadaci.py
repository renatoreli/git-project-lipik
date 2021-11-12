#%%
# 1
#Kreirajte dvije brojčane varijable te ispišite rezultat operatora usporedbe (usporedba jednakosti, nejednakosti, strogo veće, strogo manje, veće ili jednako, manje ili jednako). 

a= int(input("Unesi prvi broj: "))
b = int(input("Unesi drugi broj: "))
#unio sam prva dva broja
if a==b:
    print("A je jednako B")
elif a!=b and a<b:
    print("A je razlicit B i manji je od B")
elif a!=b and a>b:
    print("A je razlicit od B i veci je od B")
elif a>=b:
    print("A je vece ili jednako B")
elif a<=b:
    print("A je manje ili jednako B")
#zadao sve uvjete za provjeru i printao rezultate

# %%
#2
# Kreirajte dvije varijable i dodijelite im vrijednosti True ili False. Ispišite rezultate logičkih operatora (and, or, not) za dvije prethodno kreirane varijable.

x = int(input("Unesi prvi broj: "))
y = int(input("Unesi drugi broj: "))
#unio prva dva broja
print( x > y and x <10)
print( x > y or y!=x)
#zadao uvjete
# %%
#3
#Napišite program koji će u varijable a i b spremiti dva dvoznamenkasta broja. U varijablu a pohranite zadnju znamenku broja koji se nalazi u varijabli b, a u varijablu b pohranite zadnju znamenku broja koja se nalazi u varijabli a. Ispišite sadržaj varijabli a i b.

a = int(input("Unesi varijablu a: "))
b=int(input("Unesi varijablu b: "))
# to be continued
#%%
#4
# Omogućite unos 8 racionalnih brojeva te ispišite rezultat po sljedećoj formuli: 

from fractions import Fraction
#importao sam fraction library za racionalne brojeve
a =Fraction(1,2)
b =Fraction(3,5)
c =Fraction(4,5)
d =Fraction(5,6)
e =Fraction(1,8)
f =Fraction(3,7)
g =Fraction(2,5)
h =Fraction(1,8)
#unio sve racionalne brojeve
rez= a + b / c * d**e // f - g % h
#unio formulu
round(rez)
print ("Rezultat je",rez)
#ispisao rezultat
# %%
#6
from mpmath import mpc
