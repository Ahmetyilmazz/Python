
# Programmer : Ahmet YILMAZ


# 1- Girilen bir sayının 0-100 arasında olup olmadığını kontrol ediniz.
'''
sayi = float(input("Sayi : "))

if (sayi > 0) and (sayi <= 100) :
    print("Sayi 0 ile 100 arasindadir.")
else :
    print ("Sayi 0 ile 100 arasinda değildir.")
'''

# 2- Girilen bir sayının pozitif çift sayı olup olmadığını kontrol ediniz.
'''
sayi = int(input("Sayi : "))

if (sayi > 0 ) and (sayi % 2 == 0) :
    print ("Sayi Pozitif Çift Sayidir. ")
else : 
    print("Sayi Pozitif Çift sayi değildir.")
'''

# 3- Girilen 3 sayıyı büyüklük olarak karşılaştırınız.
'''
a = int(input("A : "))
b = int(input("B : "))
c = int(input("C : "))

if (a > b) and (a > c) :
    print ("A en büyük sayidir.")
elif (b > a) and (b > c) :
    print ("B en büyük sayidir.")
elif (c > a) and (c > b) :
    print ("C en büyük sayidir. ")
else :
    print ("Tüm sayilar birbirine eşittir.")
'''


# 4- Kişinin ad, kilo ve boy bilgilerini alıp kilo indekslerini hesaplayınız.
#    Formül: (Kilo / boy uzunluğunun karesi)
#    Aşağıdaki tabloya göre kişi hangi gruba girmektedir.
#    0 - 18.4    => Zayıf 
#    18.5 - 24.9 => Normal  
#    25.0 - 29.9 => Kilolu
#    30.0 - 34.9 => Şişman (Obez)
'''

ad = input("Adınız : ")
kilo = float(input("Kilonuz : "))
boy = float(input("Boyunuz : "))

index = (kilo / boy)**2 # a**b a üzeri b anlamı taşır.

if (index >= 0) and (index <= 18.4) :
    print ("Zayıf")
elif (index > 18.4) and (index <= 24.9) :
    print ("Normal")
elif (index > 24.9) and (index <= 29.9) :
    print ("Kilolu")
elif (index > 29.9) and (index <= 34.9) :
    print ("OBEZ")

'''