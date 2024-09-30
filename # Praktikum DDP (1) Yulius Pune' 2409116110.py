# Program perhitungan harga barang

# Input data pengguna
nama = input("Masukkan Nama: ")
nim = input("Masukkan NIM: ")
kelas = input("Masukkan Kelas: ")

print("..............................................................................................................................")
print("Hai " + str(nama))
print("Dengan NIM " + str(nim))
print("Kelas: " + str(kelas))
print("..............................................................................................................................")
print()

# Menghitung harga barang
ulang = "ya"
while ulang.lower() == "ya":
    print("========== Menghitung Harga Barang ==============")
    
    harga_barang = float(input("Harga Barang: "))
    jumlah_barang = int(input("Jumlah Barang: "))
    
    # Harga Sebelum Diskon
    total_harga = harga_barang * jumlah_barang
    
    # Harga Setelah Diskon
    if total_harga >  250000:
        persen_diskon = total_harga * 0.25
        diskon = total_harga - persen_diskon
        print("Anda Mendapatkan Diskon 25%. Jadi harga barang Anda: Rp. " + str(diskon))
    else:
        print("Anda tidak mendapatkan diskon. Jadi harga barang: Rp. " + str(total_harga))
    
    print("=============== Selesai ==================")

    # Perulangan
    ulang = input("Lanjut menghitung atau tidak (ya/t): ")
    if ulang.lower() == "t":
        print("Terima kasih!")
        break
