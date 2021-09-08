

# Programmer : Ahmet YILMAZ 



'''
a = ["elma", "armut", "vişne", "kiraz", 6, 5, 5.9, ["fghghgh"]]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]


for eleman in a :         # Listedeki elemanları sırala.
    print ("{} adlı elemanın veri tipi : {}".format(eleman, type(eleman)))  #Listedeki elemanların tiplerini göster.


toplam = 0                  # Listede bulunan sayıları toplama.
for eleman in b :
    toplam += eleman
print ("Toplam : ",toplam)


'''


'''
i = 0 
while (i < 10) :
    print ("i'nin değeri : ", i)
    i += 3 


i = 10 
while (i <= 100) :
    print ("i'nin değeri : ", i) 
    i += 10 

'''

'''
# Girilen 2 sayı arasındaki (bu sayılar da dahil) sayıların toplamını bulan program.
sayi1 = int (input ("Lütfen 1. sayıyı giriniz : "))
sayi2 = int (input ("Lütfen 2. sayıyı giriniz : "))

toplam = 0

for i in range(sayi1,sayi2+1) :
    toplam += i
print ("Bu sayıların toplamları : ",toplam)


'''


'''
# Dik üçgenin hipotenüs uzunluğunu bulma.

dik_kenar_1 = float (input("Dik kenar 1'in uzunluğunu giriniz :  "))
dik_kenar_2 = float (input("Dik Kenar 2'in uzunluğunu giriniz : "))

hipotenüs = (dik_kenar_1**2 + dik_kenar_2**2)**0.5

print ("Hipotenüs uzunluğu : ", hipotenüs)


'''


'''
 
list = [2,3,4]

for i in range (1,10) :   
    if (i in list) :    # i değeri list'in içinde varsa başa dön.
        continue
    print(i) 


print ("\n")  # yukarıdaki ve alttaki kodun çıktısını karıştırmamak için eklenmiş bir satır.

liste = [8,4,3,1,-1,-4,-8]

toplam = 0 

for eleman in liste :
    if eleman <= 0 :
        break
    toplam += eleman 
print (toplam)


'''

