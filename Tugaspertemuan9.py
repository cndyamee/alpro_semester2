#1.
def bubble_sort(arr):
    n = len(arr)
    
    for i in range(n):
        for j in range(0, n - i - 1):
            # Tukar kalau elemen sekarang lebih besar dari berikutnya
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Contoh penggunaan
data = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(data)

print("Hasil sorting:", data)

#2.
def bubble_sort(arr):
    n = len(arr)
    
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Tukar posisi
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        
        # Menampilkan proses tiap langkah
        print(f"Langkah ke-{i+1}: {arr}")

# Input dari user
data_input = input("Masukkan angka (pisahkan dengan spasi): ")
data = list(map(int, data_input.split()))

# Proses sorting
bubble_sort(data)

print("Hasil akhir:", data)

#3.
data = [64, 34, 25, 12]

# Mengurutkan dari kecil ke besar
data.sort()
print("Ascending:", data)

# Mengurutkan dari besar ke kecil
data.sort(reverse=True)
print("Descending:", data)

#4.
data = [10, 20, 30, 40]

# Membalik urutan list
data.reverse()

print("Hasil reverse:", data)

#5.
list_1 = [1]       # Baris 1
list_2 = list_1    # Baris 2
list_1[0] = 2      # Baris 3
print(list_2)      # Baris 4

#6.
buah = ["Apel", "Mangga", "Jeruk", "Pisang"]

# Mengambil sebagian data
print(buah[0:2])  # ['Apel', 'Mangga']
print(buah[1:3])  # ['Mangga', 'Jeruk']

#7.
buah = ["Apel", "Mangga", "Jeruk", "Pisang", "Anggur"]

# Menggunakan indeks positif dan negatif
print(buah[1:-1])  # ['Mangga', 'Jeruk', 'Pisang']

#8.
buah = ["Apel", "Mangga", "Jeruk", "Pisang", "Anggur"]

# Menggunakan indeks negatif ke positif
print(buah[-3:3])  # ['Jeruk']

#9.
buah = ["Apel", "Mangga", "Jeruk", "Pisang"]

# Mengambil dari awal sampai sebelum indeks tertentu
print(buah[:2])  # ['Apel', 'Mangga']
print(buah[:3])  # ['Apel', 'Mangga', 'Jeruk']

#10.
buah = ["Apel", "Mangga", "Jeruk", "Pisang"]

# Mengambil dari indeks tertentu sampai akhir
print(buah[1:])  # ['Mangga', 'Jeruk', 'Pisang']
print(buah[2:])  # ['Jeruk', 'Pisang']

#11.
buah = ["Apel", "Mangga", "Jeruk", "Pisang"]

# Mengambil semua elemen
salinan = buah[:]

print("Data asli:", buah)
print("Salinan:", salinan)

#12.
buah = ["Apel", "Mangga", "Jeruk", "Pisang", "Anggur"]

# Menghapus sebagian elemen dengan slicing
del buah[1:3]

print("Hasil:", buah)

#13.
angka = [1, 2, 3, 4, 5]

# Menghapus semua elemen
angka.clear()

print("Hasil:", angka)

#14.
angka = [1, 2, 3, 4, 5]

# Menghapus list sepenuhnya
del angka

# Coba tampilkan
print(angka)

#15.
nama = ["Cindy", "Alya", "Rina"]

print("Cindy" in nama)   # True
print("Budi" in nama)    # False

#16.
nama = ["Cindy", "Alya", "Rina"]

print("Budi" not in nama)   # True
print("Cindy" not in nama)  # False

#17.
my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
largest = my_list[0]

for i in range(1, len(my_list)):
    if my_list[i] > largest:
        largest = my_list[i]

print(largest)

#18.
my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
largest = my_list[0]

for i in my_list:
    if i > largest:
        largest = i

print(largest)

#19.
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
to_find = 5
found = False

for i in range(len(my_list)):
    found = my_list[i] == to_find
    if found:
        break

if found:
    print("Elemen ditemukan pada index ke-", i)
else:
    print("Tidak ada di dalam list")
    
#20. kuiz 21
tebakan = [3, 7, 11, 42, 34, 49]
hasil_undi = [5, 9, 11, 42, 3, 49]
benar = 0

for angka in tebakan:
    if angka in hasil_undi:
        benar += 1

print(f"Anda menebak benar sebanyak: {benar} kali")

#21. kuiz 22
list_awal = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
list_unik = []

for angka in list_awal:
    if angka not in list_unik:
        list_unik.append(angka)

print(f"List asli: {list_awal}")
print(f"List unik: {list_unik}")

