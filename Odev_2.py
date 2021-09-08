# Konsoldan istenen n değerine karşılık n tane Ahmet yazdırınız.

print("Bu program girilen sayi kez AHMET yazdirir. ")

n = 0 
while n<=0 :
    n= int(input ("Pozitif Bir Sayi Giriniz : "))

for a in range(n) : # Baslama ve bitis degeri range'nin içine göre değişir. 0'dan itibaren başlayıp liste oluşturur range ifadesi.
    print("Ahmet")  


print(str (a+1) + " kez Ahmet yazdirildi.")