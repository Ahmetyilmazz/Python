# 5'e 5 içi dolu ve içi boş kareler çizdiriniz. 

print("Bu program 5'e 5 içi dolu kare çizdirir. \n")



a=5
for i in range(a):
    print ('*' * a)

print("\t \t")

n = 5
print('*' * n)
for i in range(n-2):
    print ('*' + ' ' * (n-2) + '*')
print('*' * n)