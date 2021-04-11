print("sisteme kayıtlı değilseniz lütfen kayıt olunuz !")
kullanıcılar={} # dictionary list 

number=int(input("kullanıcı num : "))
name=input("kullanıcı adı : ")
pasword=input("şifrenizi oluşturun : ")
print(f"{number} {name} kullanıcı adıyla kayıt oldunuz !! \n  ")

kullanıcılar.update({

    'number':{ 
        'name': name,
        'pasword': pasword,
    }
})
print(kullanıcılar)
print(kullanıcılar['number']['name'])


print("sisteme giriş için hoşgeldiniz !  \n lütfen bilgilerinizi giriniz : ")
kullanıcı_adı=input("kullanıcı adınızı giriniz ! : ")
sifre=input("sifrenizi giriniz: ")
if (  (kullanıcı_adı ==kullanıcılar['number']['name'] ) and  (sifre==kullanıcılar['number']['pasword'] )  ):
    print("sisteme giriş yaptınız ! ")

else:
    print("kullanıcı adı ve ya sifre hatalı ! ")   