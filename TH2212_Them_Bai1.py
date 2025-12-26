import math
a = float(input("Nhập số a: "))
b = float(input("Nhập số b: "))
c = float(input("Nhập số c: "))

#Chu vi
chu_vi = a + b + c
#Nửa chu vi
p = chu_vi / 2
#Diện tích
dien_tich = math.sqrt(p * (p - a) * (p - b) * (p - c))

print(f"Chu vi của tam giác là: {chu_vi:.2f}")
print(f"Diện tích của tam giác là: {dien_tich:.2f}")
