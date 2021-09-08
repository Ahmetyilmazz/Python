
# Programmer : Ahmet YILMAZ

print("Bu_Program_Girilen_Ortalamaya_Göre_Gecme_Durumu_Hesaplar. \n")

n = 0 
while n<=0 :
    n= int(input ("Lütfen Geçmeniz Gereken Ortalamayı Giriniz : "))

ortalama = float(input("Lutfen Kendi Ortalamanızı Giriniz : "))

if(ortalama >=n):
    print("Tebrikler, bu dersten geçtiniz...")
else :
    print("Üzgünüz, bu dersten kaldınız...")

