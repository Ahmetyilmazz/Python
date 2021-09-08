
# Programmer : Ahmet YILMAZ

import random

print("Sayı tahmin oyununa hoş geldiniz!n 1-100 arasında bir sayı tahmin edin") 


sayi = random.randint(0,100)
sayi_tahmin_hakki = 10
while 1:

    tahmin = int(input("Tahmininiz: "))

    if tahmin == sayi :
        print ("Tebrikler ! Random Sayi : " + str(sayi))
        break 
    else :
        print ("Yanlış !!! Tekrar bir sayi giriniz : ")
        sayi_tahmin_hakki -= 1

    if sayi_tahmin_hakki == 0 :
        print ("Tahmin hakkiniz bitmiştir, Bilgisayarin seçtiği sayi :" + str(sayi))
        break 