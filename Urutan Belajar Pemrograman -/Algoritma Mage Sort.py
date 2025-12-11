from colorama import Fore, Style, init
init(autoreset=True)

def merge_sort(arr, depth=0):
    indent = "  " * depth
    print(Fore.CYAN + f"{indent}▶ Memproses: {arr}")

    if len(arr) <= 1:
        print(Fore.GREEN + f"{indent}✓ Sudah terurut: {arr}")
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    print(Fore.YELLOW + f"{indent}Membagi menjadi: {left_half} dan {right_half}")

    left_sorted = merge_sort(left_half, depth+1)
    right_sorted = merge_sort(right_half, depth+1)

    merged = merge(left_sorted, right_sorted, depth)
    print(Fore.MAGENTA + f"{indent}✔ Hasil gabung: {merged}")
    return merged


def merge(left, right, depth):
    indent = "  " * depth
    print(Fore.BLUE + f"{indent}Menggabungkan {left} dan {right}")

    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            print(Fore.GREEN + f"{indent}→ Ambil {left[i]} dari kiri")
            result.append(left[i])
            i += 1
        else:
            print(Fore.GREEN + f"{indent}→ Ambil {right[j]} dari kanan")
            result.append(right[j])
            j += 1

    # Tambahkan sisa elemen
    for x in left[i:]:
        print(Fore.GREEN + f"{indent}→ Sisa kiri: {x}")
        result.append(x)

    for x in right[j:]:
        print(Fore.GREEN + f"{indent}→ Sisa kanan: {x}")
        result.append(x)

    return result


# Program Utama
print(Fore.CYAN + "===============================")
print(Fore.GREEN + "    PROGRAM MERGE SORT")
print(Fore.CYAN + "===============================")

# Input user
data_input = input(Fore.YELLOW + "Masukkan angka-angka (pisahkan dengan spasi): ")

data = list(map(int, data_input.split()))

print(Fore.CYAN + "\nProses pengurutan dimulai...\n")
sorted_data = merge_sort(data)

print(Fore.CYAN + "\n===============================")
print(Fore.GREEN + f"Hasil akhir: {sorted_data}")
print(Fore.CYAN + "===============================")
