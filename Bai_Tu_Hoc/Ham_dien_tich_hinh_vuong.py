# Tạo hàm tính diện tích hình vuông.

# Hàm tính diện tích hình vuông
def tinh_dien_tich_hinh_vuong(canh): 
    return canh * canh

# Nhập độ dài cạnh từ người dùng
canh = float(input("Nhập độ dài cạnh của hình vuông: ")) 

# Tính và in kết quả
dien_tich = tinh_dien_tich_hinh_vuong(canh) 
print(f"Diện tích của hình vuông là: {dien_tich}")