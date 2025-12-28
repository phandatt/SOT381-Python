n = int(input("Nhập số phần tử: "))
ds = []

for i in range(n):
    ds.append(int(input("Nhập phần tử i: ")))

tong = 0
for i in ds:
    tong += i

print("Danh sách:", ds)
print("Tổng các phần tử:", tong)