
'''
02.06.2020
// AHMET YILMAZ //
// Odev = FINAL_Amiral_Batti
'''

import random

print ("Amiral Batti Oyununa Hoş Geldiniz..")
print("\n")


while 1:
   
    # Oyun_Alani
    minimum_oyun_alani_buyuklugu = 10 
    oyun_alani_buyuklugu = 0
    # Başlangıcı a, sonu b, doğrultusu da c ise; gemi = [a,b,c] olarak gösterilsin. c = 'D'(dikey), 'Y' (yatay) değerlerini alacaktır.
    gemi_1 = [[0,0],[0,0]] # Konumu ve Doğrultusu gerekli. 
    gemi_2 = [[1,0],[1,1]]
    gemi_3 = [[2,0],[2,2]]
    gemi_4 = [[3,0],[3,3]]
    
    gemi1_noktalistesi = []
    gemi2_noktalistesi = []
    gemi3_noktalistesi = []
    gemi4_noktalistesi = []
    
    
    
    
    while (oyun_alani_buyuklugu < minimum_oyun_alani_buyuklugu):
        oyun_alani_buyuklugu = int(input("Oyun Alanını Giriniz (Min.10): "))

        if oyun_alani_buyuklugu >= minimum_oyun_alani_buyuklugu :
            print("Oyun Alanınız : " + str(oyun_alani_buyuklugu) + "x" + str(oyun_alani_buyuklugu))
            continue
        else:
            print("Oyun alanınız Min.10 olmalıdır.") 
    
    oyun_alani =[[" ? "]*oyun_alani_buyuklugu for _ in range(oyun_alani_buyuklugu)] #list([list("?" * oyun_alani_buyuklugu)] *oyun_alani_buyuklugu) #Oyun_Alani KAYNAK: https://stackoverflow.com/questions/2739552/2d-list-has-weird-behavor-when-trying-to-modify-a-single-value
    oyun_alani_gizli = [[" ? "]*oyun_alani_buyuklugu for _ in range(oyun_alani_buyuklugu)]

    print("Lütfen Oynamak İstediğiniz Modu Seçiniz")
    print ("---------------------------------------")
    print ("1- Gizli Mod ")
    print ("2- Açık Mod ")

    secim = int(input("Mod Seçiniz (1/2): "))

    
    print()

    # Gemi_1 
    gemi_1 [0][0] = (random.randint(0,oyun_alani_buyuklugu-1)) 
    gemi_1 [0][1] = (random.randint(0,oyun_alani_buyuklugu-1)) 

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
    #print (gemi_1) #Test edildi.
    
    gemi1_noktalistesi = gemi_1[0] # A ile B aynı oldukları için sadece A yazıldı.
    #print("Gemi1 nokta listesi: "  + str(gemi1_noktalistesi)) # Test

    while 1 :

        # Gemi_2
        gemi_2 [0][0] = (random.randint(0,oyun_alani_buyuklugu-1))
        gemi_2 [0][1] = (random.randint(0,oyun_alani_buyuklugu-1))

        Xa = gemi_2 [0][0]
        Ya = gemi_2 [0][1]
        n = 2
        XbYb_olasiliklari= ([Xa-(n-1),Ya], [Xa, Ya + (n-1)], [Xa + (n-1),Ya], [Xa, Ya - (n-1)]) # Hepsinde ortak formül.
        xbyblistesi = list(XbYb_olasiliklari)

        for xy in xbyblistesi:        # xy yi xbyb içinde nokta nokta gez.
            if int(xy[0]) < 0:
                xbyblistesi.remove( xy ) # Tuple listeye çevir, aralıkta olmayan noktaları sil. Listeyi tekrar tupleye çevir.
            elif int(xy[0]) >= oyun_alani_buyuklugu  : 
                xbyblistesi.remove( xy ) # Tuple listeye çevir, aralıkta olmayan noktaları sil. Listeyi tekrar tupleye çevir.

            if int(xy[1]) < 0:
                xbyblistesi.remove( xy ) # Tuple listeye çevir, aralıkta olmayan noktaları sil. Listeyi tekrar tupleye çevir.
            elif int(xy[1]) >= oyun_alani_buyuklugu  : 
                xbyblistesi.remove( xy ) # Tuple listeye çevir, aralıkta olmayan noktaları sil. Listeyi tekrar tupleye çevir.


        XbYb = xbyblistesi [(random.randint(0,len(xbyblistesi)-1))]  # Random olasılık seçimi
        gemi_2 [1][0] = XbYb[0] 
        gemi_2 [1][1] = XbYb[1]   
        
        gemi2_noktalistesi = gemi_2
        #print("Gemi2 nokta listesi: " + str(gemi2_noktalistesi)) # Test

        kesisim_varmı = 0 #kesişim başlangıçta yok olsun.
        for gemi in gemi1_noktalistesi:
            if gemi in gemi2_noktalistesi:
                kesisim_varmı = 1

        if kesisim_varmı == 0:
            break

    #print (gemi_2) #Test edildi.

    while 1:

        # Gemi_3
        gemi_3 [0][0] = (random.randint(0,oyun_alani_buyuklugu-1))
        gemi_3 [0][1] = (random.randint(0,oyun_alani_buyuklugu-1))

        Xa = gemi_3 [0][0]
        Ya = gemi_3 [0][1]
        n = 3
        XbYb_olasiliklari= ([Xa-(n-1),Ya], [Xa, Ya + (n-1)], [Xa + (n-1),Ya], [Xa, Ya - (n-1)]) # Hepsinde ortak formül yani Xa sı ve Ya sına göre olasılıklar.
        xbyblistesi = list(XbYb_olasiliklari)

        for xy in xbyblistesi:        # xy yi xbyb içinde nokta nokta gez.
            if int(xy[0]) < 0:
                xbyblistesi.remove( xy ) # Tuple listeye çevir, aralıkta olmayan noktaları sil. Listeyi tekrar tupleye çevir.
            elif int(xy[0]) >= oyun_alani_buyuklugu  : 
                xbyblistesi.remove( xy ) # Tuple listeye çevir, aralıkta olmayan noktaları sil. Listeyi tekrar tupleye çevir.

            if int(xy[1]) < 0:
                xbyblistesi.remove( xy ) # Tuple listeye çevir, aralıkta olmayan noktaları sil. Listeyi tekrar tupleye çevir.
            elif int(xy[1]) >= oyun_alani_buyuklugu  : 
                xbyblistesi.remove( xy ) # Tuple listeye çevir, aralıkta olmayan noktaları sil. Listeyi tekrar tupleye çevir.


        XbYb = xbyblistesi [(random.randint(0,len(xbyblistesi)-1))]  # Olasılıklardan random seçim.
        gemi_3 [1][0] = XbYb[0] 
        gemi_3 [1][1] = XbYb[1]  
       
        gemi3_noktalistesi = []        
        if gemi_3[0][1] < gemi_3[1][1]: # range içine önce küçük olan yazılması gerektiğinden eklendi. x değişmediği durum - gemi yatay
            for i in range(gemi_3[0][1] , gemi_3[1][1]):
                gemi3_noktalistesi.append([gemi_3[0][0],i])
            gemi3_noktalistesi.append([gemi_3[0][0],gemi_3[1][1]])
        elif  gemi_3[0][1] > gemi_3[1][1]:
            for i in range(gemi_3[1][1] , gemi_3[0][1]):
                gemi3_noktalistesi.append([gemi_3[0][0],i])
            gemi3_noktalistesi.append([gemi_3[0][0],gemi_3[0][1]])
        else: # y değişmediği durum - gemi dikey
            if gemi_3[0][0] < gemi_3[1][0]:# range içine önce küçük olan yazılması gerektiğinden eklendi. 
                for i in range(gemi_3[0][0] , gemi_3[1][0]):
                    gemi3_noktalistesi.append([i,gemi_3[0][1]])
                gemi3_noktalistesi.append([gemi_3[1][0],gemi_3[0][1]])
            else:
                for i in range(gemi_3[1][0] , gemi_3[0][0]):
                    gemi3_noktalistesi.append([i,gemi_3[0][1]])
                gemi3_noktalistesi.append([gemi_3[0][0],gemi_3[0][1]])
            
        #print("Gemi3 nokta listesi: " + str(gemi3_noktalistesi)) # Test

        kesisim_varmı = 0 #kesişim başlangıçta yok olsun.
        for gemi in gemi1_noktalistesi:
            if gemi in gemi3_noktalistesi:
                kesisim_varmı = 1

        for gemi in gemi2_noktalistesi:
            if gemi in gemi3_noktalistesi:
                kesisim_varmı = 1

        if kesisim_varmı == 0:
            break

    #print("Gemi 3 oluşturuldu.") 
    #print(gemi_3)

    
    while 1:

        # Gemi_4
        gemi_4 [0][0] = (random.randint(0,oyun_alani_buyuklugu-1))
        gemi_4 [0][1] = (random.randint(0,oyun_alani_buyuklugu-1))

        Xa = gemi_4 [0][0]
        Ya = gemi_4 [0][1]
        n = 4
        XbYb_olasiliklari= ([Xa-(n-1),Ya], [Xa, Ya + (n-1)], [Xa + (n-1),Ya], [Xa, Ya - (n-1)]) # Hepsinde ortak formül yani Xa sı ve Ya sına göre olasılıklar.
        xbyblistesi = list(XbYb_olasiliklari)

        #print("gemi4 b nokta olasılık : " + str(xbyblistesi))
        for xy in xbyblistesi:        # xy yi xbyb içinde nokta nokta gez.
            if int(xy[0]) < 0:
                xbyblistesi.remove( xy ) # Tuple listeye çevir, aralıkta olmayan noktaları sil. Listeyi tekrar tupleye çevir.
            elif int(xy[0]) >= oyun_alani_buyuklugu  : 
                xbyblistesi.remove( xy ) # Tuple listeye çevir, aralıkta olmayan noktaları sil. Listeyi tekrar tupleye çevir.

            if int(xy[1]) < 0:
                xbyblistesi.remove( xy ) # Tuple listeye çevir, aralıkta olmayan noktaları sil. Listeyi tekrar tupleye çevir.
            elif int(xy[1]) >= oyun_alani_buyuklugu  : 
                xbyblistesi.remove( xy ) # Tuple listeye çevir, aralıkta olmayan noktaları sil. Listeyi tekrar tupleye çevir.

        #print("gemi4 b nokta olasılık kontrol edilmiş: " + str(xbyblistesi))

        XbYb = xbyblistesi [(random.randint(0,len(xbyblistesi)-1))]  # Olasılıklardan random seçim.
        gemi_4 [1][0] = XbYb[0] 
        gemi_4 [1][1] = XbYb[1]  


        gemi4_noktalistesi = []        
        if gemi_4[0][1] < gemi_4[1][1]: # range içine önce küçük olan yazılması gerektiğinden eklendi. x değişmediği durum - gemi yatay
            for i in range(gemi_4[0][1] , gemi_4[1][1]):
                gemi4_noktalistesi.append([gemi_4[0][0],i])
            gemi4_noktalistesi.append([gemi_4[0][0],gemi_4[1][1]])
        elif  gemi_4[0][1] > gemi_4[1][1]:
            for i in range(gemi_4[1][1] , gemi_4[0][1]):
                gemi4_noktalistesi.append([gemi_4[0][0],i])
            gemi4_noktalistesi.append([gemi_4[0][0],gemi_4[0][1]])
        else: # y değişmediği durum - gemi dikey
            if gemi_4[0][0] < gemi_4[1][0]:# range içine önce küçük olan yazılması gerektiğinden eklendi. 
                for i in range(gemi_4[0][0] , gemi_4[1][0]):
                    gemi4_noktalistesi.append([i,gemi_4[0][1]])
                gemi4_noktalistesi.append([gemi_4[1][0],gemi_4[0][1]])
            else:
                for i in range(gemi_4[1][0] , gemi_4[0][0]):
                    gemi4_noktalistesi.append([i,gemi_4[0][1]])
                gemi4_noktalistesi.append([gemi_4[0][0],gemi_4[0][1]])
            
        #print("Gemi4 nokta listesi: " + str(gemi4_noktalistesi)) # Test

        kesisim_varmı = 0 #kesişim başlangıçta yok olsun.
        for gemi in gemi1_noktalistesi:
            if gemi in gemi4_noktalistesi:
                kesisim_varmı = 1
        for gemi in gemi2_noktalistesi:
            if gemi in gemi4_noktalistesi:
                kesisim_varmı = 1
        for gemi in gemi3_noktalistesi:
            if gemi in gemi4_noktalistesi:
                kesisim_varmı = 1

        if kesisim_varmı == 0:
            break 

    #print("Gemi 4 oluşturuldu.") 
    #print(gemi_4)
    
    #Gemileri_Haritaya_Yerleştirme
    # Gemi uçları yerleştirme    
    oyun_alani[ gemi_1[0][0] ][ gemi_1[0][1] ] = " O "
    oyun_alani[ gemi_1[1][0] ][ gemi_1[1][1] ] = " O "

    oyun_alani[ gemi_2[0][0] ][ gemi_2[0][1] ] = " o "
    oyun_alani[ gemi_2[1][0] ][ gemi_2[1][1] ] = " O "

    oyun_alani[ gemi_3[0][0] ][ gemi_3[0][1] ] = " o "
    oyun_alani[ gemi3_noktalistesi[1][0]][gemi3_noktalistesi[1][1]] = " O "
    oyun_alani[ gemi_3[1][0] ][ gemi_3[1][1] ] = " o "

    oyun_alani[ gemi_4[0][0] ][ gemi_4[0][1] ] = " o "
    oyun_alani[ gemi4_noktalistesi[1][0]][gemi4_noktalistesi[1][1]] = " O "
    oyun_alani[ gemi4_noktalistesi[2][0]][gemi4_noktalistesi[2][1]] = " O "
    oyun_alani[ gemi_4[1][0] ][ gemi_4[1][1] ] = " o "
    

    if secim == 1:
        print("Gizli_Modda Oyun Başladı...")
        print("-" * (7*oyun_alani_buyuklugu))
        for i in range(oyun_alani_buyuklugu):
            print(oyun_alani_gizli[i])
        print("-" * (7*oyun_alani_buyuklugu))
    elif secim == 2:
        print("Acik_Modda Oyun Başladı...")
        print("-" * (7*oyun_alani_buyuklugu))
        for i in range(oyun_alani_buyuklugu):
            print(oyun_alani[i])
        print("-" * (7*oyun_alani_buyuklugu))
    else :
        print("Sadece İki Moddan Birini Seçebilirsiniz...")

        
    '''
    for i in range(oyun_alani_buyuklugu): # oyun alanı ekrana yazdırma 
        print(oyun_alani [i])  
    '''
    print()

    oyuncu_atis_hakki = (oyun_alani_buyuklugu*oyun_alani_buyuklugu)//3  # // kullanılmasının sebebi float bir değişken olduğunda tam sayı kısmı alması.
    oyuncu_puani = oyuncu_atis_hakki
    #print(oyuncu_atis_hakki)

    for i in range(0,oyuncu_atis_hakki):

        atis_x = int(input("Vurmak İstediğiniz Noktanın x Koordinatını Yazınız: "))
        atis_y = int(input("Vurmak İstediğiniz Noktanın y Koordinatını Yazınız: "))
        oyuncu_puani -= 1 

        if (atis_x < 0) | (atis_x >= oyun_alani_buyuklugu):
            print("Lütfen Oyun Alanı İçinde Bir Nokta Giriniz !!!")
        elif (atis_y < 0) | (atis_y >= oyun_alani_buyuklugu):
            print("Lütfen Oyun Alanı İçinde Bir Nokta Giriniz !!!")
        else:
            if (oyun_alani[atis_x][atis_y] == " O ") | (oyun_alani[atis_x][atis_y] == " o ") :
                print("==> Tebrikler Bir Gemi Vurdunuz ! ") # Geminin Bütün Bölümleri vurulduysa Tebrikler bir gemi batırdınız mesajı da verilecek.
                oyun_alani[atis_x][atis_y] = " X "
                oyun_alani_gizli[atis_x][atis_y] = " X "
                batirma_kontrol = 1 # İlk durumda batmış olsun.
                '''
                for xy in gemi1_noktalistesi:
                    if (oyun_alani[ int(xy[0]) ][ int(xy[1]) ] == " O ") | (oyun_alani[ int(xy[0]) ][ int(xy[1]) ] == " o ") :
                        batirma_kontrol = 0 
                if batirma_kontrol == 1:
                    print("Tebrikler Bir Gemi Batırdınız ! - (Gemi_1)")

                batirma_kontrol = 1 # İlk durumda batmış olsun.
                for xy in gemi2_noktalistesi:
                    if (oyun_alani[ int(xy[0]) ][ int(xy[1]) ] == " O ") | (oyun_alani[ int(xy[0]) ][ int(xy[1]) ] == " o ") :
                        batirma_kontrol = 0 
                if batirma_kontrol == 1:
                    print("Tebrikler Bir Gemi Batırdınız ! - (Gemi_2)")
                '''
            elif (oyun_alani[atis_x][atis_y] == " X ") :
                print("Aynı Noktaya Birden Fazla Atış Yapamazsınız. Lütfen Başka Bir Nokta Belirtiniz.")


            if (oyun_alani[atis_x][atis_y] == " ? "):
                print("==> Maalesef İsabet Edemediniz.")
                oyun_alani[atis_x][atis_y] = " * "
                oyun_alani_gizli[atis_x][atis_y] = " * "

            elif (oyun_alani[atis_x][atis_y] == " * "):
                print("Aynı Noktaya Birden Fazla Atış Yapamazsınız. Lütfen Başka Bir Nokta Belirtiniz.")
                

        
        
        if secim == 1:
            print("-" * (7*oyun_alani_buyuklugu))
            for i in range(oyun_alani_buyuklugu):
                print(oyun_alani_gizli[i])
            print("-" * (7*oyun_alani_buyuklugu))
        elif secim == 2:
            print("-" * (7*oyun_alani_buyuklugu))
            for i in range(oyun_alani_buyuklugu):
                print(oyun_alani[i])
            print("-" * (7*oyun_alani_buyuklugu))
            
     
    
                 
                
        
    print("Puanınız: " + str(oyuncu_puani))

    yeni_oyun = input("Tekrar Oynamak için R ye basınız..")
    if yeni_oyun != "R" :
        break
        


