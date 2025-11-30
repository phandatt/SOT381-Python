a = int(input("Nhập số a: "))
b = int(input("Nhập số b: "))

while b != 0:
    a, b = b, a % b
print(f"Ước chung lớn nhất là: {a}")