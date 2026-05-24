#1.
a = 10
b = 5
print(a ==b)            # sama dengan
print(a != b)           # tidak sama dengan
print(a > b)            # lebih besar
print(a < b)            # lebih kecil
print(a >= b)           # lebih besar sama dengan
print(a <= b)           # lebih kecil sama dengan

#2.
while True:
    n = int(input("Masukkan nilai: "))
    print(n >= 100)

#3.
nilai = int(input("Masukkan nilai: "))

if nilai >= 80:
    print("Anda lulus")

#4.
nilai = int(input("Masukkan nilai: "))

if nilai > 90:
    print("Nilai A")
if nilai > 80:
    print("Nilai B")
if nilai > 70:
    print("Nilai C")

#5.
nilai = int(input("Masukkan nilai: "))

if nilai >= 75:
    print("Lulus")
else:
    print("Tidak lulus")

#6.
umur = int(input("Masukkan umur: "))

if umur >= 18:
    print("Dewasa")
elif umur >= 13:
    print("Remaja")
else:
    print("Anak-anak")

#7.
a = int(input("Masukkan angka pertama: "))
b = int(input("Masukkan angka kedua: "))

if a > b:
    print("Angka pertama lebih besar")
elif a < b:
    print("Angka kedua lebih besar")
else:
    print("Kedua angka sama")

#8.Kuiz12
a = int(ainput("Masukkan angka pertama: "))
b = int(ainput("Masukkan angka kedua: "))
c = int(ainput("Masukkan angka ketiga: "))

if a > b and a > c:
    print("Angka terbesar adalah", a)
elif a > b and b > c:
    print("Angka terbesar adalah", b)
else:
    print("Angka terbesar adalah", c)

#9.
a = int(input("Masukkan angka pertama: "))
b = int(input("Masukkan angka kedua: "))
c = int(input("Masukkan angka ketiga: "))

terbesar = max(a, b, c)
print("Angka terbesar adalah: ", terbesar)

#10.Kuiz13
pendapatan = float(input("Masukkan pendapatan bulanan anda: "))
pajak = 0

#mengubah pendapatan bulanan menjadi tahunan
pendapatan_tahun = pendapatan * 12

# menentukan tarif pajak
if pendapatan_tahun <= 60000000:
    pajak = pendapatan_tahun * 0.05
elif pendapatana_tahun <= 250000000:
    pajak = pendapatan_tahun * 0.15
elif pendapatan_tahun <= 500000000:
    pajak = pendapatan_tahun * 0.25
else:
    pajak = pendapatan_tahun * 0.30

print("Pajak penghasilan yang harus anda bayar adalah", pajak, "rupiah")

