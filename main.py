# entrypoint => main.py

# otomasyon programlama => e-ticaret, e-devlet

# yapay zeka =>

# değişkenler
# python dili type-safe değildir.
# değişken tipleri
number = 10  # integer, int
print(number)

name = 'Halit' # string, String
print(name)
print(type(name))
# python değişken tipinin değişmesine izin veriyor.
name = 20
print(name)
print(type(name))

# Değişken isimleri rakamla başlayamaz, ya harf ya da _ ile başlamalı.
# Özel keywordler olamaz (def,while,if gibi)
_age = 25
print(_age) 

#işlem => operatörler
print("******")
print(25+50)
print(50-25)
print(100/2) # double,float => ondalıklı sayı.
print(50*2)
print(100//2)
print(103//2)
print(101%2) # mod
print(5**3)

is_active = True

# karşılaşttırma operatörleri
print("Karşılaştırma:")
print(1==1)
print(1==2)
print(1!=2)
print(1 > 2)
print(1 >= 2)
print(1 < 2)
print(1 <= 2)
# Boolean, bool

# mantıksal operatörler -> and,or,not
print("Mantıksal:")
print(1 == 1 and 10 == 10) # true-true => true
print(1 == 1 and 10 == 11) # true-false => false
print(1 == 2 and 10 == 11) # false-false => false
print("Or")
print(1 == 1 or 10 == 10) # true-true => true
print(1 == 1 or 10 == 11) # true-false => true
print(1 == 2 or 10 == 11) # false-false => false

print("***")
print(1==1 and 5==5 or 25>10 and 50<100)
print("***")
print(not ( (( (5>3 and 5==5) and (3<5 or 5>3) ) and 3==3) or 5 < 3))
print(not 1==1)

# atama operatörleri
print("Atama")
x=5

#x = x+3
x+=3
x-=2
x*= 5
x/= 1 # float
# x=x//5
x//=5 # float
print(x)
# **, %, //, /
#

students = [ "Beyzanur", "Ali", "Yusuf", 10, True, 5.0 ]
students.append("Eda Nur")
print(students)
students.pop()
print(students)
print(students[3])
#print(students[6])

a=5
b=a #5
b+=10
print(a)
print(b)
# Value type-Reference Type => Immutable - Mutable typelar

a_list=["Eleman 1", "Eleman 2"]     
b_list = a_list
b_list.append("Eleman 3") # @123ABC
print(a_list)
print(b_list)
