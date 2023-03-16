total_belanja = int(input("Total belanja: Rp "))
bayar = total_belanja

if total_belanja > 100000:
    print("Kamu mendapatkan bonus amerrr")
    print("dan diskon nge BO 5% ")
    
    diskon = total_belanja * 5 / 100
    bayar = total_belanja - diskon

print("Total yang harus dibayar: Rp", bayar)
print("Terima kasihhh")
print("Tunggu kunjungan anda berikutnya")
