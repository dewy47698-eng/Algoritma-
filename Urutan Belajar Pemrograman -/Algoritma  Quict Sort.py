 
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

# Quick Sort dengan visualisasi
def quick_sort_visual(arr, ascending=True, level=0):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = [x for x in arr[1:] if (x <= pivot if ascending else x >= pivot)]
    right = [x for x in arr[1:] if (x > pivot if ascending else x < pivot)]
    
    print(MAGENTA + "  " * level + f"Pivot: {pivot}, Left: {left}, Right: {right}" + RESET)
    time.sleep(0.5)
    
    sorted_left = quick_sort_visual(left, ascending, level + 1)
    sorted_right = quick_sort_visual(right, ascending, level + 1)
    
    merged = sorted_left + [pivot] + sorted_right
    print(HIJAU + "  " * level + f"Merged: {merged}" + RESET)
    time.sleep(0.5)
    return merged

# Menu interaktif
arr = []

while True:
    clear()
    print(BIRU + "========================================")
    print("             ALGORITMA QUICK SORT")
    print("========================================" + RESET)

    print("\n=== MENU ===")
    print("1. Masukkan Elemen Array")
    print("2. Tampilkan Array")
    print("3. Quick Sort Ascending")
    print("4. Quick Sort Descending")
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
            print(BIRU + "\nMulai Quick Sort Ascending..." + RESET)
            sorted_arr = quick_sort_visual(arr.copy(), ascending=True)
            print(HIJAU + f"\nArray setelah Quick Sort Ascending: {sorted_arr}" + RESET)
        input("\nTekan Enter untuk kembali...")

    elif pilihan == "4":
        if not arr:
            print(MERAH + "Array masih kosong!" + RESET)
        else:
            print(BIRU + "\nMulai Quick Sort Descending..." + RESET)
            sorted_arr = quick_sort_visual(arr.copy(), ascending=False)
            print(HIJAU + f"\nArray setelah Quick Sort Descending: {sorted_arr}" + RESET)
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