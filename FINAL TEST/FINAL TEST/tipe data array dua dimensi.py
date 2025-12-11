# Program Array Dua Dimensi (Versi Berbeda & Menarik)

def tampil_matriks(m):
    print("\n=== TAMPILKAN MATRIKS ===")
    for i in range(len(m)):
        for j in range(len(m[i])):
            print(f"{m[i][j]:4}", end=" ")
        print()  # pindah baris

def tambah_baris(m):
    print("\nMenambah baris baru...")
    baris_baru = []
    for x in range(len(m[0])):
        nilai = int(input(f"Masukkan nilai untuk kolom {x}: "))
        baris_baru.append(nilai)
    m.append(baris_baru)

def ubah_nilai(m):
    print("\n=== UBAH NILAI MATRIKS ===")
    b = int(input("Baris yang ingin diubah : "))
    k = int(input("Kolom yang ingin diubah : "))
    nilai_baru = int(input("Nilai baru: "))
    m[b][k] = nilai_baru


# Matriks awal
matriks = [
    [5, 10, 15],
    [20, 25, 30],
    [35, 40, 45]
]

tampil_matriks(matriks)

ubah_nilai(matriks)
tampil_matriks(matriks)

tambah_baris(matriks)
tampil_matriks(matriks)

print("\nPROGRAM SELESAI.")