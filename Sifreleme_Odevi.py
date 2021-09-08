
'''
24.04.2020
// AHMET YILMAZ //
// Odev = ODEV-2_Sifre_Kontrolu
'''

# Kontrol Karakter Dizileri 
buyuk_harfler = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
kucuk_harfler = "abcdefghijklmnopqrstuvwxyz"
alfanumerik = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
sayilar = "0123456789"
bosluk = " "

# Kullanıcı Bilgilendirme Mesajları / Şifre Kuralları 
print ("...Aşağıdaki şartlara uygun bir şifre giriniz... \n")
print ("1. En az 8, en fazla 12 karakter içermelidir. ")
print ("2. En az 1 büyük harf ve en az 1 küçük harf karakteri içermelidir. ")
print ("3. Sayı ile başlayıp sayı ile bitemez. (Örnek: 1test, test5, 2test4 vb. kabul edilmez.) ")
print ("4. Boşluk karakteri içeremez. ")
print ("5. En az 1 tane alfanümerik olmayan karakter (Rakam ve Harf dışında) içermelidir.")
print ("6. İçinde tekrarlayan karakter bulunmamalıdır. (Örnek: test, deneme, t3r3)")
print ("7. İçinde en az 1 tane sayi bulunmalidir (İlk ve son karakterde bulunamaz).")
print ("8. Alfanümerik karakter ilk veya son karakterde bulunmamalıdır.")

print ("\n")


while 1 :

    sifre = input ("Şifrenizi Giriniz : ")    

    print ("\n")   

    # 1. Şart 
    sekizden_buyuk_esit_mi = 0    # Durum değişkeni.
    onikiden_kucuk__esit_mi = 0   # Durum değişkeni.
    if len(sifre) >= 8 : # Şifre boyutu 8'den büyük eşitse    
        sekizden_buyuk_esit_mi = 1

    if len(sifre) <= 12 :  # Şifre boyutu 12'den küçük eşitse
        onikiden_kucuk__esit_mi = 1  

    if (sekizden_buyuk_esit_mi == 1) & (onikiden_kucuk__esit_mi == 1) :  # 8 <= sifre boyutu <= 12 
        print ("1. Şart sağlanmıştır.")
    else :
        if sekizden_buyuk_esit_mi == 0 :  
            print ("Şifreniz de karakter sayınız en az 8'den başlamalıdır.")
        
        if onikiden_kucuk__esit_mi == 0 :
            print ("Şifreniz de karakter sayınız 12'yi geçemez.")
        
        continue  # Şart sağlanmadıysa while'ın başına dön. 

    # 2. Şart
    buyuk_harf_var_mı = 0   # Durum değişkeni.
    kucuk_harf_var_mı = 0   # Durum değişkeni.
    for karakter in sifre :
        if karakter in buyuk_harfler :  # buyuk_harfler dizi içinde karakter varsa
            buyuk_harf_var_mı = 1

        if karakter in kucuk_harfler :  # kucuk_harfler dizi içinde karakter varsa
            kucuk_harf_var_mı = 1

    if (buyuk_harf_var_mı == 1) & (kucuk_harf_var_mı == 1) : # Büyük ve Küçük harf varsa
        print ("2. Şart Sağlanmıştır.")
    else : 
        if buyuk_harf_var_mı == 0 :  
            print ("Şifreniz de en az 1 tane büyük harf kullanmalısınız.")

        if kucuk_harf_var_mı == 0 :
            print ("Şifreniz de en az 1 tane küçük harf kullanmalısınız.")

        continue  # Şart sağlanmadıysa while'ın başına dön. 

    # 3. Şart 
    sayi_ile_baslıyor_mu = 0  # Durum değişkeni.
    sayi_ile_bitiyor_mu = 0   # Durum değişkeni.
    if sifre[0] in sayilar :  # sifrenin ilk karakteri sayıysa
        sayi_ile_baslıyor_mu = 1

    if sifre[-1] in sayilar : # Şifrenin son karakteri sayıysa 
        sayi_ile_bitiyor_mu = 1

    if (sayi_ile_baslıyor_mu == 1) | (sayi_ile_bitiyor_mu == 1) : # İlk karakteri veya son karakteri sayıysa
        print ("Şifreniz sayı ile başlayıp sayı ile bitemez.")
        continue  # Şart sağlanmadıysa while'ın başına dön.
    else :
        print ("3. Şart sağlanmıştır")

    # 4. Şart 
    bosluk_karakteri_var_mı = 0 # Durum değişkeni.
    for karakter in sifre :   
        if karakter in bosluk : # bosluk dizi içinde karakter varsa
            bosluk_karakteri_var_mı = 1 

    if bosluk_karakteri_var_mı == 1 :
        print ("Şifreniz de boşluk karakteri içeremez.")

        continue  # Şart sağlanmadıysa while'ın başına dön.
    else :
        print ("4. Şart Sağlanmıştır.") 

    # 5. Şart
    alfanumerik_olmayan_karakter_var_mı = 0  # Durum değişkeni.
    for karakter in sifre :
        if karakter not in alfanumerik : # alfanumerik dizi içinde karakter varsa
            alfanumerik_olmayan_karakter_var_mı = 1
            
    if alfanumerik_olmayan_karakter_var_mı == 1 : 
        print ("5. Şart Sağlanmıştır.")
    else :
        print ("Şifreniz de alfanümerik olmayan karakter olmalıdır.")

        continue  # Şart sağlanmadıysa while'ın başına dön. 
    
    # 6. Şart // Dersteki örneklerden faydalanıldı...
    karakter_tekrari_var_mı = 0 # Durum değişkeni.
    krktr_dizi = ""
    for karakter in sifre :
        if karakter not in krktr_dizi : # krktr_dizi içinde karakter yoksa
            krktr_dizi += karakter # krktr_dizi = krktr_dizi + karakter 
        else :
            karakter_tekrari_var_mı = 1 

    if karakter_tekrari_var_mı == 1 :
        print ("Şifreniz de tekrar eden karakter olmamalıdır.")

        continue  # Şart sağlanmadıysa while'ın başına dön. 

    else :
        print ("6. Şart Sağlanmıştır.")

    # 7. Şart 
    icinde_sayi_var_mi = 0  # Durum değişkeni.
    for karakter in sifre :
        if karakter in sayilar : # sayilar içinde karakter varsa
            icinde_sayi_var_mi = 1 
    
    if icinde_sayi_var_mi == 1 :
        print ("7. Şart sağlanmıştır.")
    else :
        print ("Şifreniz de en az 1 tane sayi olmalidir.")

        continue  # Şart sağlanmadıysa while'ın başına dön.

    # 8. Şart 
    ozel_karakter_ile_basliyor_mu = 0  # Durum değişkeni.
    ozel_karakter_ile_bitiyor_mu = 0   # Durum değişkeni.
    if sifre[0] not in alfanumerik :   # alfanumerik dizi içinde sifrenin ilk karakteri yoksa
        ozel_karakter_ile_basliyor_mu = 1

    if sifre[-1] not in alfanumerik : # alfanumerik dizi içinde sifrenin son karakteri yoksa
        ozel_karakter_ile_bitiyor_mu = 1

    if (ozel_karakter_ile_basliyor_mu == 1) | (ozel_karakter_ile_bitiyor_mu == 1) : # İlk ve son karakter özel karakterse
        print ("Özel karakter ile başlayıp özel karakter ile bitemez.")
        continue  # Şart sağlanmadıysa while'ın başına dön.

    else :
        print ("8. Şart Sağlanmıştır. \n")



    sifre_tekrar = input ("Şifrenizi Tekrar Giriniz : ")
    if sifre == sifre_tekrar : 
        print ("Şifreniz Oluşturuldu.")
        break 
    else :
        print ("Girilen şifreler aynı değil.")

