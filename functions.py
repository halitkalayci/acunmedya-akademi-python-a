#fonksiyonlar -> kod tekrarını azaltmak için kullandığım tekrar eden 
# kodları isimli bir şekilde tekrar kullanılabilir hale getirmek.

price = 500
total_price = price + (price * 0.2)
print(total_price)
# fonksiyon tanımlamak
def calculate_tax(price, rate=20): #parametreler
    # fonksyion scopeundaki değişkenler o scope'a özeldir
    f_variable = "Deneme"
    return price + (price*(rate/100)) # hesaplamayı yap ve çağırılan yere değeri dön.
    #konsola çıktı ver.

price1 = calculate_tax(100) # konsola çıktı ver
#print(f_variable)
price2 = calculate_tax(200) # hesaplanan değeri al..
price3 = calculate_tax(200)
price4 = calculate_tax(300, 10)
price5 = calculate_tax(1000, 10)
price6 = calculate_tax(500, 10)
print(price1)
print(price2+price3)
print(price6)


def sum(*args):
    if len(args) <= 0:
        return "En az 1 sayı göndermek zorundasınız."
    sonuc = 0
    for sayi in args:
        sonuc += sayi
    return sonuc

print(sum(1,2))
print(sum(10,20,30,40,50,60,70))
print(sum(10,20,30))
print(sum(1))

x = sum() #string dönmek yerine bir hata fırlatmalı.
#print(x+50)

# *kwargs -> Araştıralım.

# lambda fonk.
# anonim

topla = lambda a,b: a+b
print(topla(1,2))

selamla = lambda isim: print(f"Merhaba {isim}")
selamla("Halit")

# oop

# class