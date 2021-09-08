

# Programmer : Ahmet YILMAZ 

while 1 :

    # Vize #
    while 1 :
        vize_sayisi = int(input("Lütfen Vize Sayisini Giriniz : "))

        if vize_sayisi >= 3 :
            break
        else :
            print("Lütfen en az 3 Vize sayisi giriniz : ")
            continue

    vize_katki = float(input("Lütfen Vizenin Katkı Oranını Giriniz (0.4 veya 0.6 olacak şekilde) : "))
    vize_son = 0
    for i in range(vize_sayisi) :
        puan = int(input("{}. Vize puanınızı giriniz : ".format( i + 1)))
        vize_son += puan

    vize = (vize_son*vize_katki)
    print("Ortalamaya etki eden notunuz = ",vize)

    print("\n")

    # QUİZ #
    while 1 :
        quiz_sayisi = int(input("Lütfen QUİZ sayısını giriniz : "))

        if quiz_sayisi >= 3 :
            break
        else :
            print("Lütfen en az 3 Quiz sayisi giriniz : ")
            continue

    quizin_katki = float(input("Lütfen Quizin Katkı Oranını Giriniz (0.4 veya 0.6 olacak şekilde) : "))
    quiz_son = 0 
    for i in range(quiz_sayisi) :
        puan = int(input("{}. Quiz puanınızı giriniz : ".format( i + 1)))
        quiz_son += puan

    quiz = (quiz_son*quizin_katki)
    print("Ortalamaya etki eden Quiz notunuz = ",quiz)

    print("\n")

    # ÖDEV #
    while 1 :
        odev_sayisi = int(input("Lütfen Odev sayısını giriniz : "))

        if quiz_sayisi >= 3 :
            break
        else :
            print("Lütfen en az 3 Odev sayisi giriniz : ")
            continue

    odevin_katki = float(input("Lütfen Odevin Katkı Oranını Giriniz (0.4 veya 0.6 olacak şekilde) : "))
    odev_son = 0 
    for i in range(odev_sayisi) :
        puan = int(input("{}. Quiz puanınızı giriniz : ".format( i + 1)))
        odev_son += puan

    odev = (odev_son*quizin_katki)
    print("Ortalamaya etki eden Quiz notunuz = ",odev)

    print("\n")

    # FİNAL # 
    while 1 :
        final_sayisi = int(input("Lütfen Final sayisini giriniz : "))
        
        if final_sayisi == 1 :
            break
        else :
            print("Sadece 1 Final Sınavı Olmalıdır. ")
            continue
    
    finalin_katki = float(input("Lütfen Finalin Katkı oranını giriniz (0.4 veya 0.6 olacak şekilde) : "))
    final_son = 0
    for i in range(final_sayisi) :
        puan = int(input("{}. Final puanınızı giriniz : ".format( i + 1)))
        final_son += puan

    final = (final_son*finalin_katki)
    print("Ortalamaya etki eden Final notunuz = ",final)
    
    print("\n")

    ortalama = (vize + quiz + odev + final)
    print("Ders Ortalamanız = ",ortalama)

    if ortalama > 100 :
        print("Ortalamanız 100'ü geçemez, Lütfen notlarınızı doğru girdiğinize emin olunuz !!!")
        continue