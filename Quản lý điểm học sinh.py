ho_ten = input("Nhập họ và tên: ")
diem_toan = float(input("Nhập điểm môn toán: "))
diem_ly = float(input("Nhập điểm môn lý: "))
diem_hoa = float(input("Nhập điểm môn Hóa: "))

diem_trung_binh = ((diem_toan + diem_ly + diem_hoa) / 3)

if diem_trung_binh >= 8:
    xep_loai = "Giỏi"
elif diem_trung_binh >= 6.5:
    xep_loai = "Khá"
elif diem_trung_binh >= 5:
    xep_loai = "Trung bình"
else:
    xep_loai = "Yếu"
    
print(f"\n {'='*40}")
print(f"{'BẢNG KẾT QUẢ HỌC TẬP':>30}")
print(f"Họ và tên: {ho_ten}")
print(f"Điểm toán: {diem_toan:.2f}")
print(f"Điểm lý: {diem_ly:.2f}")
print(f"Điểm hóa: {diem_hoa:.2f}")
print(f"Điểm trung bình: {diem_trung_binh:.2f}")
print(f"Xếp loại: {xep_loai}")
