while True:
    w = float(input("Nhập cạnh w: "))
    h = float(input("Nhập cạnh h: "))
    if 0.0 <= w and h <= 100.0:
        break
chu_vi = (w + h) * 2
dien_tich = w * h

print(f"Chu vi hình chữ nhật là: {chu_vi:.2f}")
print(f"Diện tích hình chữ nhật là: {dien_tich:.2f}")
