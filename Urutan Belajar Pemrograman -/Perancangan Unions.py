import time

# ==========================================================
# WARNA UNTUK TERMINAL
# ==========================================================
class Color:
    HEADER = "\033[95m"
    BLUE = "\033[94m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    CYAN = "\033[96m"
    RED = "\033[91m"
    END = "\033[0m"

# ==========================================================
# CLASS SIMULASI UNION
# ==========================================================
class Union:
    def __init__(self):
        self.value = None
        self.type = None
        self.history = []

    def garis(self):
        print(Color.BLUE + "-"*50 + Color.END)

    def set_value(self, val, tipe):
        if tipe.lower() == "int":
            self.value = int(val)
            self.type = "INTEGER"
        elif tipe.lower() == "float":
            self.value = float(val)
            self.type = "FLOAT"
        elif tipe.lower() == "string":
            self.value = str(val)
            self.type = "STRING"
        else:
            print(Color.RED + "Tipe data tidak valid!" + Color.END)
            return
        self.history.append((self.value, self.type))
        print(Color.CYAN + f">>> Mengisi data sebagai {self.type}" + Color.END)
        print(Color.GREEN + f"Nilai saat ini : {self.value}" + Color.END)
        self.garis()
        time.sleep(1)

    def tampilkan_history(self):
        print(Color.YELLOW + "\nRiwayat Perubahan Union:" + Color.END)
        for i, (val, tipe) in enumerate(self.history, start=1):
            print(f"{i}. Nilai: {val} | Tipe: {tipe}")
        self.garis()

# ==========================================================
# PROGRAM UTAMA
# ==========================================================
print(Color.HEADER + "===== SIMULASI UNION INTERAKTIF =====\n" + Color.END)
time.sleep(1)

union_var = Union()

while True:
    print("\nPilih tipe data untuk diisi:")
    print("1. Integer")
    print("2. Float")
    print("3. String")
    print("4. Tampilkan Riwayat")
    print("5. Keluar")
    choice = input("Masukkan pilihan (1-5): ")

    if choice == "1":
        val = input("Masukkan nilai integer: ")
        union_var.set_value(val, "int")
    elif choice == "2":
        val = input("Masukkan nilai float: ")
        union_var.set_value(val, "float")
    elif choice == "3":
        val = input("Masukkan nilai string: ")
        union_var.set_value(val, "string")
    elif choice == "4":
        union_var.tampilkan_history()
    elif choice == "5":
        print(Color.HEADER + "\n>>> Program selesai!" + Color.END)
        break
    else:
        print(Color.RED + "Pilihan tidak valid! Silakan coba lagi." + Color.END)
