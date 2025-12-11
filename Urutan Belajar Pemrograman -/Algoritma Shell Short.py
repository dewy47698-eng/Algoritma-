import time
import os

# ============================
#   WARNA UNTUK ANIMASI
# ============================
MERAH = "\033[91m"
HIJAU = "\033[92m"
KUNING = "\033[93m"
BIRU = "\033[94m"
CYAN = "\033[96m"
RESET = "\033[0m"

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def tampil_data(data, highlight1=None, highlight2=None):
    """Menampilkan array dengan warna untuk elemen yang diproses"""
    hasil = ""
    for i, v in enumerate(data):
        if i == highlight1:
            hasil += f"{MERAH}[{v}]{RESET} "      # elemen utama
        elif i == highlight2:
            hasil += f"{KUNING}({v}){RESET} "     # elemen pembanding
        else:
            hasil += f"{v} "
    print(" ", hasil)


def shell_sort(data):
    n = len(data)
    gap = n // 2

    print(CYAN + "=== PROSES SHELL SORT DIMULAI ===\n" + RESET)
    time.sleep(1)

    while gap > 0:
        clear()
        print(BIRU + f"Gap saat ini: {gap}" + RESET)
        print("Mengelompokkan data dengan jarak gap...\n")
        tampil_data(data)
        time.sleep(1.5)

        for i in range(gap, n):
            temp = data[i]
            j = i

            clear()
            print(BIRU + f"Gap {gap} – Memasukkan {MERAH}{temp}{RESET} ke posisi yang tepat\n")
            tampil_data(data, highlight1=i)
            time.sleep(1)

            while j >= gap and data[j - gap] > temp:
                clear()
                print(KUNING + f"{data[j - gap]} lebih besar dari {temp}, geser ke kanan" + RESET)
                tampil_data(data, highlight1=j, highlight2=j-gap)
                time.sleep(1)

                data[j] = data[j - gap]
                j -= gap

            data[j] = temp

            clear()
            print(HIJAU + f"{temp} ditempatkan pada posisi {j}" + RESET)
            tampil_data(data)
            time.sleep(1)

        gap //= 2
        print(HIJAU + f"\nGap diperkecil menjadi {gap}\n" + RESET)
        time.sleep(1.5)

    print(CYAN + "\n=== PROSES SHELL SORT SELESAI ===\n" + RESET)
    return data


# ============================
#        PROGRAM UTAMA
# ============================

clear()
print("PROGRAM SHELL SORT (Animasi + Warna)")
data = list(map(int, input("Masukkan angka (pisahkan dengan spasi): ").split()))

print("\nData sebelum diurutkan:", data)
input("\nTekan ENTER untuk memulai...")

hasil = shell_sort(data)

print("\nData setelah diurutkan:", HIJAU, hasil, RESET)
