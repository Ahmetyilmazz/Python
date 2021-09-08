
# Programmer : Ahmet YILMAZ

print ("İşlem Seçiniz : ('1' Toplama  '2' Çıkarma '3' Çarpma '4' Bölme)")

def Topla (x,y) :
    return x + y 

def Cikar(x,y) :
    return x - y 

def Carp(x,y) :
    return x * y 

def Bol(x,y) :
    return x / y

secim = input ("Lütfen İşlemi Seçiniz : ")
sayi1 = float(input("1. Sayiyi giriniz : "))
sayi2 = float(input("2. Sayiyi Giriniz : "))

if secim == '1' :
    print ("{} + {} = {} ".format(sayi1,sayi2, Topla(sayi1,sayi2)))
elif secim == '2' :
    print ("{} - {} = {} ".format(sayi1,sayi2, Cikar(sayi1,sayi2)))
elif secim == '3' :
    print ("{} * {} = {} ".format(sayi1,sayi2, Carp(sayi1,sayi2)))
elif secim == '4' :
    print ("{} / {} = {} ".format(sayi1,sayi2, Bol(sayi1,sayi2)))