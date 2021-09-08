


# Programmer : Ahmet YILMAZ

print ("Bu program sizden aldığı değerler üzerine 2. Dereceden denklemin köklerini bulur .!.")

# denklem = ax**2 + bx + c = 0

a = float(input("Lütfen x karenin katsayısını giriniz : "))
b = float(input("Lütfen x'in katsayısını giriniz : "))
c = float(input("Lütfen sabit sayiyi giriniz : "))

delta = b**2 - 4 * a * c 

if delta > 0 :
    x1 = (- b - delta**0.5)/(2*a) # 0.5 karekök. 
    x2 = (- b + delta**0.5)/(2*a)

    print("Denklemin 2 Reel kökü vardır bunlar : ")
    print ("X1 = ",x1)
    print ("X2 = ",x2)

if delta == 0 : 
    x1 = (- b + delta**0.5)/(2*a) 
    x2 = (- b + delta**0.5)/(2*a)
    x1 = x2
    print("Bu denklemin bir kökü vardır = ", x1)

if delta < 0 :
    print("Bu denklemin Reel kökü yoktur. ")