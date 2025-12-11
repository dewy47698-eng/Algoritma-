# Program Bubble Sort Interaktif (Model Lain)
print("=== PROGRAM BUBBLE SORT INTERAKTIF ===\n")

# Membuat array
angka = [64, 34, 25, 12, 22, 11, 90]

print("Data awal dalam array:")
for i, value in enumerate(angka):
    print(f"Index {i} -> {value}")

# Proses Bubble Sort
print("\nProses Bubble Sort dimulai...\n")
n = len(angka)
for i in range(n):
    swapped = False
    print(f"Iterasi ke-{i+1}:")
    for j in range(0, n-i-1):
        print(f"  Membandingkan index {j} ({angka[j]}) dan index {j+1} ({angka[j+1]})...", end=" ")
        if angka[j] > angka[j+1]:
            angka[j], angka[j+1] = angka[j+1], angka[j]
            swapped = True
            print("ditukar!")
        else:
            print("tidak ditukar")
    # Tampilkan array setelah iterasi
    print("Array sekarang:")
    for k, v in enumerate(angka):
        print(f"Index {k} -> {v}")
    print()
    if not swapped:
        print("Tidak ada pertukaran, array sudah terurut.")
        break

print("=== BUBBLE SORT SELESAI ===")
print("Data akhir dalam array:")
for i, value in enumerate(angka):
    print(f"Index {i} -> {value}")