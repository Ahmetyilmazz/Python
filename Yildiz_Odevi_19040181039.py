
''' // AHMET YILMAZ
    // Bu program "Visual Studio Code" programında yazılmış olup bu İDE'de ve PyCharm IDE’sinde denenmiştir.
'''
print("Bu Program sizden aldığı boyuta göre alt alta olacak şekilde 'AHMET YILMAZ' ifadesinin harflerini tek tek yazdırır.\n")

boyut = int(input ("Boyutu Giriniz : "))

print("\n")

# A harfi
for i in range(boyut):
    for j in range(boyut):
        if i == 0 :  # İlk satırda mıyız ? 
            if (j == 0) | (j == (boyut - 1)): # İlk ve Son stündaki boşluklar.
                print (' ', end="")
            else :
                print ('*', end="")               
        elif i == int(boyut/2) :  # A'nın orta çizgisine geldiysek...
            print ('*', end="")   # i boyut/2 iken j döngü sayısı kadar yıldız yazacak.
        else :    
            if (j == 0) | (j == (boyut - 1)): # İlk ve Son stündaki yıldızlar.
                print ('*', end="")
            else :
                print (' ', end="") 
    print("\n", end="")

print("\n")

# H harfi
for i in range(boyut):
    for j in range(boyut):
        if i == 0 :  # İlk satırda mıyız ?
            if (j == 0) | (j == (boyut - 1)): # İlk ve Son stündaki yıldızlar.
                print ('*', end="")
            else :
                print (' ', end="")
        elif i == int(boyut/2) :  # H'nin orta çizgisine geldiysek..
            print ('*', end="")
        else : 
            if (j == 0) | (j == boyut - 1 ): # Diğer durumlardaki ilk ve Son stündaki yıldızlar.
                print('*', end="")
            else :
                print(' ', end="")
    print("\n", end="")

print("\n")

# M harfi
for i in range(boyut):
    for j in range(boyut):
        if (j == 0) | (j == (boyut-1)) : # M'nin ilk ve son stündaki yıldızlar.
            print ('*', end="")
        else :
            if (i > 0) & (i < (boyut/2)) : 
                if (j == i) | (j == (boyut-i-1)) : # i'nin değerinin gittikçe azalması ve denklemi sağlaması için (j == (boyut-i-1)) yazdım.
                    print ('*', end="")
                else :
                    print (' ', end="")
            else :
                print (' ', end="")   
    print("\n", end="")    

print("\n")

# E harfi 
for i in range(boyut):
    for j in range(boyut):
        if (i == 0) | (i == int(boyut/2)) | (i == boyut-1): # E'nin 0, (boyut/2) ve (boyut-1)'inci indisleri.
            print ('*', end="")
        else :
            if (j == 0) : 
                print ('*', end="")
            else :
                print (' ', end="")
    print("\n", end="")
            
print("\n")

# T harfi
for i in range(boyut):
    for j in range(boyut):
        if i == 0 :
            print ('*', end="")
        else :
            if (j == int(boyut/2)): 
                print ('*', end="")
            else :
                print (' ', end="")
    print("\n", end="")
        
print("\n \n")

# Y harfi 
for i in range(boyut):
    for j in range (boyut) :
        if ( i >= 0 ) & ( i < int(boyut/2)):     # Y'nin V kısmı.    
            if (j == i) | (j == (boyut-i-1)):   # V kısmının sağ ve soldaki kısımları için.
                print ('*', end="") 
            else :
                print (' ', end="")
        else :
            if (j == int(boyut/2)) :   # Y'nin I kısmı.
                print ('*', end="")
            else :
                print (' ', end="")
    print("\n", end="")

print ("\n")

# I harfi 
for i in range(boyut) : 
    for j in range(boyut) :
        if (i == 0) | (i == boyut -1 ): # İlk ve son satır karakter sayısı kadar yıldız.
            print ('*', end="")
        else : 
            if ( j == int(boyut/2)) : 
                print ('*', end="")
            else :
                print (' ', end="")
    print("\n", end="")

print ("\n")

# L harfi 
for i in range(boyut) : 
    for j in range(boyut) :
        if j == 0 : 
            print ('*', end="")
        else :
            if i == (boyut-1) :
                print ('*', end="")
            else :
                print ('', end="")
    print("\n", end="")

print("\n")

# M harfi
for i in range(boyut):
    for j in range(boyut):
        if (j == 0) | (j == (boyut-1)) :  # M'nin ilk ve son stündaki yıldızlar.
            print ('*', end="")
        else :
            if (i > 0) & (i < (boyut/2)) :
                if (j == i) | (j == (boyut-i-1)) : # i'nin değerinin gittikçe azalması ve denklemi sağlaması için (j == (boyut-i-1)) yazdım.
                    print ('*', end="")
                else :
                    print (' ', end="")
            else :
                print (' ', end="")   
    print("\n", end="") 

print("\n")

# A harfi
for i in range(boyut):
    for j in range(boyut):
        if i == 0 :  # İlk satırda mıyız ? 
            if (j == 0) | (j == (boyut - 1)): # İlk ve Son stündaki boşluklar.
                print (' ', end="")
            else :
                print ('*', end="")               
        elif i == int(boyut/2) :  # A'nın orta çizgisine geldiysek...
            print ('*', end="")   # i boyut/2 iken j döngü sayısı kadar yıldız yazacak.
        else :    
            if (j == 0) | (j == (boyut - 1)): # İlk ve Son stündaki yıldızlar.
                print ('*', end="")
            else :
                print (' ', end="") 
    print("\n", end="")

print("\n")

# Z harfi
for i in range(boyut) :
    for j in range(boyut) :
        if (i == 0) | (i == boyut-1) :
            print ('*', end="")
        else :
            if (j == (boyut-i-1)) :
                print ('*', end="")
            else :
                print (' ', end="")
    print("\n", end="")