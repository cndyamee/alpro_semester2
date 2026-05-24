#1.
nama = input("Masukkan nama kamu: ")
print ("Halo nama saya", nama)

#2.
umur = input("Masukkan umur kamu: ")
print ("Umur saya", umur, "tahun")

#3.
angka = input ("Masukkan angka: ")
print ("Kamu memasukkan: ", angka)

hasil = angka + angka
print ("Jika dijumlahkan hasilnya: ", hasil)

#4.
nilai = float(input("Masukkan nilai desimal: "))
print ("Nilai yang kamu masukkan adalah: ", nilai)

#5.
alas   = float(input("Masukkan panjang alas: "))
tinggi = float(input("Masukkan panjang tinggi: "))
hypo   = (alas**2 + tinggi**2) **0.5
print ("Panjang sisi segitiga adalah: ", hypo)

#6.
alas   = float(input("Masukkan panjang alas: "))
tinggi = float(input("Masukkan panjang tinggi: "))
print ("Panjang sisi miring segitiga adalah: ",
       round((alas**2 + tinggi**2) **0.5, 2))

#7.
nama_depan    = input("Masukkan nama depan: ")
nama_belakang = input("Masukkan nama belakang: ")
nama_lengkap  = nama_depan + " " + nama_belakang
print("Nama lengkap saya adalah: " + nama_lengkap)

#8.
kata = input("Masukkan sebuah kata: ")
print("Hasil replikasi: ", kata * 3)

#9.
angka = 25
teks  = str(angka)
print("Nilai setelah dikonversi menjadi string adalah: ", teks)

#10.
angka = 20
nama  = "Cindy"
nilai = 9.5
print(type(angka))
print(type(nama))
print(type(nilai))

#11.kuiz7
a = float(input("Masukkan nilai a: "))
b = float(input("Masukkan nilai b: "))

print("Hasil penjumlahan: ", a + b)
print("Hasil pengurangan: ", a - b)
print("Hasil pembagian  : ", a / b)
print("Hasil perkalian  : ", a * b)

print("Selamat kamu sudah pintar matematika")

#12.kuiz8
#meminta input dari user
x = float(input("Masukkan nikai x: "))
step1 = 1.0 / x
step2 = 1.0 / (x + step1)
step3 = 1.0 / (x + step2)
y = 1.0 / (x + step3)

#menampilkan hasil
print("Hasil dari variabel y adalah: ", y)

#13.kuiz9
jam    = int(input("Waktu mulai (jam): "))
menit  = int(input("Waktu mulai (menit): "))
durasi = int(input("Waktu mulai (durasi): "))

# 1. Tambahkan durasi ke menit yang sudah ada
total_menit = menit + durasi

# 2. Hitung tambahan jam dari total menit(menggunakan pembagian bulat //)
tambahan_jam = total_menit // 60

# 3. Hitung sisa menit setelah diambil jamnya (menggunakan modulo %)
menit_akhir = total_menit % 60

# 4. Hitung jam akhir dan gunakan modulo 24 agar jika lewat tengah malam kembali ke 0
jam_akhir = (jam + tambahan_jam) % 24

print(f"Acara akan segera berakhir pukul {jam_akhir:02d}:{menit_akhir:02d}")



