


# Programmer : AHMET YILMAZ


print ("Bu program Vize ve final notu ile ortalama hesaplar ve bu ortalamasıyla öğrencinin geçip kaldığını belirtir.")

vize = int(input ("Lütfen vize notunuzu giriniz : "))
final = int(input("Lütfen final notunuzu giriniz : "))

ortalama = (vize * 0.4 + final * 0.6)
print ("Ders Ortalamanız : ",ortalama)

if ortalama >= 60 :
    print ("Tebrikler, GEÇTİNİZ.")
else :
    print ("Maalesef bu dersten GEÇEMEDİNİZ.")

