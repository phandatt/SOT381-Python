print("=== THÔNG TIN CÁ NHÂN ===")

full_name = input("Nhập họ và tên: ")
birth_year = int(input("Nhập năm sinh: "))
height = float(input("Nhập chiều cao của bạn (m): "))
weight = float(input("Nhập cân nặng của bạn (kg): "))

# Tính BMI
bmi = weight / (height ** 2)
current_year = int(input("Nhập năm hiện tại: "))
age = current_year - birth_year

print("\n" + "=" *40)
print("THÔNG TIN ĐÃ NHẬP: ")
print(f"Họ và tên: {full_name: >18}")
print(f"Tuổi: {age: >18}")
print(f"Chiều cao: {height: >18.1f} m")
print(f"Cân nặng: {weight: >18.1f} kg")
print(f"Chỉ số BMI: {bmi: >17.2f}")
print("="*40)

