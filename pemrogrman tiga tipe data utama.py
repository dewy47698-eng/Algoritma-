# =====================================================
#       PROGRAM TIPE DATA UTAMA (INT, FLOAT, STR)
# =====================================================

print("=== PROGRAM TIPE DATA UTAMA ===\n")

# 1. Integer
umur = 18
print(f"Integer (int) -> umur: {umur} (tipe: {type(umur)})")

# 2. Float
berat = 55.5
print(f"Float (float) -> berat: {berat} kg (tipe: {type(berat)})")

# 3. String
nama = "Dewi"
print(f"String (str) -> nama: {nama} (tipe: {type(nama)})\n")

# Operasi sederhana
print("=== Contoh Operasi pada Tipe Data ===\n")

# Operasi integer
tahun_lahir = 2003
tahun_sekarang = 2025
umur_hitung = tahun_sekarang - tahun_lahir
print(f"Operasi Integer: {tahun_sekarang} - {tahun_lahir} = {umur_hitung}")

# Operasi float
harga_barang = 125.75
jumlah_barang = 3
total_harga = harga_barang * jumlah_barang
print(f"Operasi Float: {harga_barang} x {jumlah_barang} = {total_harga}")

# Operasi string
greeting = "Halo"
pesan = greeting + " " + nama + "!"
print(f"Operasi String: '{greeting}' + '{nama}' = '{pesan}'")

print("\n=== PROGRAM SELESAI ===")