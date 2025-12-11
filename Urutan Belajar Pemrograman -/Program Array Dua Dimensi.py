# Program Array Dua Dimensi versi menarik

import time
import os

def clear():
    os.system("cls" if os.name == "nt" else "clear")

clear()
print("======================================")
print("     PROGRAM ARRAY DUA DIMENSI 2D     ")
print("======================================\n")
time.sleep(1)

# Membuat array 2 dimensi (matriks)
matriks = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

print(">>> Isi Matriks Awal:\n")
for baris in matriks:
    print("  |", "  ".join(f"{x:3d}" for x in baris), "|")
time.sleep(1)

# Akses elemen
print("\n>>> Akses Elemen:")
print(f"  Elemen [0][1] = {matriks[0][1]}")
print(f"  Elemen [2][2] = {matriks[2][2]}")
time.sleep(1)

# Mengubah elemen tengah
print("\n>>> Mengubah Elemen Tengah (baris 1, kolom 1) menjadi 555...\n")
matriks[1][1] = 555
time.sleep(1)

print(">>> Matriks Setelah Perubahan:\n")
for baris in matriks:
    print("  |", "  ".join(f"{x:3d}" for x in baris), "|")
time.sleep(1)

# Menjumlahkan semua elemen
total = sum(sum(baris) for baris in matriks)

print("\n>>> Total Semua Elemen dalam Matriks =", total)
print("\n======================================")
print("        Program Selesai ✓")
print("======================================")
