nhiet_do = float(input("Nhập nhiệt độ: "))
loai_nhiet_do = input("Nhập loại nhiệt độ: ")

if loai_nhiet_do == "C":
    F = nhiet_do * 1.8 + 32
    K = nhiet_do + 273.15
    print(f"{F:.2f}")
    print(f"{K:.2f}")
elif loai_nhiet_do == "F":
    C = (nhiet_do - 32) / 1.8
    K = (nhiet_do + 459.67) / 1.8
    print(f"{C:.2f}")
    print(f"{K:.2f}")
elif loai_nhiet_do == "K":
    C = nhiet_do -273.15
    F = (nhiet_do - 273.15) * 1.8 + 32
    print(f"{C:.2f}")
    print(f"{F:.2f}")
else:
    print("Loại không hợp lệ! Vui lòng nhập C, F hoặc K.")
