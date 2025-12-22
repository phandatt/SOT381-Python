n= int(input("Nhập số bài hát yêu thích: "))
dsBaiHat = []

for i in range(n):
    tenBai = input(f"Tên bài thứ {i+1}:")
    dsBaiHat.append(tenBai)

for i in range(n):
    ten = dsBaiHat[i]
    print(f"Bài {i+1}: {ten}")

for bai in dsBaiHat:
    print(bai.upper())
