#1 Kullanici Bilgileri

name, age, height = None, None, None

name=input("Adiniz:")
age=int(input("Yasiniz:"))
height=float(input("Boyunuz: "))

print(f"Sayin {name};bize yasinizi {age},boyunuzu {height} olarak bildirdiniz.")

#2 Ders Notlari
math,phy,chem=None,None,None

math=int(input("Matematik :"))
phy=int(input("Fizik :"))
chem=int(input("Kimya : "))

mean=(math+phy+chem)/3
print(f"ortalamaniz : {mean}")

#3 Karakterler

country="Türkiye"
firstCh=country[0]
lastCh=country[-1]
length=len(country)
reversWord=list(reversed(country))
print(f"Ilk harf:{firstCh}\n Son harf:{lastCh} \n Uzunluk:{length} \n Ters hali: {reversWord}")