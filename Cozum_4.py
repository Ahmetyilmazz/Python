
# Programmer : Ahmet YILMAZ 
# 5'e 5 içi dolu ve içi boş kareler çizdiriniz. (yan yana çıktı olacak şekilde ve arada 5 karakter olacak şekilde.)

print("Odev_4'un Çözümüdür.. \n ") # \n bir alt satıra geç demektir.

# print("") # Print kendisi de bir satır ekliyor , Böyle de yapılabilir.

n = 5
kare1_satir1 = '*' * n
kare2_satir1 = '*' * n
bosluk = "     "    
print(kare1_satir1 + bosluk + kare2_satir1)
for i in range(n-2):
    print ('*' + ' ' * (n-2) + '*' + bosluk + '*' * n )
print(kare1_satir1 + bosluk + kare2_satir1) # İlk ve Son satirin ayni olması gerektiği için kopyaladım, degiskenler ondan dolayı aynı.


