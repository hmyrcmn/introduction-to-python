# diziyi ikiye böldüm ve ilk ve son kısmınının yerini değiştirdim . 
liste=[11,12,13,14,15,16,17,18,19,20]
new_list=[]
new_list[::]=liste[5::1]  # 5 yerine len(liste)/2 yazılabilir 
new_list[6::]=liste[:5:1] 
print(liste)
print(new_list)

# diziyi tersden yazdırmak için reverse komutu kullandım 

liste.reverse()
print(liste)
new_list.reverse()
print(new_list)


# day 2 homework 2: 
x=int(input("\n dikkat sadece tek basamaklı sayı girebilirsiniz \n kaça kadar çift sayıları yazdırmak istersiniz: "))
liste_cift=[] # belirli aralıktaki sayıları için bir liste oluşturdum.
if (x>1 and x<10):
    for i in range(0,x+1,1):
        if(i%2==0):
            print(i)
            liste_cift.append(i)
    print(liste_cift)
else:
    print( "lütfen belirtilen aralıkta deger giriniz !")
