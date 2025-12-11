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

# Bubble Sort dengan arah sorting
def bubble_sort(arr, ascending=True):
    n = len(arr)
    for i in range(n):
        swapped = False
        print(BIRU + f"\nIterasi ke-{i+1}" + RESET)
        for j in range(0, n-i-1):
            print(f"Membandingkan {arr[j]} dan {arr[j+1]}")
            time.sleep(0.3)
            if (ascending and arr[j] > arr[j+1]) or (not ascending and arr[j] < arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
                print(HIJAU + f"Ditukar: {arr}" + RESET)
        if not swapped:
            print(HIJAU + "Tidak ada pertukaran, array sudah terurut!" + RESET)
            break
    return arr

# Menu interaktif
arr = []

while True:
    clear()
    print(BIRU + "========================================")
    print("           ALGORITMA BUBBLE SORT")
    print("========================================" + RESET)

    print("\n=== MENU ===")
    print("1. Masukkan Elemen Array")
    print("2. Tampilkan Array")
    print("3. Bubble Sort Ascending")
    print("4. Bubble Sort Descending")
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
            print(BIRU + "\nMulai Bubble Sort Ascending..." + RESET)
            sorted_arr = bubble_sort(arr.copy(), ascending=True)
            print(HIJAU + f"\nArray setelah Bubble Sort Ascending: {sorted_arr}" + RESET)
        input("\nTekan Enter untuk kembali...")

    elif pilihan == "4":
        if not arr:
            print(MERAH + "Array masih kosong!" + RESET)
        else:
            print(BIRU + "\nMulai Bubble Sort Descending..." + RESET)
            sorted_arr = bubble_sort(arr.copy(), ascending=False)
            print(HIJAU + f"\nArray setelah Bubble Sort Descending: {sorted_arr}" + RESET)
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
        