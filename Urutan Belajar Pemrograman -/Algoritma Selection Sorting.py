import os
import time

# Warna ANSI
MERAH = "\033[91m"
HIJAU = "\033[92m"
KUNING = "\033[93m"
BIRU = "\033[94m"
MAGENTA = "\033[95m"
RESET = "\033[0m"

# Clear layar
def clear():
    os.system("cls" if os.name == "nt" else "clear")

# Animasi loading
def loading(text):
    print(KUNING + text, end="")
    for _ in range(3):
        print(".", end="", flush=True)
        time.sleep(0.3)
    print(RESET)

# Selection Sort dengan visualisasi
def selection_sort_visual(arr, ascending=True):
    n = len(arr)
    for i in range(n):
        idx = i
        for j in range(i+1, n):
            print(f"Membandingkan {arr[idx]} dan {arr[j]}")
            time.sleep(0.5)
            if (ascending and arr[j] < arr[idx]) or (not ascending and arr[j] > arr[idx]):
                idx = j
        if idx != i:
            arr[i], arr[idx] = arr[idx], arr[i]
            print(HIJAU + f"Ditukar: {arr}" + RESET)
        else:
            print(BIRU + f"Tidak ada pertukaran pada iterasi ke-{i+1}" + RESET)
        time.sleep(0.5)
    return arr

# Menu interaktif
arr = []

while True:
    clear()
    print(BIRU + "========================================")
    print("          ALGORITMA SELECTION SORT")
    print("========================================" + RESET)

    print("\n=== MENU ===")
    print("1. Masukkan Elemen Array")
    print("2. Tampilkan Array")
    print("3. Selection Sort Ascending")
    print("4. Selection Sort Descending")
    print("5. Reset Array")
    print("6. Keluar")

    pilihan = input("\nPilih menu (1-6): ")

    if pilihan == "1":
        try:
            arr_input = input("Masukkan elemen array, pisahkan dengan spasi: ")
            arr = [int(x) for x in arr_input.split()]
            loading("Menyimpan elemen array")
            print(HIJAU + "Array berhasil disimpan!" + RESET)
        except:
            print(MERAH + "Input salah! Masukkan hanya angka." + RESET)
        input("\nTekan Enter untuk kembali...")

    elif pilihan == "2":
        if not arr:
            print(MERAH + "Array masih kosong!" + RESET)
        else:
            print(HIJAU + "Isi Array:" + RESET, arr)
        input("\nTekan Enter untuk kembali...")

    elif pilihan == "3":
        if not arr:
            print(MERAH + "Array masih kosong!" + RESET)
        else:
            print(BIRU + "\nMulai Selection Sort Ascending..." + RESET)
            sorted_arr = selection_sort_visual(arr.copy(), ascending=True)
            print(HIJAU + f"\nArray setelah Selection Sort Ascending: {sorted_arr}" + RESET)
        input("\nTekan Enter untuk kembali...")

    elif pilihan == "4":
        if not arr:
            print(MERAH + "Array masih kosong!" + RESET)
        else:
            print(BIRU + "\nMulai Selection Sort Descending..." + RESET)
            sorted_arr = selection_sort_visual(arr.copy(), ascending=False)
            print(HIJAU + f"\nArray setelah Selection Sort Descending: {sorted_arr}" + RESET)
        input("\nTekan Enter untuk kembali...")

    elif pilihan == "5":
        arr.clear()
        loading("Mereset array")
        print(HIJAU + "Array berhasil dikosongkan!" + RESET)
        input("\nTekan Enter untuk kembali...")

    elif pilihan == "6":
        print(KUNING + "Keluar dari program..." + RESET)
        time.sleep(1)
        break

    else:
        print(MERAH + "Pilihan tidak ada dalam menu!" + RESET)
        input("\nTekan Enter untuk kembali...")