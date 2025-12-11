import time
import os

# Warna ANSI
MERAH = "\033[91m"
HIJAU = "\033[92m"
KUNING = "\033[93m"
BIRU = "\033[94m"
CYAN = "\033[96m"
RESET = "\033[0m"

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def tampil_data(data, highlight=None, moved=None):
    """Menampilkan array dengan warna untuk elemen yang diproses"""
    output = ""
    for i, val in enumerate(data):
        if i == highlight:
            output += f"{MERAH}[{val}]{RESET} "      # key yang sedang diproses
        elif i == moved:
            output += f"{KUNING}({val}){RESET} "     # elemen yang digeser
        else:
            output += f"{val} "
    print(" ", output)


def insertion_sort(data):
    print(CYAN + "=== PROSES INSERTION SORT DIMULAI ===\n" + RESET)
    time.sleep(1)

    for i in range(1, len(data)):
        key = data[i]
        j = i - 1

        clear()
        print(BIRU + f"PASS {i}: Memasukkan nilai {MERAH}{key}{RESET} ke bagian terurut\n" + RESET)
        tampil_data(data, highlight=i)
        time.sleep(1)

        while j >= 0 and data[j] > key:
            clear()
            print(BIRU + f"PASS {i}: Menggeser elemen lebih besar → {data[j]}" + RESET)
            tampil_data(data, highlight=i, moved=j)
            time.sleep(1)

            data[j + 1] = data[j]
            j -= 1

        data[j + 1] = key

        clear()
        print(HIJAU + f"→ {key} ditempatkan di posisi {j+1}" + RESET)
        tampil_data(data)
        time.sleep(1)

    print(CYAN + "\n=== PROSES SELESAI ===" + RESET)
    return data


# ============================
#        PROGRAM UTAMA
# ============================

clear()
print("PROGRAM INSERTION SORT (berwarna & animasi)")
data = list(map(int, input("Masukkan angka (pisahkan dengan spasi): ").split()))

print("\nData sebelum diurutkan:", data)
input("\nTekan ENTER untuk memulai...")

hasil = insertion_sort(data)

print("\nData setelah diurutkan:", HIJAU, hasil, RESET)
