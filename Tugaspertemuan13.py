#1.
# membuat tuple
data = ("Cindy", 11, "Palembang")

# menampilkan tuple dan isinya
print("Isi tuple:", data)
print("Elemen ke-0:", data[0])
print("Elemen ke-1:", data[1])
print("Elemen ke-2:", data[2])

#2.
data = ("Cindy", 11, "Palembang")

# menampilkan seluruh isi
print("Isi tuple:", data)

# mengakses elemen
print("Nama:", data[0])

# perulangan
for item in data:
    print(item)

#3.
data = ("Cindy", 17, "Bandung")

# ubah ke list dulu
data_list = list(data)

# modifikasi data
data_list[1] = 11
data_list[2] = "Palembang"

# ubah lagi ke tuple
data = tuple(data_list)

print(data)

#4.
data1 = ("Cindy", 11)
data2 = ("Palembang",)

# len()
print("Jumlah elemen:", len(data1))

# +
gabung = data1 + data2
print("Hasil gabung:", gabung)

# *
ulang = data1 * 2
print("Hasil ulang:", ulang)

# in dan not in
print("Cindy ada di tuple?", "Cindy" in gabung)
print("Bandung tidak ada di tuple?", "Bandung" not in gabung)

#5.
# tuple
data = ("Cindy", 11, "Palembang")

# penugasan simultan
nama, umur, kota = data

print("Nama:", nama)
print("Umur:", umur)
print("Kota:", kota)

#6.
# membuat dictionary
data = {
    "nama": "Cindy",
    "umur": 20,
    "kota": "Palembang",
    "hobi": "scroll TikTok"
}

# menampilkan dictionary
print("Isi dictionary:", data)

# menampilkan tiap nilai
print("Nama:", data["nama"])
print("Umur:", data["umur"])
print("Kota:", data["kota"])
print("Hobi:", data["hobi"])

#7.
# membuat dictionary
data = {
    "nama": "Cindy",
    "umur": 20,
    "kota": "Palembang",
    "hobi": "scroll TikTok"
}

# mengakses isi dictionary
print("Nama:", data["nama"])
print("Umur:", data["umur"])
print("Kota:", data["kota"])
print("Hobi:", data["hobi"])

#8.
# membuat dictionary
data = {
    "nama": "Cindy",
    "umur": 20,
    "kota": "Palembang",
    "hobi": "scroll TikTok"
}

# mengambil semua key
kunci = data.keys()

print("Semua key:", kunci)

# menampilkan satu per satu
for key in data.keys():
    print(key)
    
#9.
# membuat dictionary
barang = {
    "nama_barang": "Buku",
    "harga": 15000,
    "stok": 20,
    "kategori": "Alat Tulis"
}

# mengambil semua value
nilai = barang.values()

print("Semua value:", nilai)

# menampilkan satu per satu
for v in barang.values():
    print(v)
    
#10.
# membuat dictionary
barang = {
    "nama_barang": "Buku",
    "harga": 15000,
    "stok": 20,
    "kategori": "Alat Tulis"
}

# mengambil key dan value sekaligus
data_items = barang.items()

print("Semua item:", data_items)

# menampilkan satu per satu
for key, value in barang.items():
    print(key, ":", value)
    
#11.
# membuat dictionary
barang = {
    "nama_barang": "Buku",
    "harga": 15000,
    "stok": 20
}

# update data
barang.update({
    "harga": 20000,      # ubah harga
    "kategori": "ATK"    # tambah data baru
})

print(barang)

#12.
# membuat dictionary
barang = {
    "nama_barang": "Buku",
    "harga": 15000,
    "stok": 20,
    "kategori": "ATK"
}

# menghapus item terakhir
item_terhapus = barang.popitem()

print("Item yang dihapus:", item_terhapus)
print("Dictionary sekarang:", barang)

#13.
# membuat dictionary
barang = {
    "nama_barang": "Buku",
    "harga": 15000,
    "stok": 20
}

# modifikasi data
barang["harga"] = 18000      # ubah nilai
barang["stok"] = 25          # ubah nilai
barang["kategori"] = "ATK"   # tambah data baru

# hapus salah satu data
del barang["stok"]

print(barang)

#14.
try:
    angka = int(input("Masukkan angka: "))
    hasil = 10 / angka
    print("Hasil:", hasil)
except ValueError:
    print("Input harus berupa angka!")
except ZeroDivisionError:
    print("Tidak bisa dibagi dengan nol!")
finally:
    print("Program selesai")
    
#15.
try:
    angka = int(input("Masukkan angka: "))
    hasil = 10 / angka
    print("Hasil:", hasil)

except (ValueError, TypeError):
    print("Terjadi kesalahan pada input!")

except ZeroDivisionError:
    print("Tidak bisa dibagi dengan nol!")
    
    