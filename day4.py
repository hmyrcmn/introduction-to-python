ogrenciler = {}
import math

for i in range (1,3, 1):  # 5 öğrenci için kayıt oluşturma 
    number = input("öğrenci no: ")
    name = input("öğrenci adı: ")
    surname = input("öğrenci soyad: ")
    vıze = math.ceil((0.3)*float (input("öğrenci vize: ")))
    fınal=math.ceil((0.4)*float(input("ögrenci final not: ")))
    project=math.ceil((0.3)*float(input("ögrenci proje: ")))  

    ogrenciler.update({
        number: {
            'ad': name,
            'soyad': surname,
            'final':fınal ,
            'vize':vıze,
            'proje':project,
            
        }
    })
    
 # tüm dic bilgileri gösteren kod 
for i in ogrenciler.values():
   print(i)

"""
print(ogrenciler) # tüm dic listeyi verir 
ogrenciler["1"]["vize"]  # 1. ögrencinin vize notunu verir
print(ogrenciler["1"]["vize"])
"""
def dızıyap():
    dizi1=[]

    dizi1.append(ogrenciler["1"]["vize"])       
    dizi1.append(ogrenciler["1"]["final"])
    dizi1.append(ogrenciler["1"]["proje"])

    dizi1.sort()
    return dizi1
num1=dızıyap()