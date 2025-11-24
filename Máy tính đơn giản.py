print("=== MÁY TÍNH ĐƠN GIẢN ===")

num1 = float(input("Nhập số bạn muốn: "))
num2 = float(input("Nhập số bạn muốn: "))
operation = input("Chọn phép tính: ")

if operation == "+":
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
elif operation == "-":
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
elif operation == "*":
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
elif operation =="/":
    if num2 != 0:
        result = num1 / num2
        print(f"{num1} / {num2} = {result:.2f}")
    else:
        print("Lỗi! Không thể chia hết cho 0!")
else:
    print("Phép tính không hợp lệ!")
    
