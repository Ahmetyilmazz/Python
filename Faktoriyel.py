

# Programmer : Ahmet YILMAZ

faktoriyel = 1 
while 1 :
    
    sayi = int(input("Lütfen sayiyi giriniz : "))

    if sayi <= 0 :
        print ("Lütfen pozitif bir sayi giriniz.")
    else :
        for i in range (1,sayi + 1) :
            faktoriyel *= i
        print ("Girdiğiniz sayinin faktöriyeli = ",faktoriyel)
    break