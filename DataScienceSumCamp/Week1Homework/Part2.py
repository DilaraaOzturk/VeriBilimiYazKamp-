# 4 Operatörler

num1=int(input("Bir sayi giriniz:"))
num2=int(input("Bir sayi giriniz:"))

print(f"Sayilarin toplami : {num1 + num2}")
print(f"Sayilarin farki : {num1-num2}")
print(f"Sayilarin bolumu :{num1/num2}")
print(f"Sayilarin modu : {num1%num2}")

# 5 Ogrenci Ortalama

stuMean=float(input("Ortalamanizi giriniz: "))
if(stuMean>50):
    print("Tebrikler geçtiniz..")
else:
    print("Üzgünüz kaldiniz..")
    
# 6 Ehliyet 
        
age_for_license=int(input("Yasinizi giriniz: "))
if(age_for_license>=18):
    print("Ehliyet alabilirsiniz.")
else:
    print("Ehliyet alamazsiniz.")
    
#7 ürün fiyat belirleme
prodPrice=float(input("Fiyat: "))
prodSale=float(input("İndirim orani % :"))
lastPrice=prodPrice-prodPrice*(prodSale/100)
print(f"Ürünün son fiyati : {lastPrice}")      
 
#8 T & F ifadeler
print(1==1)
print(1!=12)
print(45<12)
print(48>47)





