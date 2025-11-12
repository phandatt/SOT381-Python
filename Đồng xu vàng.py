# Điểm số bắt đầu
diem_so = 100
print("Điểm số ban đầu của Naples:", diem_so)

# Naples nhắt được đồng xu vàng
print("Naples nhắt được đồng xu vàng! +50 điểm")
diem_so += 50
# Cập nhật điểm số
print("Điểm số hiện tại:", diem_so)

# Naples dẫm phải bẫy
print("Naples dẫm phải bẫy! -20 điểm")
diem_so -= 20
print("Điểm số hiện tại:", diem_so)

# Dùng toán tử để kiểm tra
diem_qua_man = 200
print("Điểm bắt buộc để qua màn:", diem_qua_man)

# Đặt câu hỏi cho máy tính: "Điểm số của Aria có lớn hơn hoặc bằng điểm cần thiết không?"
ket_qua_qua_man = diem_so >= diem_qua_man

print("Naples có đủ điểm qua màn không?", ket_qua_qua_man)
