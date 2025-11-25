diem_so = [8.5, 9.0, 8.3, 7.5, 6.5]
tong_diem = 0
so_mon = 0

print("Quá trình tính điểm: ")
for diem in diem_so:
    tong_diem += diem
    so_mon += 1
    print(f"Môn {so_mon}: {diem} điểm")

diem_trung_binh = tong_diem / so_mon
print(f"Điểm trung bình: {diem_trung_binh:.2f}")