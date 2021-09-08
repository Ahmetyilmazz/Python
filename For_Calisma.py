# 5'e 5 içi dolu ve içi boş kareler çizdiriniz. (yan yana çıktı olacak şekilde ve arada 5 karakter olacak şekilde.)

a = 5
n = 5 

for a in range(a):  
    print('*' * a)
    for n in range(n):  # Buradaki n global (en tepeye yazılan değer) değer değil, lokal(bölgesel) değişken olarak yorumlanıyor.
        print('-' * n + str(n)) # str burda n'in her satırdaki değerini gösterdi.
    
