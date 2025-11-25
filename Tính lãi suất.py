tien_goc = 100000000
lai_suat = 0.07
so_nam = int(input("Nhập số năm bạn muốn: "))

for nam in range (1, so_nam + 1):
    so_tien_cuoi_nam = tien_goc * (1 + lai_suat) ** nam
    print(f"Năm {nam}: {so_tien_cuoi_nam:,.0f} VNĐ")
             
            