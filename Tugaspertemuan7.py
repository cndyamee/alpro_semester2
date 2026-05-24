#1.
# Membuat list
buah = ["Apel", "Pisang", "Jeruk", "Mangga"]

# Mengakses elemen pertama (index 0)
print(buah[0])  # Output: Apel

# Mengakses elemen ketiga (index 2)
print(buah[2])  # Output: Jeruk

#2.
peserta = ["Andi", "Budi", "Caca"]

pemenang = peserta[0]
print(f"Pemenangnya adalah {pemenang}") # Output: Pemenangnya adalah Andi

#3.
# Contoh penggunaan fungsi len() pada list
hobi = ["Membaca", "Coding", "Gitar"]

# Menghitung jumlah elemen dalam list
jumlah_hobi = len(hobi)

# Menampilkan hasil
print(jumlah_hobi) # Output: 3

#4.
# Contoh menghapus elemen dari list
buah = ["Apel", "Mangga", "Jeruk", "Pisang"]

# Menggunakan remove()
buah.remove("Mangga")

# Menggunakan pop()
buah.pop(1)

# Menampilkan hasil akhir
print(buah) # Output: ['Apel', 'Pisang']

#5.
# Contoh penggunaan negative indexing
laptop = ["Asus", "Lenovo", "Acer", "MacBook"]

# Mengakses elemen terakhir
terakhir = laptop[-1]

# Mengakses elemen kedua dari belakang
sebelum_terakhir = laptop[-2]

print(terakhir)          # Output: MacBook
print(sebelum_terakhir)  # Output: Acer

#6.
topi_list = [1, 2, 3, 4, 5]

# Langkah 1: Meminta input user untuk mengganti nilai tengah (indeks 2)
topi_list[2] = int(input("Masukkan angka integer: "))

# Langkah 2: Menghapus elemen terakhir pada list
del topi_list[-1]

# Langkah 3: Menampilkan panjang dari list
print(len(topi_list))

print(topi_list)

#7.
# Contoh penggunaan append() dan insert()
hobi = ["Mreading", "Coding"]

# Menggunakan append() untuk menambah di akhir
hobi.append("Gitar")

# Menggunakan insert() untuk menambah di posisi tertentu (index 1)
hobi.insert(1, "Gaming")

print(hobi) 
# Output: ['Mreading', 'Gaming', 'Coding', 'Gitar']

#8.
# append dengan perulangan
data_nilai = []

for i in range(20, 26):
    data_nilai.append(i)

print(data_nilai)

#9.
# insert dengan perulangan
angka = []

for i in range(5, 0, -1):
    angka.insert(0, i * 2)

print(angka)

#10.
# Menukar nilai menggunakan list
my_list = [10, 20]

# Menukar posisi elemen index 0 dengan index 1
my_list[0], my_list[1] = my_list[1], my_list[0]

print(my_list)
# Output: [20, 10]

#11.
# Membalikkan isi list menggunakan perulangan
my_list = [10, 1, 8, 3, 5]
length = len(my_list)

for i in range(length // 2):
    my_list[i], my_list[length - i - 1] = my_list[length - i - 1], my_list[i]

print(my_list)
# Output: [5, 3, 8, 1, 10]

#12.
# List in Action 2: Membalikkan list dengan perulangan
my_list = [10, 1, 8, 3, 5]
length = len(my_list)

# Melakukan perulangan hingga titik tengah list
for i in range(length // 2):
    # Menukar elemen depan dengan elemen belakang yang sesuai
    my_list[i], my_list[length - i - 1] = my_list[length - i - 1], my_list[i]

print(my_list)
# Output: [5, 3, 8, 1, 10]

#.13.Kuiz
# Langkah 1: Membuat list kosong
exo = []
print("Langkah 1: ", exo)

# Langkah 2: Menggunakan append() untuk 4 anggota
exo.append("Suho")
exo.append("Kai")
exo.append("Chanyeol")
exo.append("Sehun")
print("Langkah 2: ", exo)

# Langkah 3: Menggunakan for untuk menambah sisa anggota
sisa_anggota = ["D.O.", "Baekhyun", "Kris", "Lay", "Luhan", "Tao", "Chen"]
for member in sisa_anggota:
    exo.append(member)
print("Langkah 3: ", exo)

# Langkah 4: Menghapus Kris, Luhan, dan Tao
exo.remove("Kris")
exo.remove("Luhan")
exo.remove("Tao")
print("Langkah 4: ", exo)

# Langkah 5: Menggunakan insert() untuk Xiumin di elemen ke-3 dari terakhir
# Karena list berubah-ubah, kita pakai index negatif agar lebih akurat
exo.insert(-2, "Xiumin")
print("Langkah 5: ", exo)

print("Jumlah anggota exo: ", len(exo))
