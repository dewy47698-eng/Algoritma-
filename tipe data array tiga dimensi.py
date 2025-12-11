import random
import time
import os

# ---------- Fungsi Warna ----------
class Color:
    RED = "\033[91m"
    GREEN = "\033[92m"
    CYAN = "\033[96m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    MAGENTA = "\033[95m"
    RESET = "\033[0m"

# ---------- Animasi Loading ----------
def loading(text="Memuat"):
    print(Color.CYAN, end="")
    for i in range(3):
        print(f"{text}{'.' * (i+1)}", end="\r")
        time.sleep(0.35)
    print(Color.RESET, end="")

# ---------- Membuat Array 3D ----------
def create_3d_array(depth, rows, cols):
    return [[[random.randint(0, 9) for _ in range(cols)] for _ in range(rows)] for _ in range(depth)]

# ---------- Tampilkan Layer dengan Warna ----------
def show_layer(layer, index):
    print(f"{Color.YELLOW}=== LAYER {index} ==={Color.RESET}")
    for row in layer:
        for val in row:
            color = random.choice([Color.RED, Color.GREEN, Color.BLUE, Color.MAGENTA])
            print(color + str(val) + Color.RESET, end="  ")
        print()
    print()

# ---------- Ringkasan Layer ----------
def summary(layer, index):
    flat = [v for row in layer for v in row]
    print(f"{Color.CYAN}Ringkasan Layer {index}:{Color.RESET}")
    print(f"  ✔ Minimum : {min(flat)}")
    print(f"  ✔ Maksimum: {max(flat)}")
    print(f"  ✔ Rata2   : {sum(flat)/len(flat):.2f}")
    print(f"  ✔ Jumlah  : {sum(flat)}\n")

# ---------- Program Utama ----------
def main():
    os.system("cls" if os.name == "nt" else "clear")

    print(Color.GREEN + "=== PROGRAM 3D ARRAY MENARIK ===" + Color.RESET)
    depth, rows, cols = 3, 4, 5

    print("\nMembuat array 3D secara acak...")
    loading()

    arr3d = create_3d_array(depth, rows, cols)

    # Tampilkan semua layer
    for d in range(depth):
        show_layer(arr3d[d], d)
        summary(arr3d[d], d)

    # Ambil koordinat tertentu
    print(Color.MAGENTA + "Cek nilai pada posisi tertentu" + Color.RESET)
    r = random.randint(0, rows - 1)
    c = random.randint(0, cols - 1)
    d = random.randint(0, depth - 1)

    print(f"Posisi acak dipilih -> Depth={d}, Row={r}, Col={c}")
    print(f"Nilainya adalah: {Color.YELLOW}{arr3d[d][r][c]}{Color.RESET}")

    print("\n" + Color.GREEN + "=== Program Selesai ===" + Color.RESET)

main()