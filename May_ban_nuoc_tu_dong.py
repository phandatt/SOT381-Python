so_tien = int(input("Nhập số tiền bạn có (đ): "))
             
print(" Máy bán nước tự động ")
print("1. Coca - 10000đ")
print("2. Pepsi - 12000đ")
print("3. Nước suối - 5000đ")

lua_chon = int(input("Nhập đồ uống bạn muốn: "))
if lua_chon == 1:
    print("Đã rõ! Vui lòng đợi trong giây lát")
    ten_mon = "Coca"
    print("Coca")
    gia_tien = 10000
    print("Giá: 10000đ")
elif lua_chon == 2:
    print("Đã rõ! Vui lòng đợi trong giây lát")
    ten_mon = "Pepsi"
    print("Pepsi")
    gia_tien = 12000
    print("Giá: 12000đ")
elif lua_chon == 3:
    print("Đã rõ! Vui lòng đợi trong giây lát")
    ten_mon = "Nước suối"
    print("Nước suối")
    gia_tien = 5000
    print("Giá: 5000đ")
else:
    print("Lựa chọn không hợp lệ")
    print("Exit")

if so_tien >= gia_tien:
    print("Mua thành công! Cảm ơn bạn!")
    tien_thua = so_tien - gia_tien
    print("Tiền thừa của bạn:" ,tien_thua, "đ")
else:
    print("Bạn không đủ tiền!")
    print("Vui lòng chọn món khác hoặc thêm tiền để mua được đồ uống!")
