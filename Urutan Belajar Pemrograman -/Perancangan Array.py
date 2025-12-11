# ==========================================================
#        PROGRAM PERANCANGAN ARRAY 1D & 2D (MENARIK)
# ==========================================================

# Warna teks agar tampilan lebih hidup
class Color:
    HEADER = "\033[95m"
    BLUE = "\033[94m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    END = "\033[0m"

print(Color.HEADER + "===== PROGRAM PERANCANGAN ARRAY =====" + Color.END)

# ==========================================================
# ARRAY 1 DIMENSI
# ==========================================================
print(Color.BLUE + "\n--- ARRAY 1 DIMENSI ---" + Color.END)

angka = [10, 20, 30, 40, 50]
print(Color.GREEN + "Isi array awal:", angka, Color.END)

print(Color.YELLOW + f"Elemen pertama  : {angka[0]}" + Color.END)
print(Color.YELLOW + f"Elemen terakhir : {angka[-1]}" + Color.END)

# Menambah elemen
angka.append(60)
print(Color.GREEN + "Setelah ditambah elemen 60:", angka, Color.END)


# ==========================================================
# ARRAY 2 DIMENSI (MATRIKS)
# ==========================================================
print(Color.BLUE + "\n--- ARRAY 2 DIMENSI (MATRIKS) ---" + Color.END)

matriks = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(Color.GREEN + "Isi Matriks:" + Color.END)
for baris in matriks:
    print(" ", baris)

# Mengakses elemen tertentu
print(Color.YELLOW + "\nMengakses elemen baris 2 kolom 3 →", matriks[1][2], Color.END)

print(Color.HEADER + "\n===== PROGRAM SELESAI =====" + Color.END)
