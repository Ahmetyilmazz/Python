# // AHMET YILMAZ

print("Bu Program sizden aldigi boyuta göre Ahmet YILMAZ yazdirir. \n")

boyut = int(input ("Boyutu Giriniz : "))

print("\n")

# A harfi
for i in range(boyut):
    if i == 0 :  # İlk satırda mıyız ? 
        print(' ' + '*'*(boyut-2) + ' ') # boyuta -2 yazmamış olsaydık eğer boyut yerine boyut +2 yazmış olurdu.
    elif i == int(boyut/2) :  # A'nın orta çizgisine geldiysek...
        print ('*'*boyut)
    else : 
        print('*' + ' '*(boyut-2) + '*')

print("\n")

# H harfi
for i in range(boyut):
    if i == int(boyut/2) :  # H'nın orta çizgisine geldiysek...
        print ('*'*boyut)
    else : 
        print('*' + ' '*(boyut-2) + '*')

print("\n")

# M harfi
for i in range(boyut):
    if i == 0 :  # İlk satırda mıyız ? 
        print('*' + ' '*(boyut-2) + '*') 
    elif i < int(boyut/2) :  # M'nın orta çizgisine gelene kadar..
        print ('*' + ' '*(i-1) + '*' + ' '*(boyut-2*i-2) + '*' + ' '*(i-1) + '*')
    elif (i == int(boyut/2)) & ((boyut-3)%2 == 0): # M'nin ortası ve # boyuta -3 yazılmasının sebebi kalan boşluğun 2'ye göre bölünebilir olup olmadığı.
        print('*' + ' ' * int((boyut-3)/2) + '*' + ' ' * int((boyut-3)/2) + '*') # Boyut tekse yap, değilse yapma.
    else : 
        print('*' + ' '*(boyut-2) + '*')

print("\n")

# E harfi 
for i in range(boyut):
    if i == 0 :  # İlk satırda mıyız ? 
        print('*' * boyut) 
    elif i == int(boyut/2) :  # E'nın orta çizgisine geldiysek...
        print ('*' * boyut)
    elif i == (boyut-1) :   # Son satir
        print('*' * boyut)
    else : 
        print('*')

print("\n")

# T harfi
for i in range(boyut):
    if i == 0 :
        print('*' * boyut)
    else :  
        print(' ' * int(boyut/2) + '*')

print("\n\n")

# Y harfi 
for i in range(boyut):
    if i == 0 :  # İlk satırda mıyız ? 
        print(' '*(boyut-2)) 
    elif i < int(boyut/2) :  # Y'nın orta çizgisine gelene kadar..
        print (' '*(i-1) + '*' + ' '*(boyut-2*i-2) + '*' + ' '*(i-1))
    else :  
        print(' ' * int((boyut-3)/2) + '*')

print("\n")

# I harfi 
for i in range(boyut) : 
    if i == 0 :
        print('*' * boyut)
    elif i == (boyut-1) :
        print('*' * boyut)
    else :
       print(' ' * int(boyut/2) + '*')


print("\n")


# L harfi 
for i in range(boyut) : 
    if i == (boyut-1) :
        print('*' * boyut)
    else :
        print('*')

print("\n")

# M harfi 
for i in range(boyut):
    if i == 0 :  # İlk satırda mıyız ? 
        print('*' + ' '*(boyut-2) + '*') 
    elif i < int(boyut/2) :  # M'nın orta çizgisine gelene kadar..
        print ('*' + ' '*(i-1) + '*' + ' '*(boyut-2*i-2) + '*' + ' '*(i-1) + '*')
    elif (i == int(boyut/2)) & ((boyut-3)%2 == 0): # M'nin ortası ve (boyuta-3) yazılmasının sebebi kalan boşluğun 2'ye göre bölünebilir olup olmadığı.
        print('*' + ' ' * int((boyut-3)/2) + '*' + ' ' * int((boyut-3)/2) + '*') # Boyut tekse yap, değilse yapma.
    else : 
        print('*' + ' '*(boyut-2) + '*')

print("\n")

# A harfi 
for i in range(boyut):
    if i == 0 :  # İlk satırda mıyız ? 
        print(' ' + '*'*(boyut-2) + ' ') # boyuta -2 yazmamış olsaydık eğer boyut yerine boyut +2 yazmış olurdu.
    elif i == int(boyut/2) :  # A'nın orta çizgisine geldiysek...
        print ('*'*boyut)
    else : 
        print('*' + ' '*(boyut-2) + '*')

print("\n")

# Z harfi
for i in range(boyut):
    if (i==0) | (i==boyut-1):  # İlk satırda ve ve son satırda mıyız ?
        print('*' * boyut)     # Boyut kadar * bastır.
    else :
        print(' ' * (boyut-i-1) + '*')  # i = 1 için; boyut-2 tane boşluk var. 


'''
for i in range(1,boyut+1):
    for j in range(1,boyut+1):
        if i==1 or i==boyut or i + j == boyut+1:
            print('*', end=" ")
        else:
            print(" ", end=" ")
    print()  
''' 