import time
import os

# Fungsi membersihkan layar
def clear():
    os.system("cls" if os.name == "nt" else "clear")

clear()
print("===========================================")
print("        PROGRAM KONSEP STRUCTURE           ")
print("===========================================\n")
time.sleep(1)

# Membuat Struktur seperti struct menggunakan class
class Mahasiswa:
    def __init__(self, nama, nim, jurusan, ipk):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan
        self.ipk = ipk

print(">>> Membuat struktur data mahasiswa...\n")
time.sleep(1)

# Membuat object struktur
mhs = Mahasiswa("Ana Laili", "220302003", "Sistem Informasi", 3.85)

print("=== DATA MAHASISWA (STRUCTURE) ===\n")
print(f"Nama     : {mhs.nama}")
print(f"NIM      : {mhs.nim}")
print(f"Jurusan  : {mhs.jurusan}")
print(f"IPK      : {mhs.ipk}\n")
time.sleep(1)

print(">>> Menampilkan struktur dalam bentuk tabel...\n")
time.sleep(1)

# Tampilan tabel rapi
print("+----------------------+----------------------+")
print("|        FIELD         |        VALUE         |")
print("+----------------------+----------------------+")
print(f"| Nama                 | {mhs.nama:<20} |")
print(f"| NIM                  | {mhs.nim:<20} |")
print(f"| Jurusan              | {mhs.jurusan:<20} |")
print(f"| IPK                  | {mhs.ipk:<20} |")
print("+----------------------+----------------------+\n")

time.sleep(1)
print(">>> Struktur berhasil ditampilkan!\n")

print("===========================================")
print("             PROGRAM SELESAI ✓             ")
print("===========================================")
