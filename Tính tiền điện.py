so_kWh = int(input("Nhập số điện (kWh): "))
tong_tien = 0

if so_kWh <= 50:
    tong_tien = so_kWh * 1.678
elif so_kWh <= 100:
    tong_tien = 50 * 1.678 + (so_kWh - 50) * 1.734
elif so_kWh <= 200:
    tong_tien = (50 * 1.678) + (50 * 1.734) + ((so_kWh - 100) * 2.014)
elif so_kWh <= 350:
    tong_tien = (50 * 1.678) + (50 * 1.734) + (100 * 2.014) + ((so_kWh - 200) * 2.536)
else:
    tong_tien = (50 * 1.678) + (50 * 1.734) + (100 * 2.014) + (150 * 2.536) + ((so_kWh - 350) * 2.927)
    
print(f"Tiền điện phải trả: {tong_tien:.2f} VNĐ")