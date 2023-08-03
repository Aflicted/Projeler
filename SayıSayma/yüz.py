import random
import time

print("Sayı tahmin oyununa hoş geldiniz!n 1-100 arasında bir sayı tahmin edin")
sayi = random.randint(1,100)
tahmin_hakki = 5

while True:
    tahmin = int(input("Tahmininiz: "))
    
    if tahmin == sayi:
        print("Sayı sorgulanıyor... ")
        time.sleep(1)
        print("Tebrikler! doğru bildiniz")

        devam=input("""tekrar oynamak ister misiniz?
        eğer oynamak isterseniz d/D tuşlayınız
        kapatmak isterseniz k/K tuşlayınız""")
        if devam=="d" or devam=="D":
            tahmin_hakki = 5
            continue
        else:
            print("byeee")
            break
        


    elif tahmin > sayi:
        print("Sayı sorgulanıyor... ")
        time.sleep(1)
        tahmin_hakki-=1
        print("Daha küçük bir sayı giriniz")
        print("Kalan tahmin hakkı: ",tahmin_hakki)

        devam=input("""tekrar oynamak ister misiniz?
        eğer oynamak isterseniz d/D tuşlayınız
        kapatmak isterseniz k/K tuşlayınız""")
        if devam=="d" or devam=="D":
            tahmin_hakki = 10
            continue
        else:
            print("byeee")
            break

        
    else:
        print("Sayı sorgulanıyor... ")
        time.sleep(1)
        tahmin_hakki -= 1
        print("Daha büyük bir sayı giriniz")
        print("Kalan tahmin hakkı: ", tahmin_hakki)
        
    if tahmin_hakki == 0:
        print("Tahmin hakkınız bitmiştir")
        print("Bilgisayarın tahmini: ",sayi)


        
        devam=input("""tekrar oynamak ister misiniz?
        eğer oynamak isterseniz d/D tuşlayınız
        kapatmak isterseniz k/K tuşlayınız""")
        if devam=="d" or devam=="D":
            tahmin_hakki = 5
            continue
        else:
            print("byeee")
            break
