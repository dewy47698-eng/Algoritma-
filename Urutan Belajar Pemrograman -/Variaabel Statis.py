import time
import os

# Fungsi membersihkan layar
def clear():
    os.system("cls" if os.name == "nt" else "clear")

clear()
print("==============================================")
print("         PROGRAM VARIABEL STATIS PYTHON       ")
print("==============================================\n")
time.sleep(1)

# Class dengan variabel statis
class Counter:
    count = 0    # variabel statis (bersama untuk semua objek)

    def tambah(self):
        Counter.count += 1
        print(f"✓ Counter bertambah menjadi: {Counter.count}")

print(">>> Membuat 2 objek counter...\n")
time.sleep(1)

c1 = Counter()
c2 = Counter()

print(">>> Menjalankan fungsi tambah() pada objek pertama...\n")
time.sleep(1)
c1.tambah()

print("\n>>> Menjalankan fungsi tambah() pada objek kedua...\n")
time.sleep(1)
c2.tambah()

print("\n>>> Menjalankan fungsi tambah() lagi pada objek pertama...\n")
time.sleep(1)
c1.tambah()

print("\n==============================================")
print("    NILAI COUNTER TETAP BERTAMBAH (STATIS)    ")
print("     Semua objek berbagi variabel yang sama   ")
print("==============================================")
