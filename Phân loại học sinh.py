diem_so = [8.5, 7.0, 9.2, 6.8, 5.5, 8.8]

for diem in diem_so:
    if diem >= 8:
        print(diem, ": Giỏi")
    elif 6.5 <= diem <= 7.9:
        print(diem, ": Khá")
    else:
        print(diem, ": Trung bình")