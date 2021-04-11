#SİSTEME GİRİŞ VE KAYIT OLMA PROJESİ 

kayıt_ol=input("sisteme kayıtlı değilsiniz \nlütfen kayıt olunuz! kayıt için t harfi giriniz")
if ((kayıt_ol=='t' ) or (kayıt_ol=='T')) :
    kayıt_kullanıcı_adı=input("kullanıcı adınız oluşturunuz!!")
    kayıt_parola=int(input("parolanızı oluşturunuz \n UYARI : parola sadece rakamlardan oluşabilir !"))
    sistemGiris=input(" şimdi sisteme giriş yapanilirsiniz giriş için e veya E giriniz e/h: ")
if (sistemGiris=="e" or sistemGiris=="E"):
    kullanıcı_adı =input("kullanıcı adınızı giriniz ")
    parola=int(input("lütfen parola bilginizi giriniz "))
    if(kullanıcı_adı==kayıt_kullanıcı_adı)and(parola==kayıt_parola):
        print("kullanıcı adı ve şifre doğru sisteme giriş yaptınız")
    elif(kullanıcı_adı!=kayıt_kullanıcı_adı ):
        print("kullanıcı adı  hatalı lütfen tekrar deneyiniz!!")
    elif (parola!=kayıt_parola):
        print("parola hatalı lütfne kontrol ediniz !!")

else: #(kayıt_ol!='t' or kayıt_ol!='T')
    print("sistemden çıkış yapınız !!")
