von = 100000000
lai_suat = 0.07
nam = int(input("Nhập số năm bạn muốn: "))

print(f"Đầu tư {von:,} VNĐ với mức lãi suất {lai_suat} trong 1 năm")
for i in range (1, nam + 1):
    von = von * (1 + lai_suat)
    print(f"Năm {i}: → {von:,.0f} VNĐ")
    
print(f"Sau {nam} năm: {von:,.0f} VNĐ")