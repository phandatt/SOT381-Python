a = float(input("Nhập số a: "))
b = float(input("Nhập số b: "))
c = float(input("Nhập số c: "))

max = a
if b > max:
    max = b
if c > max:
    max = c

min = b
if a < min:
    min = a
if c < min:
    min = c

print(f"Số lớn nhất là: {max:.2f}")
print(f"Số nhỏ nhất là: {min:.2f}")

