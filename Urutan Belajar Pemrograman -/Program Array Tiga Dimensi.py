import time
import os

# Fungsi membersihkan layar
def clear():
    os.system("cls" if os.name == "nt" else "clear")

clear()
print("============================================")
print("     PROGRAM ARRAY TIGA DIMENSI (3D)        ")
print("============================================\n")
time.sleep(1)

# Membuat array 3 dimensi
array3D = [
    [
        [1, 2, 3],
        [4, 5, 6]
    ],
    [
        [7, 8, 9],
        [10, 11, 12]
    ],
    [
        [13, 14, 15],
        [16, 17, 18]
    ]
]

print(">>> Struktur Array 3D Berhasil Dibuat!\n")
time.sleep(1)

# Menampilkan isi array 3D
print("=== ISI ARRAY 3D ===")
for i, lapisan in enumerate(array3D):
    print(f"\n-- Lapisan {i} --")
    for baris in lapisan:
        print(" | ", "  ".join(f"{x:3d}" for x in baris), " |")
    time.sleep(0.5)

# Akses elemen tertentu
print("\n=== AKSES ELEMEN ===")
print(f"Elemen [0][1][2] = {array3D[0][1][2]}")
print(f"Elemen [2][0][1] = {array3D[2][0][1]}")
time.sleep(1)

# Mengubah nilai
print("\n>>> Mengubah elemen [1][1][0] menjadi 999...\n")
array3D[1][1][0] = 999
time.sleep(1)

print("=== ARRAY SETELAH PERUBAHAN ===")
for i, lapisan in enumerate(array3D):
    print(f"\n-- Lapisan {i} --")
    for baris in lapisan:
        print(" | ", "  ".join(f"{x:3d}" for x in baris), " |")
    time.sleep(0.5)

# Hitung total elemen
total = sum(
    nilai
    for lapisan in array3D
    for baris in lapisan
    for nilai in baris
)

print("\n=== HASIL PERHITUNGAN ===")
print(f"Total seluruh elemen = {total}\n")

print("============================================")
print("              PROGRAM SELESAI ✓             ")
print("============================================")
