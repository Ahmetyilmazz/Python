

# Programmer : Ahmet YILMAZ 



# anahtar = 1 

while 1 :

    secim = int(input("\n Lutfen yapacaginiz islemi seciniz : \n0- Çıkış\n1- Toplama\n2- Cikarma\n3- Carpma\n4- Bolme\n5- Üs Alma\n6- Faktoriyel\n7- Karekök\n=> "))

    if secim == 0 :
        print("Uygulamadan Cikiliyor..")
        break

    if secim == 1 :
        sayi1 = float(input("Lütfen islem yapmak istediğiniz birinci sayıyı giriniz : "))
        sayi2 = float(input("Lütfen islem yapmak istediğiniz ikinci sayıyı giriniz : "))

        toplama = sayi1 + sayi2

        print (toplama)

    elif secim == 2 :
        sayi1 = float(input("Lütfen islem yapmak istediğiniz birinci sayıyı giriniz : "))
        sayi2 = float(input("Lütfen islem yapmak istediğiniz ikinci sayıyı giriniz : "))

        cikarma = sayi1 - sayi2

        print (cikarma)

    elif secim == 3 :
        sayi1 = float(input("Lütfen islem yapmak istediğiniz birinci sayıyı giriniz : "))
        sayi2 = float(input("Lütfen islem yapmak istediğiniz ikinci sayıyı giriniz : "))

        carpma  = sayi1 * sayi2

        print (carpma)

    elif secim == 4 :
        sayi1 = float(input("Lütfen islem yapmak istediğiniz birinci sayıyı giriniz : "))
        sayi2 = float(input("Lütfen islem yapmak istediğiniz ikinci sayıyı giriniz : "))

        bolme   = sayi1 / sayi2

        print (bolme)

    elif secim == 5 :
        sayi1 = float(input("Lütfen üssünü almak istediğiniz sayinin alt tabanini giriniz  : "))
        sayi2 = float(input("Lütfen üssü giriniz : "))

        us = sayi1 ** sayi2 

        print (us)

    elif secim == 6 :
        sayi1 = float(input("Lütfen faktoriyelini almak istediğiniz sayıyı giriniz : "))
        
        if (sayi1 > 0):
            
            faktoriyel = 1 
            for i in range(1,secim + 1) :
                faktoriyel *= i 
            print(faktoriyel)
        else : 
            print ("=> Lütfen pozitif sayı giriniz ...")

    elif secim == 7 :
        sayi1 = float(input("Lütfen karekökünü almak istediğinz sayiyi giriniz : "))

        karekok = (sayi1 ** 0.5) 

        print(karekok) 

    else :
        print ("Numaralandirilmis islemlerden birini seciniz ! ")
        
