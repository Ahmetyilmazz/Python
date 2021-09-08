


# Dörtgenin kenarları a ve b'dir. Konsoldan istenen a ve b tamsayi ölçü değerlerine göre
# dörtgen çizecek python kodunu yazınız. Her 1 br için * kullanınız.

print("Bu program sizden aldıgı a ve b degerlerine gore dortgen cizer. \n ")

a= int(input ("Uzun Kenari Giriniz (a) = "))
b= int(input ("Kisa Kenari Giriniz (b) = "))

print('*' * b)
for i in range(a-2):
    print ('*' + ' ' * (b-2) + '*')
print('*' * b)