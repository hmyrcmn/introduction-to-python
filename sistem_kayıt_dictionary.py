want_record=input("sisteme kayıt olmak istiyormusunuz  E/H: ")
kullanıcılar={} # dictionary list 

if (want_record=='e' or want_record=='E'):
    number=(input("kullanıcı num : "))
    name=input("kullanıcı adı : ")
    pasword=input("şifrenizi oluşturun : ")
    print(f"{number} {name} kullanıcı adıyla kayıt oldunuz !! \n  ")

    kullanıcılar.update({

        'number':{ 
            'name': name,
            'pasword': pasword,
        }
    })
    print("sisteme giriş için hoşgeldiniz !  \n lütfen bilgilerinizi giriniz : ")
    kullanıcı_adı=input("kullanıcı adınızı giriniz ! : ")
    sifre=input("sifrenizi giriniz: ")
    if (  (kullanıcı_adı ==kullanıcılar['number']['name'] ) and  (sifre==kullanıcılar['number']['pasword'] ) ):
        print("sisteme giriş yaptınız ! ")
    
    else:
        print("kullanıcı adı ve ya sifre hatalı ! ")   

else: # kayıtlı oldugu için giriş ekranı na yönlendirme için 
    print("sisteme giriş için hoşgeldiniz !  \n lütfen bilgilerinizi giriniz : ")
    kullanıcı_adı=input("kullanıcı adınızı giriniz ! : ")
    sifre=input("sifrenizi giriniz: ")
    if (  (kullanıcı_adı ==kullanıcılar['number']['name'] ) and  (sifre==kullanıcılar['number']['pasword'] )):
        print("sisteme giriş yaptınız ! ")
    
    else:
        print("kullanıcı adı ve ya sifre hatalı ! ")   



