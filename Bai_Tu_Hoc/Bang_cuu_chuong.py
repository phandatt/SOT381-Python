# In bảng cửu chương cho một số.

# Nhập một số từ người dùng
so = int(input("Nhập một số: "))

# In bảng cửu chương của số đó
print(f"Bảng cửu chương của {so}:") 
for i in range(1, 11): 
    print(f"{so} x {i} = {so * i}") 
