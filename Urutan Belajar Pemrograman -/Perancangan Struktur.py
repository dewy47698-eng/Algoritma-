import time

# ==============================
# Warna teks untuk terminal
# ==============================
class Color:
    HEADER = "\033[95m"
    BLUE = "\033[94m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    END = "\033[0m"

# ==============================
# Class Mahasiswa (sebagai struktur)
# ==============================
class Mahasiswa:
    def __init__(self, nama, nim, jurusan, ipk):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan
        self.ipk = ipk
    
    def tampilkan(self):
        print(f"{Color.GREEN}Nama    : {self.nama}{Color.END}")
        print(f"{Color.GREEN}NIM     : {self.nim}{Color.END}")
        print(f"{Color.GREEN}Jurusan : {self.jurusan}{Color.END}")
        print(f"{Color.GREEN}IPK     : {self.ipk}{Color.END}\n")

# ==============================
# Program utama
# ==============================
print(Color.HEADER + "===== PROGRAM PERANCANGAN STRUKTUR =====" + Color.END)
time.sleep(1)

# Membuat data mahasiswa
mhs1 = Mahasiswa("dewi susanti", "220302003", "Sistem Informasi", 3.85)
mhs2 = Mahasiswa("indriani", "220302004", "Teknik Informatika", 3.70)

print(Color.BLUE + "\n--- Data Mahasiswa 1 ---" + Color.END)
mhs1.tampilkan()
time.sleep(1)

print(Color.BLUE + "--- Data Mahasiswa 2 ---" + Color.END)
mhs2.tampilkan()
time.sleep(1)

# Mengubah data mahasiswa
print(Color.YELLOW + ">>> Mengubah IPK mahasiswa 2 menjadi 3.75..." + Color.END)
mhs2.ipk = 3.75
time.sleep(1)
print(Color.BLUE + "--- Data Mahasiswa 2 Setelah Update ---" + Color.END)
mhs2.tampilkan()

print(Color.HEADER + "===== PROGRAM SELESAI =====" + Color.END)
