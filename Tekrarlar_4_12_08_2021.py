

# Programmer : Ahmet YILMAZ 



'''
sayilar = [1,3,5,7,9,12,19,21]

while 1 :
    print (sayilar)

'''

'''
# 2: Başlangıç ve bitiş değerlerini kullanıcıdan alıp aradaki tüm tek sayıları ekrana yazdıran program.

sayi1 = int (input("Lütfen başlangıç sayınızı giriniz : "))
sayi2 = int (input ("Lütfen bitiş sayınızı giriniz : "))

for i in range (sayi1 , sayi2) :
    if i % 2 == 1 :
        print (i)

# üstteki for döngüsüyle çözümü; alttaki while döngüsüyle çözümü .

i = sayi1
while i < sayi2 :
    i += 1
    if % 2 == 1 :
        print (i)
'''


'''
# 3: 1-100 arasındaki sayıları azalan şekilde yazdırınız .

x = 100
while x > 0 :
    x -= 1 
    print(x)

'''




'''
###### ALTTAKİ ÖRNEK GAYET GÜZEL ÖRNEK ##############
# 4 - Kullanıcıdan alacağınız sınırsız ürün bilgisini ürünler listesi içerisinde saklayınız.
#     ** ürün sayısını kullanıcıya sorun.
#     ** dictionary listesi yapısı (name, price) şeklinde olsun.
#     ** ürün ekleme işlemi bittiğinde ürünleri ekrana while ile listeleyiniz.

urunler = []

urun_sayisi = int(input ("Lütfen ürün sayisini giriniz : "))

x = 0 

while (x < urun_sayisi) :
    urun_isim  =  input ("Ürün adını giriniz : ")
    urun_fiyat =  float (input ("Ürün fiyatını giriniz : "))
    urunler.append ({
        'Ürünün ismi' : urun_isim,
        'Ürünün fiyatı' : urun_fiyat
    })
    x += 1 


for urun in urunler : 
    print (urun)



'''




