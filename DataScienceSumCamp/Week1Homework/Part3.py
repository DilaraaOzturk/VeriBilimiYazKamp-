from datetime import datetime 
#Mini alışveriş uygulamasi
prod1=float(input("1.ürünün fiyati:"))
prod2=float(input("2.ürünün fiyati:"))
prod3=float(input("3.ürünün fiyati:"))
toplam=prod1+prod2+prod3

if(toplam>200):
    toplam=toplam -toplam*(0.1)
    print("200 ve üzeri indirimi uygulanmiştir.(%10)")

print(f"Toplam: {toplam}")    

#10 Yaş grubu belirleme
bornYear=int(input("Dogum yilinizi giriniz: "))
age=datetime.now().year-bornYear
if(age<13):
    print("Çocuksunuz.")
elif(age<18):
    print("Ergensiniz.")
else:
    print("Yetişkinsiniz.")        
