
# Programmer : Ahmet YILMAZ 

import random 
# print (random.randint(1, 10))

print ("Amiral Batti Oyununa Hoş Geldiniz..")
print("\n")

# Oyun_Alani

minimum_oyun_alani_buyuklugu = 10 
oyun_alani_buyuklugu = 0
# Başlangıcı a, sonu b, doğrultusu da c ise; gemi = [a,b,c] olarak gösterilsin. c = 'D'(dikey), 'Y' (yatay) değerlerini alacaktır.
gemi_1 = [[0,0],[0,0]] # Konumu ve Doğrultusu gerekli. 
gemi_2 = [[1,0],[1,1]]
gemi_3 = [[2,0],[2,2]]
gemi_4 = [[3,0],[3,3]]


while 1:  
    
    while (oyun_alani_buyuklugu < minimum_oyun_alani_buyuklugu):
        oyun_alani_buyuklugu = int(input("Oyun Alanını Giriniz (Min.10): "))

        if oyun_alani_buyuklugu >= minimum_oyun_alani_buyuklugu :
            print("Oyun Alanınız : " + str(oyun_alani_buyuklugu) + "x" + str(oyun_alani_buyuklugu))
            continue
        else:
            print("Oyun alanınız Min.10 olmalıdır.") 
    oyun_alani = [["?"]*oyun_alani_buyuklugu for _ in range(oyun_alani_buyuklugu)] #list([list("?" * oyun_alani_buyuklugu)] *oyun_alani_buyuklugu) #Oyun_Alani KAYNAK: https://stackoverflow.com/questions/2739552/2d-list-has-weird-behavor-when-trying-to-modify-a-single-value
    
    for i in range(oyun_alani_buyuklugu):
        print(oyun_alani [i])     

    print()

    # Gemi_1 
    gemi_1 [0][0] = (random.randint(0,oyun_alani_buyuklugu)) 
    gemi_1 [0][1] = (random.randint(0,oyun_alani_buyuklugu)) 

    Xa = gemi_1 [0][0]
    Ya = gemi_1 [0][1]
    n = 1
    XbYb_olasiliklari= ([Xa-(n-1),Ya], [Xa, Ya + (n-1)], [Xa + (n-1),Ya], [Xa, Ya - (n-1)]) # Hepsinde ortak formül.
    '''
    # gemi_1 de böyle bir koşula gerek olmadığı için yorum satırı olarak yazılmıştır.

    xbyblistesi = list(XbYb_olasiliklari)

    for xy in xbyblistesi:        # xy yi xbyb içinde nokta nokta gez.
        if (0 > xy[0]) | (oyun_alani_buyuklugu < xy[0]) : 
            xbyblistesi.remove( xy ) # Tuple listeye çevir, aralıkta olmayan noktaları sil. Listeyi tekrar tupleye çevir.
        elif (0 > xy[1]) | (oyun_alani_buyuklugu < xy[1]):
            xbyblistesi.remove( xy ) # Tuple listeye çevir, aralıkta olmayan noktaları sil. Listeyi tekrar tupleye çevir.
    '''
    XbYb = XbYb_olasiliklari [(random.randint(0,len(XbYb_olasiliklari)-1))]  # Random olasılık seçimi. # xbyblistesi
    gemi_1 [1][0] = XbYb[0] 
    gemi_1 [1][1] = XbYb[1] 
    print (gemi_1) #Test edildi.

    gemi1_noktalistesi = gemi_1
    #print(gemi1_noktalistesi ) # Test

    while 1 :

        # Gemi_2
        gemi_2 [0][0] = (random.randint(0,oyun_alani_buyuklugu))
        gemi_2 [0][1] = (random.randint(0,oyun_alani_buyuklugu))

        Xa = gemi_2 [0][0]
        Ya = gemi_2 [0][1]
        n = 2
        XbYb_olasiliklari= ([Xa-(n-1),Ya], [Xa, Ya + (n-1)], [Xa + (n-1),Ya], [Xa, Ya - (n-1)]) # Hepsinde ortak formül.
        xbyblistesi = list(XbYb_olasiliklari)

        for xy in xbyblistesi:        # xy yi xbyb içinde nokta nokta gez.
            if (0 > xy[0]) | (oyun_alani_buyuklugu < xy[0]) : 
                xbyblistesi.remove( xy ) # Tuple listeye çevir, aralıkta olmayan noktaları sil. Listeyi tekrar tupleye çevir.
            elif (0 > xy[1]) | (oyun_alani_buyuklugu < xy[1]):
                xbyblistesi.remove( xy ) # Tuple listeye çevir, aralıkta olmayan noktaları sil. Listeyi tekrar tupleye çevir.

        XbYb = xbyblistesi [(random.randint(0,len(xbyblistesi)-1))]  # Random olasılık seçimi
        gemi_2 [1][0] = XbYb[0] 
        gemi_2 [1][1] = XbYb[1]   
        print (gemi_2) #Test edildi.

        if gemi_2 in gemi1_noktalistesi:
            break
        else:
            print("OLDU-1") 
        break
    
    gemi2_noktalistesi = gemi_2
    #print(gemi2_noktalistesi) # Test.

    while 1:

        # Gemi_3
        gemi_3 [0][0] = (random.randint(0,oyun_alani_buyuklugu))
        gemi_3 [0][1] = (random.randint(0,oyun_alani_buyuklugu))

        Xa = gemi_3 [0][0]
        Ya = gemi_3 [0][1]
        n = 3
        XbYb_olasiliklari= ([Xa-(n-1),Ya], [Xa, Ya + (n-1)], [Xa + (n-1),Ya], [Xa, Ya - (n-1)]) # Hepsinde ortak formül yani Xa sı ve Ya sına göre olasılıklar.
        xbyblistesi = list(XbYb_olasiliklari)

        for xy in xbyblistesi:        # xy yi xbyb içinde nokta nokta gez.
            if (0 > xy[0]) | (oyun_alani_buyuklugu < xy[0]) : 
                xbyblistesi.remove( xy ) # Tuple listeye çevir, aralıkta olmayan noktaları sil. Listeyi tekrar tupleye çevir.
            elif (0 > xy[1]) | (oyun_alani_buyuklugu < xy[1]):
                xbyblistesi.remove( xy ) # Tuple listeye çevir, aralıkta olmayan noktaları sil. Listeyi tekrar tupleye çevir.

        XbYb = xbyblistesi [(random.randint(0,len(xbyblistesi)-1))]  # Olasılıklardan random seçim.
        gemi_3 [1][0] = XbYb[0] 
        gemi_3 [1][1] = XbYb[1]  
        print(gemi_3) #Test edildi.

        if gemi_3 in gemi1_noktalistesi :
            break
        elif gemi_3 in gemi2_noktalistesi:
            break
        else:
            print("OLDU-2")

        break
    
    gemi3_noktalistesi = gemi_3 
    #print(gemi3_noktalistesi) # Test.

    while 1:

        # Gemi_4
        gemi_4 [0][0] = (random.randint(0,oyun_alani_buyuklugu))
        gemi_4 [0][1] = (random.randint(0,oyun_alani_buyuklugu))

        Xa = gemi_4 [0][0]
        Ya = gemi_4 [0][1]
        n = 4
        XbYb_olasiliklari= ([Xa-(n-1),Ya], [Xa, Ya + (n-1)], [Xa + (n-1),Ya], [Xa, Ya - (n-1)]) # Hepsinde ortak formül yani Xa sı ve Ya sına göre olasılıklar.
        xbyblistesi = list(XbYb_olasiliklari)

        for xy in xbyblistesi:        # xy yi xbyb içinde nokta nokta gez.
            if (0 > xy[0]) | (oyun_alani_buyuklugu < xy[0]) : 
                xbyblistesi.remove( xy ) # Tuple listeye çevir, aralıkta olmayan noktaları sil. Listeyi tekrar tupleye çevir.
            elif (0 > xy[1]) | (oyun_alani_buyuklugu < xy[1]):
                xbyblistesi.remove( xy ) # Tuple listeye çevir, aralıkta olmayan noktaları sil. Listeyi tekrar tupleye çevir.
            
        XbYb = xbyblistesi [(random.randint(0,len(xbyblistesi)-1))]  # Olasılıklardan random seçim.
        gemi_4 [1][0] = XbYb[0] 
        gemi_4 [1][1] = XbYb[1]  
        print(gemi_4) #Test edildi.

        if gemi_4 in gemi1_noktalistesi:
            break
        elif gemi_4 in gemi2_noktalistesi:
            break
        elif gemi_4 in gemi3_noktalistesi:
            break
        else:
            print("OLDU-3")
            
        break

    
    # Gemileri_Haritaya_Yerleştirme    
    oyun_alani[ gemi_1[0][0] ][ gemi_1[0][1] ] = "O"
    oyun_alani[ gemi_1[1][0] ][ gemi_1[1][1] ] = "O"
    oyun_alani[ gemi_2[0][0] ][ gemi_2[0][1] ] = "O"
    oyun_alani[ gemi_2[1][0] ][ gemi_2[1][1] ] = "O"
    oyun_alani[ gemi_3[0][0] ][ gemi_3[0][1] ] = "O"
    oyun_alani[ gemi_3[1][0] ][ gemi_3[1][1] ] = "O"
    oyun_alani[ gemi_4[0][0] ][ gemi_4[0][1] ] = "O"
    oyun_alani[ gemi_4[1][0] ][ gemi_4[1][1] ] = "O"
    
    
    for i in range(oyun_alani_buyuklugu):
        print(oyun_alani [i])  
    









    '''
    #Mod_Eklentisi
    while 1:

        secim = int(input("Mod Seçiniz (1/2): "))

        if secim == 1:
            print("Gizli_Mod Seçilmiştir.")   # gizli mod kısmı burayla 
        
        elif secim == 2:
            print("Açık Mod Seçilmiştir.")    # acik mod kısmı buranın devamıyla alakası sanırım.

        else :
            print("Sadece İki Moddan Birini Seçebilirsiniz.")
            continue
        
        break
    
    atis_secimi = int(input("Vurmak istediğiniz noktayı yazınız: "))
    if atis_secimi == gemiler :
        print("Tebrikler 1 gemi vurdunuz !")
    else:
        print("AAA")    
    '''
    

    
    break