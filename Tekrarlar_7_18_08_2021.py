

# Programmer : Ahmet YILMAZ



# Fonksiyon kullanarak hesap makinesi .

def toplama (sayi1, sayi2) :
    return sayi1 + sayi2

def cikarma (sayi1, sayi2) :
    return sayi1 - sayi2

def carpma (sayi1, sayi2) :
    return sayi1 * sayi2

def bolme (sayi1, sayi2) :
    return sayi1 / sayi2

while 1:

    secim = int(input ("Lütfen seçim yapın (0- Çıkış 1- Toplama 2-Çıkarma 3-Çarpma 4-Bölme) : "))

    if secim == 0 :
        exit()

    sayi1 = int(input("Lütfen birinci sayiyi giriniz : "))
    sayi2 = int(input("Lütfen ikinci sayiyi giriniz : "))

    if secim == 1 :
        print ("Sonuç : ",toplama(sayi1,sayi2))
    elif secim == 2 :
        print ("Sonuç: ", cikarma (sayi1, sayi2))
    elif secim == 3 :
        print ("Sonuç: ", carpma (sayi1, sayi2))
    elif secim == 4 :
        print ("Sonuç: ", bolme (sayi1, sayi2))
    else :
        print ("Yanlış seçim lütfen tekrar deneyin.")
        exit ()

