while True:
    print("=== MENU ===")
    print("1. Xin chào")
    print("2. Bạn cần tính bình phương số?")
    print("0. Thoát")
    
    lua_chon = input("Nhập số chức năng: ")
    if lua_chon == "1":
        print("Xin chào! ")
    elif lua_chon == "2":
        x = int(input("Nhập số bạn cần: "))
        print(f"Bình phường số {x}: {x * x}")
    elif lua_chon == "0":
        print("Tạm biệt! Hẹn gặp lại. ")
        break
    else:
        print("Lựa chọn không hợp lệ! Vui lòng chọn lại!")