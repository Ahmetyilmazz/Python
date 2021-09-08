

# Programmer : Ahmet YILMAZ 



'''
# Vize ve final notu hesaplama ve ortalamaya göre geçip kalma durumunu bulan pr.

vize = float(input("Vize notu : "))
final = float(input("Final notu : "))


ortalama = (vize*0.4 + final*0.6)

print (ortalama)

if (ortalama >= 60) :
    print ("Dersi Geçtiniz !!!")
else : 
    print ("Dersi Geçemediniz ...")


'''


'''
print(*range(3))  # 0 dan 3 e kadar sırala .

print(*range (3,10)) # 3'den 10'a kadar sırala .

print (*range (3,10,3)) # 3'den 10'a kadar 3'er 3'er sırala .


list = [*range(10)]
print(list)


'''


'''
# 1'den girilen sayiya kadar tek sayıları bastıran pr.

sayi1 = int(input("Lütfen bir sayi giriniz : "))

for i in range(1, sayi1 + 1, 2 ) :
    print (i)

'''



'''
# Hem tek hem 5 e bölünen 100 ‘e kadar olan sayıları sıralayan program.

for i in range(1, 101) :
    if (i % 5 == 0 and i % 2 != 0 ) :  # Bu satır : i'nin 5'e bölümünden kalan 0 ve i'nin 2'ye bölümünden kalan 0 değil ise koşulu anlamına gelir.
        print(i)
'''


'''
# Kenarları girilen dikdörtgenin çevre ve alanını hesaplayan program.

kisa_kenar = float (input ("Dikdörtgenin kısa kenarını giriniz  : "))
uzun_kenar = float (input ("Dikdörtgenin uzun kenarını giriniz  : " ))

dikdortgen_cevre = (kisa_kenar*2) + (uzun_kenar*2)
dikdortgen_alan = (kisa_kenar * uzun_kenar)

print ("Uzunluklarını girmiş olduğunuz dikdörtgenizin çevres : ",dikdortgen_cevre)
print ("Uzunluklarını girmiş olduğunuz dikdörtgenizin alanı  : ", dikdortgen_alan)



'''



