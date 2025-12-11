import time
import os

# Fungsi untuk membersihkan layar
def clear():
    os.system("cls" if os.name == "nt" else "clear")

clear()
print("==============================================")
print("           PROGRAM KONSEP UNION PYTHON        ")
print("==============================================\n")
time.sleep(1)

# Class meniru union: hanya satu tipe aktif
class UnionLike:
    def __init__(self):
        self._storage = None

    def set_int(self, value):
        self._storage = ("Integer", value)

    def set_float(self, value):
        self._storage = ("Float", value)

    def set_string(self, value):
        self._storage = ("String", value)

    def show(self):
        tipe, nilai = self._storage
        print(f" Tipe Aktif : {tipe}")
        print(f" Nilai      : {nilai}\n")

# Membuat union
u = UnionLike()

print(">>> Menyimpan nilai sebagai Integer...\n")
time.sleep(1)
u.set_int(100)
u.show()

print(">>> Mengubah nilai menjadi Float...\n")
time.sleep(1)
u.set_float(45.67)
u.show()

print(">>> Mengubah nilai menjadi String...\n")
time.sleep(1)
u.set_string("Halo Dunia!")
u.show()

time.sleep(1)
print("==============================================")
print("          SELURUH DATA UNION TERGANTI         ")
print("       (hanya 1 yang aktif pada satu waktu)   ")
print("==============================================")
