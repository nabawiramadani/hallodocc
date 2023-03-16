total_belanja = int(input("Total belanja: Rp "))
bayar = total_belanja

if total_belanja > 100000 and total_belanja <= 500000:
    print("Kamu mendapatkan diskon 5%")
    diskon = total_belanja * 5 / 100
    bayar = total_belanja - diskon
elif total_belanja > 500000 and total_belanja <= 1000000:
    print("Kamu mendapatkan diskon 10%")
    diskon = total_belanja * 10 / 100
    bayar = total_belanja - diskon
elif total_belanja > 1000000:
    print("Kamu mendapatkan diskon 15%")
    diskon = total_belanja * 15 / 100
    bayar = total_belanja - diskon

print("Total yang harus dibayar: Rp", bayar)
print("Terima kasihhh")
print("Tunggu kunjungan anda berikutnya")
