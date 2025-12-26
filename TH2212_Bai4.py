def so_lon_nhat(a, b, c):
    return max(a, b, c)
def so_nho_nhat(a, b, c):
    return min(a, b, c)

a = float(input("Nhập số a: "))
b = float(input("Nhập số b: "))
c = float(input("Nhập số c: "))

print("Số lớn nhất là: ", so_lon_nhat(a, b, c))
print("Số nhỏ nhất là: ", so_nho_nhat(a, b, c))

