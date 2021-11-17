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
#6

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
#7
a="lagan"
b="oblatna"

for index,char in enumerate(b):
    print(index, char)

    for index_2,char_2 in enumerate(a):
        print(index_2,char_2)
#%%
#8
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
#9
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
#11

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
#12
string=input(("Unesi string"))
if(string==string[::-1]):
      print("Ovo je palindrom")
else:
      print("Nije palindrome")
#%%
#15
x=int(input("Unesi prvi broj"))
y= int(input("unesi drugi broj"))
for num in range(x, y + 1):
      if num % 2 != 0:
        print(num, end = " ")
#%%
#19
n=int(input("unesi bro:j"))
g=""
for i in range(n):
    a = int(input("unesi neki broj: "))
    g += str((a%100) // 10)
print(g)
#%%




