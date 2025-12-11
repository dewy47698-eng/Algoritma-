# Program Insertion Sort Interaktif (Versi Lebih Bagus)
print("=== PROGRAM INSERTION SORT INTERAKTIF ===\n")

# Membuat array
angka = [29, 10, 14, 37, 13]

print("Data awal dalam array:")
for idx, val in enumerate(angka):
    print(f"Index {idx} -> {val}")

# Proses Insertion Sort
print("\nProses Insertion Sort dimulai...\n")
for i in range(1, len(angka)):
    key = angka[i]
    j = i - 1
    print(f"➡ Memproses index {i} ({key})")

    # Geser elemen ke kanan sampai posisi yang tepat ditemukan
    while j >= 0 and angka[j] > key:
        print(f"   🔄 Geser index {j} ({angka[j]}) ke index {j+1}")
        angka[j + 1] = angka[j]
        j -= 1

    angka[j + 1] = key
    print("✅ Array setelah memasukkan elemen:")
    for idx, val in enumerate(angka):
        print(f"Index {idx} -> {val}")
    print()

print("=== INSERTION SORT SELESAI 🎉 ===")
print("Data akhir dalam array:")
for idx, val in enumerate(angka):
    print(f"Index {idx} -> {val}")