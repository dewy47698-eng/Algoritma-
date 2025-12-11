# Program Array Satu Dimensi (Menarik dan Interaktif)

print("=== PROGRAM ARRAY SATU DIMENSI ===\n")

# Membuat array
angka = [10, 20, 30, 40, 50]

print("Data awal dalam array:")
for i, value in enumerate(angka):
    print(f"Index {i} -> {value}")

# Menambah data baru
print("\nMenambah data baru ke array...")
angka.append(60)

print("Data setelah ditambah:")
for i, value in enumerate(angka):
    print(f"Index {i} -> {value}")

# Mengakses elemen tertentu
print("\nMengakses elemen array:")
print("Elemen pada index 3 adalah:", angka[3])

# Mengubah nilai
angka[1] = 99
print("\nSetelah mengubah nilai index 1 menjadi 99:")
for i, value in enumerate(angka):
    print(f"Index {i} -> {value}")

print("\n=== PROGRAM SELESAI ===")