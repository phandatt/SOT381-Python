def tinhS(n):
    tong_tu = 0
    tong_mau = 0

    for i in range(1, n + 1):
        tong_tu += i
        if i % 2 == 0:
            tong_mau += i
    S = tong_tu / tong_mau
    return S

n = int(input("Nhập số n: "))
ket_qua = tinhS(n)
print(f"Kết quả S = {ket_qua}")
   
    
