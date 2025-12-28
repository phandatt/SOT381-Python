số = int(input("Nhập số cần kiểm tra: "))
if số < 2:
    print("Đây không phải là số nguyên tố.")
else:
    là_số_nguyên_tố = True
    for i in range(2, int(số ** 0.5) + 1):
        if số % i == 0:
            là_số_nguyên_tố = False
            break
    print("Đây là số nguyên tố" if là_số_nguyên_tố else "Không phải là số nguyên tố.")
