

# Programmer : Ahmet YILMAZ 



'''
# 1
numbers = []
for x in range (10):
    numbers.append (x)

print (numbers)

###
numbers = [x for x in range (10)]
print (numbers)


# 2 
for x in range(10):
    print (x**2)

###
numbers = [x**2 for x in range(10)]
print (numbers)

###
numbers = [x*x for x in range(10) if x % 3 == 0] # if sorgusu : 3 e tam bölünebilenleri al.
print (numbers)



# 3

myString = 'Merhaba'
listem = []

for letter in myString :
    listem.append(letter)
print (listem)

###
listem = [letter for letter in myString] 
print (listem)


# 5 

years = [1983, 1999, 2008, 1956, 1986]
ages = [2021-year for year in years]
print (ages)

###
results = [x if x % 2 == 0  else 'TEK' for x in range(1,10)] # 1-10 arasındaki sayıların mod 2 'si 0 a eşitse yazdır değilse 'TEK' yaz.
print (results)


# 7 

result = []


for x in range (3) :
    for y in range (3) :
        result.append((x,y))

print (result)

###
numbers = [(x,y,z) for x in range(3) for y in range (3) for z in range (3)]

print (numbers)


'''

# 1-100 arasında rastgele üretilecek bir sayıyı aşağı yukarı ifadeleri ile 
# buldurmaya çalışın. (hak = 5)
# ** "random modülü" için "python random" şeklinde arama yapın.
# ** 100 üzerinden puanlama yapın. (Her soru 20 puan)
# ** Hak bilgisini kullanıcıdan alın ve her soru belirtilen can sayısı üzerinden hesaplansın.


'''
import random

sayi = random.randint(1,100) 
can = int (input ("Kaç hak kullanmak istersiniz : "))
hak = can
sayac = 0 


while hak > 0 :
    hak -= 1 
    sayac += 1 
    tahmin = int (input ("Tahmininiz : "))

    if sayi == tahmin :
        print (f"Tebrikler, {sayac}. defada bildiniz. Toplam puanınız : {100 - (100/can) * (sayac - 1)}")
        break
    elif sayi > tahmin :
        print ("Yukarı")
    else :
        print ("Aşağı")

    if hak == 0 :
        print (f"Hakkınız bitmiştir, Tutulan sayi : {sayi}")
    
        

'''


