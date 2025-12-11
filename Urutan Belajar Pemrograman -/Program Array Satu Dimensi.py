# Program Array Satu Dimensi dengan Tampilan Menarik

import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

nilai = [10, 20, 30, 40, 50]

def tampilkan_array():
    print("\n=== Daftar Nilai dalam Array ===")
    for i, val in enumerate(nilai):
        print(f"• nilai[{i}] = {val}")

def tambah_data():
    try:
        data = int(input("\nMasukkan angka baru: "))
        nilai.append(data)
        print("✓ Data berhasil ditambahkan!")
    except:
        print("⚠ Masukkan angka yang valid!")

def ubah_data():
    try:
        index = int(input("\nUbah nilai pada indeks ke: "))
        if 0 <= index < len(nilai):
            new_value = int(input("Masukkan nilai baru: "))
            nilai[index] = new_value
            print("✓ Data berhasil diubah!")
        else:
            print("⚠ Indeks tidak ditemukan!")
    except:
        print("⚠ Input tidak valid!")

def hapus_data():
    try:
        index = int(input("\nHapus data indeks ke: "))
        if 0 <= index < len(nilai):
            nilai.pop(index)
            print("✓ Data berhasil dihapus!")
        else:
            print("⚠ Indeks tidak valid!")
    except:
        print("⚠ Input harus berupa angka!")

while True:
    clear()
    print("===== PROGRAM ARRAY 1 DIMENSI =====")
    print("1. Tampilkan isi array")
    print("2. Tambah data")
    print("3. Ubah data")
    print("4. Hapus data")
    print("5. Keluar")

    pilihan = input("\nPilih menu (1-5): ")

    if pilihan == "1":
        tampilkan_array()
    elif pilihan == "2":
        tambah_data()
    elif pilihan == "3":
        ubah_data()
    elif pilihan == "4":
        hapus_data()
    elif pilihan == "5":
        print("\nTerima kasih! Program selesai.")
        break
    else:
        print("\n⚠ Pilihan tidak valid!")

    input("\nTekan ENTER untuk lanjut...")
