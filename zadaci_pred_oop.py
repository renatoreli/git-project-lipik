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
string="Random"[::-1]
print(string)
lista_string=list(string)

print (lista_string)



# %%
#3.  Napiši program koji upisuje bodove n plesnih natjecanja. Ispiši zbroj svih bodova tako da odbaciš 
#    najbolji i najlošiji rezultat.



#%%
#4. Kreiraj listu brojeva i pretvori svaki element u listi u njegov kvadrat
lista=[2,4,6,8,10,12]
kvadrat=[broj**2 for broj in lista]
print(kvadrat)

# %%
#5 Kreiraj listu koja se sastoji od stringova i brojeva, te odvoji brojeve i stringove u zasebne liste

lista=[1,2,3,"a","b","c"]
brojevi=[]
for item in lista:
    for subitem in item.split():
        if(subitem.isdigit()):
            brojevi.append(subitem)
print(brojevi)
# %%
