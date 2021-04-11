sorular = ['Hangisi Kaymağı İle Ünlü Olan İlimizdir ?',
'Hangisi Dondurması İle Ünlü Olan İlimizdir ?',
'Hangisi Pidesi İle Ünlü Olan İlimizdir ?',
'türkiyenin başkenti ?',
'üçgenin iç açıları toplamı kaç ',
'1 saniye kac sanıse',
'1 dk kaç sanıye',
'pirinç ne tür bir yiyecektir?',
'vucudumuzun yuzde kaçı sudur?',
'mide agzına verilen isim nedir ?',
]

soru_1_cevaplar = ['A) Afyon','B) Mersin','C) Yozgat','D) Bursa']
soru_2_cevaplar = ['A) Denizli','B) Konya','C) KahramanMaraş','D) Eskişehir']
soru_3_cevaplar = ['A) Bursa','B) Konya','C) İstanbul','D) Ankara']
soru_4_cevaplar = ['A) Afyon','B) Mersin','C) ankara','D) Bursa']
soru_5_cevaplar = ['A) 180','B) 120','C) 100','D) 190']
soru_6_cevaplar = ['A) 100','B) 60','C) 120','D) 180']
soru_7_cevaplar = ['A) 100','B) 60','C) 120','D) 180']
soru_8_cevaplar = ['A) karbonhidrat','B) protein','C) yag','D) vitamin']
soru_9_cevaplar = ['A) 30','B) 40','C) 60','D) 70']
soru_10_cevaplar = ['A) pilor','B) kapak','C) kapı','D) kardıyak']

dogru_cevaplar = ['a','c','b','c','a','a','b','a','d','a']



def sor():

    puan = 0

    print('Soru 1:',sorular[0])

    for x in soru_1_cevaplar:

        print(x)

    cevap_1 = input('Cevabınız Nedir: ')

    if (cevap_1.lower() == dogru_cevaplar[0]):

        print('Tebrikler! Doğru Cevap.')

        puan += 10

    else:

        print('Cevabınız Yanlış. Doğru Cevap A Şıkkı.')

    print('-'*50)

    

    print('Soru 2:',sorular[1])

    for x in soru_2_cevaplar:

        print(x)

    cevap_2 = input('Cevabınız Nedir: ')

    if (cevap_2.lower() == dogru_cevaplar[1]):

        print('Tebrikler! Doğru Cevap.')

        puan += 10

    else:

        print('Cevabınız Yanlış. Doğru Cevap C Şıkkı.')

    print('-'*50)



    print('Soru 3:',sorular[2])

    for x in soru_3_cevaplar:

        print(x)

    cevap_3 = input('Cevabınız Nedir: ')

    if (cevap_3.lower() == dogru_cevaplar[2]):

        print('Tebrikler! Doğru Cevap.')

        puan += 10

    else:

        print('Cevabınız Yanlış. Doğru Cevap B Şıkkı.')

    print('-'*50)

    print('Soru 4:',sorular[3])

    for x in soru_4_cevaplar:

        print(x)

    cevap_4 = input('Cevabınız Nedir: ')

    if (cevap_4.lower() == dogru_cevaplar[3]):

        print('Tebrikler! Doğru Cevap.')

        puan += 10

    else:

        print('Cevabınız Yanlış. ')

    print('-'*50)

    

    print('Soru 5:',sorular[4])

    for x in soru_5_cevaplar:

        print(x)

    cevap_5 = input('Cevabınız Nedir: ')

    if (cevap_5.lower() == dogru_cevaplar[4]):

        print('Tebrikler! Doğru Cevap.')

        puan += 10

    else:

        print('Cevabınız Yanlış. .')

    print('-'*50)



    print('Soru 6:',sorular[5])

    for x in soru_6_cevaplar:

        print(x)

    cevap_6 = input('Cevabınız Nedir: ')

    if (cevap_6.lower() == dogru_cevaplar[5]):

        print('Tebrikler! Doğru Cevap.')

        puan += 10

    else:

        print('Cevabınız Yanlış..')

    print('-'*50)
    puan = 0

    print('Soru 7:',sorular[6])

    for x in soru_7_cevaplar:

        print(x)

    cevap_7 = input('Cevabınız Nedir: ')

    if (cevap_7.lower() == dogru_cevaplar[6]):

        print('Tebrikler! Doğru Cevap.')

        puan += 10

    else:

        print('Cevabınız Yanlış..')

    print('-'*50)

    

    print('Soru 8:',sorular[7])

    for x in soru_8_cevaplar:

        print(x)

    cevap_8 = input('Cevabınız Nedir: ')

    if (cevap_8.lower() == dogru_cevaplar[7]):

        print('Tebrikler! Doğru Cevap.')

        puan += 10

    else:

        print('Cevabınız Yanlış. Doğru Cevap C Şıkkı.')

    print('-'*50)



    print('Soru 9:',sorular[8])

    for x in soru_9_cevaplar:

        print(x)

    cevap_9 = input('Cevabınız Nedir: ')

    if (cevap_9.lower() == dogru_cevaplar[8]):

        print('Tebrikler! Doğru Cevap.')

        puan += 10

    else:

        print('Cevabınız Yanlış. Doğru Cevap B Şıkkı.')

    print('-'*50)
    for x in soru_10_cevaplar:

        print(x)

    cevap_10 = input('Cevabınız Nedir: ')

    if (cevap_10.lower() == dogru_cevaplar[9]):

        print('Tebrikler! Doğru Cevap.')

        puan += 10

    else:

        print('Cevabınız Yanlış. Doğru Cevap B Şıkkı.')

    print('-'*50)

    print('Soru Oyunumuz Bitmiştir. Toplamda {} puan aldınız'.format(puan))
    print(type(format(puan)))
    

    if(int(puan)<50):
        print("5 sorudan az dogru cevabınız var başarısız oldunuz")
    else:
        print("basarılı oldunuz")

sor()