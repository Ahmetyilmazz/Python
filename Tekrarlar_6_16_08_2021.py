

# Programmer : Ahmet YILMAZ 



'''

# 1
def sayHello() :
    print ('Hello')

sayHello()
sayHello()


# 2

def yasHesapla (dogumYili) :
    return 2021 - dogumYili

ageAhmet =  yasHesapla(2001)
ageAda   = yasHesapla(2019)
ageCinar = yasHesapla(2017)

print (ageAhmet, ageAda, ageCinar)


# 3

def EmekliligeKacYilKaldi(dogumYili, isim ) :

    yas = yasHesapla(dogumYili)
    emeklilik = 65 - yas

    if emeklilik > 0 :
        print (f"emekliliğine {emeklilik} yıl kaldı")
    else :
        print ("Zaten emekli oldunuz")
    
EmekliligeKacYilKaldi(1983, 'Ali')
EmekliligeKacYilKaldi(1950, 'Ahmet')
EmekliligeKacYilKaldi(1974, 'Yağmur')

print (help (EmekliligeKacYilKaldi)) 

'''
# 1- Gönderilen bir kelimeyi belirtilen kez ekranda gösteren fonksiyonu yazın.

def yazdir (kelime, adet) :
    print (kelime * adet)

yazdir ('Merhaba\n', 10) # \n alt satıra geçmesi için konmuştur.


# 2- Kendine gönderilen sınırsız sayidaki parametreyi listeye çeviren fonksiyonu yazın.


def listeyeCevir(*parametreler) :
    liste = []

    for parametre in parametreler:
        liste.append(parametre)
    
    return liste 

result = listeyeCevir(10,20,30,'Merhaba')

print (result)


# 3- Gönderilen 2 sayı arasındaki tüm asal sayıları bulun.

def asalSayilariBul (sayi1, sayi2) :
    for sayi in range (sayi1, sayi2 + 1) :
        if sayi > 1 :
            for i in range (2, sayi) :
                if (sayi % i == 0) :
                    break
            else :
                print (sayi)

sayi1 = int (input ("Sayi 1 : "))
sayi2 = int (input ("Sayi 2 : "))

asalSayilariBul (sayi1, sayi2)



# 4- Kendisine gönderilen bir sayının tam bölenlerini bir liste şeklinde döndüren fonksiyonu yazınız.

def tamBolenleriBul (sayi) :
    tamBolenler = [] 

    for i in range (2, sayi) :
        if (sayi % i == 0):
            tamBolenler.append(i)
        
    return tamBolenler

print (tamBolenleriBul(20))

