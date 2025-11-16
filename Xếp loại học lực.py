diem = float(input("Nhập điểm của bạn: "))
print("Điểm của bạn là: ", diem)

if diem >= 8:
    print("Học lực của bạn là: Giỏi.")
    print("Hãy tiếp tục phát huy.")
elif diem >= 6.5:
    print("Học lực của bạn là: Khá .")
    print("Tiếp tục cố gắng.")
elif diem>= 5:
    print("Học lực của bạn là: Trung bình.")
    print("Cần cố gắng thêm.")
else:
    print("Học lực của bạn là: Yếu.")
    print("Bạn cần cố gắng hơn rất nhiều.")
    