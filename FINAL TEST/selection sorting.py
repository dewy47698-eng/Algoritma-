# Program Selection Sort dalam Python

def selection_sort(data):
    # Loop untuk setiap posisi dalam list
    for i in range(len(data)):
        # Anggap elemen saat ini sebagai yang terkecil
        min_index = i
        
        # Cari elemen terkecil di sisa list
        for j in range(i + 1, len(data)):
            if data[j] < data[min_index]:
                min_index = j
        
        # Tukar elemen terkecil dengan elemen pada posisi saat ini
        data[i], data[min_index] = data[min_index], data[i]
    
    return data


# Contoh penggunaan
angka = [64, 25, 12, 22, 11]
print("Sebelum di-sort :", angka)

hasil = selection_sort(angka)
print("Setelah di-sort :", hasil)