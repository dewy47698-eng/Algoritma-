# =====================================================
#          PROGRAM DICTIONARY INTERAKTIF
# =====================================================

print("=== PROGRAM DICTIONARY INTERAKTIF ===\n")

# Membuat dictionary awal
mahasiswa = {
    "001": "Ana",
    "002": "Yemima",
    "003": "Indri"
}

# Fungsi untuk menampilkan data dictionary
def tampilkan_data(dic):
    print("Data saat ini dalam dictionary:")
    for key, value in dic.items():
        print(f"ID {key} -> {value}")
    print()

# Tampilkan data awal
print("Data awal:")
tampilkan_data(mahasiswa)

# Menambah data baru
print("Menambah data baru ke dictionary...")
mahasiswa["004"] = "Dewi"
tampilkan_data(mahasiswa)

# Mengakses data tertentu
id_akses = "002"
print(f"Mengakses data dengan ID {id_akses}:")
print(f"ID {id_akses} -> {mahasiswa[id_akses]}\n")

# Mengubah data
print("Mengubah data ID 003 menjadi 'Indri'...")
mahasiswa["003"] = "Indri Sari"
tampilkan_data(mahasiswa)

# Menghapus data
print("Menghapus data dengan ID 001...")
del mahasiswa["001"]
tampilkan_data(mahasiswa)

# Menambahkan interaksi tambahan: cek ID tertentu
id_cek = "005"
print(f"Mengecek apakah ID {id_cek} ada dalam dictionary...")
if id_cek in mahasiswa:
    print(f"ID {id_cek} -> {mahasiswa[id_cek]}")
else:
    print(f"ID {id_cek} tidak ditemukan.\n")

# Menampilkan jumlah data
print(f"Jumlah total data dalam dictionary: {len(mahasiswa)}\n")

print("=== PROGRAM DICTIONARY SELESAI ===")