para=1200
t=123


for i in range (0,3):
    sifre=int(input("şifre gir"))
    if t==sifre:
        print("tebrikler giriş yaptınız")
        break
    else:
        print("şifre yanlış")
    
else:
    print("kartınız bloke oldu")

print("para çekmek için 1 \n para yatırmak için 2 \n parayı görmek için 3 \n çıkmak için 4")

for i in range(0,999):
        girilen=int(input("seçiminiz"))
        if girilen==1:
            çek=int(input("çekmek istediğiniz miktari giriniz"))
            if çek>para:
                print("Bakiyenizden küçük bir miktar çekiniz, bakiyeniz:",para)
            else:
                para=para-çek
                print("bakiyeniz",para)
        elif girilen==2:
            yatır=int(input("yatırmak istediğiniz miktarı giriniz"))
            para=para+yatır
            print("bakiyeniz",para)
        elif girilen==3:
            print(para)
        elif girilen==4:
            break
