# Tạo hàm tính diện tích hình chữ nhật.

# Hàm tính diện tích hình chữ nhật
def tinh_dien_tich_hinh_chu_nhat(chieu_dai, chieu_rong): 
    return chieu_dai * chieu_rong

# Nhập chiều dài và chiều rộng 
chieu_dai = float(input("Nhập chiều dài của hình chữ nhật: ")) 
chieu_rong = float(input("Nhập chiều rộng của hình chữ nhật: "))

# Tính và in kết quả
dien_tich = tinh_dien_tich_hinh_chu_nhat(chieu_dai, chieu_rong) 
print(f"Diện tích của hình chữ nhật là: {dien_tich}") 