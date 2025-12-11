# ==========================================================
#                PROGRAM SEARCHING 
# ==========================================================

# Warna teks
class Color:
    HEADER = "\033[95m"
    BLUE = "\033[94m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    CYAN = "\033[96m"
    END = "\033[0m"


print(Color.HEADER + "========== PROGRAM SEARCHING ==========\n" + Color.END)


# ----------------------------------------------------------
#                LINEAR SEARCH (pemeriksaan 1 per 1)
# ----------------------------------------------------------
def linear_search(data, target):
    print(Color.BLUE + "===== LINEAR SEARCH =====" + Color.END)
    print(Color.CYAN + f"Mencari nilai: {target}\n" + Color.END)

    for i in range(len(data)):
        print(Color.YELLOW + f"👉 Memeriksa indeks {i} → {data[i]}" + Color.END)

        if data[i] == target:
            print(Color.GREEN + f"\n✔ Data ditemukan pada indeks {i}" + Color.END)
            print(Color.BLUE + "-"*40 + Color.END)
            return i

    print(Color.RED + "\n✘ Data tidak ditemukan" + Color.END)
    print(Color.BLUE + "-"*40 + Color.END)
    return -1


# ----------------------------------------------------------
#               BINARY SEARCH (lebih cepat)
# ----------------------------------------------------------
def binary_search(data, target):
    print(Color.BLUE + "\n===== BINARY SEARCH =====" + Color.END)
    print(Color.CYAN + f"Mencari nilai: {target}\n" + Color.END)

    kiri = 0
    kanan = len(data) - 1

    while kiri <= kanan:
        mid = (kiri + kanan) // 2
        print(Color.YELLOW + f"🔎 Mid {mid} → {data[mid]}" + Color.END)

        if data[mid] == target:
            print(Color.GREEN + f"\n✔ Data ditemukan pada indeks {mid}" + Color.END)
            print(Color.BLUE + "-"*40 + Color.END)
            return mid
        elif data[mid] < target:
            print(Color.CYAN + f"{data[mid]} < {target} → geser ke kanan\n" + Color.END)
            kiri = mid + 1
        else:
            print(Color.CYAN + f"{data[mid]} > {target} → geser ke kiri\n" + Color.END)
            kanan = mid - 1

    print(Color.RED + "✘ Data tidak ditemukan" + Color.END)
    print(Color.BLUE + "-"*40 + Color.END)
    return -1


# ----------------------------------------------------------
#                   CONTOH PENGGUNAAN
# ----------------------------------------------------------

data1 = [10, 20, 30, 40, 50]
linear_search(data1, 40)

data2 = [5, 10, 15, 20, 25, 30, 35]
binary_search(data2, 25)

print(Color.HEADER + "\n========== PROGRAM SELESAI ==========" + Color.END)
