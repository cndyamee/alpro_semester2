#1.
def hitung_mundur(lanjut=True):
    print("Siap...")
    print("Mulai...")
    print("Ayo...")

    if not lanjut:
        return

    print("Semangat Belajar!")

hitung_mundur()   # tanpa argumen

#2.
def hitung_mundur(lanjut=True):
    print("Siap...")
    print("Mulai...")
    print("Ayo...")

    if not lanjut:
        return

    print("Semangat Belajar!")

hitung_mundur(False)

#3.
def hitung_kuadrat(angka):
    hasil = angka ** 2
    return hasil

# menyimpan nilai return ke dalam variabel
nilai = hitung_kuadrat(5)

print(nilai)

#4.
def hitung_kuadrat(angka):
    return angka ** 2

# memanggil fungsi tapi tidak menyimpan hasilnya
hitung_kuadrat(5)

#5.
def sapa():
    print("Halo!")
    return

hasil = sapa()
print(hasil)

#6.
def hitung_total(daftar_angka):
    total = 0
    for angka in daftar_angka:
        total += angka
    return total

# Contoh penggunaan
data = [10, 20, 30, 40]
hasil = hitung_total(data)
print("Total:", hasil)

#7.
def penjumlahan_list(lst):
    s = 0
    for elemen in lst:
        s += elemen
    return s

print(penjumlahan_list(7))

#8.
def buat_list(angka):
    hasil = []
    for i in range(1, angka + 1):
        hasil.append(i)
    return hasil

# Contoh penggunaan
data = buat_list(5)
print(data)

#9. Kuiz 23
def tahun_kabisat(tahun):
    # tahun kabisat jika:
    # habis dibagi 4 DAN tidak habis dibagi 100
    # ATAU habis dibagi 400
    if (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0):
        return True
    else:
        return False


data_uji = [1900, 2000, 2016, 1987]
data_hasil = [False, True, True, False]

for i in range(len(data_uji)):
    th = data_uji[i]
    print(th, "->", end=" ")
    hasil = tahun_kabisat(th)
    
    if hasil == data_hasil[i]:
        print("OK")
    else:
        print("Gagal")
        
#10. Kuiz 24
def tahun_kabisat(tahun):
    if (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0):
        return True
    else:
        return False


def hari_didalam_bulan(tahun, bulan):
    if bulan == 2:  # Februari
        if tahun_kabisat(tahun):
            return 29
        else:
            return 28
    elif bulan in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    else:
        return 30


data_uji = [1900, 2000, 2016, 1987]
data_bulan = [2, 2, 1, 11]
data_hasil = [28, 29, 31, 30]

for i in range(len(data_uji)):
    thn = data_uji[i]
    bln = data_bulan[i]
    print(thn, bln, "->", end=" ")
    
    hasil = hari_didalam_bulan(thn, bln)
    
    if hasil == data_hasil[i]:
        print("OK")
    else:
        print("Gagal")
        
#11. Kuiz 25
def tahun_kabisat(tahun):
    if (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0):
        return True
    else:
        return False


def hari_didalam_bulan(tahun, bulan):
    if bulan == 2:
        if tahun_kabisat(tahun):
            return 29
        else:
            return 28
    elif bulan in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif bulan in [4, 6, 9, 11]:
        return 30
    else:
        return None


def hari_pada_tahun(tahun, bulan, hari):
    # validasi bulan
    if bulan < 1 or bulan > 12:
        return None
    
    # validasi hari
    jumlah_hari = hari_didalam_bulan(tahun, bulan)
    if jumlah_hari is None or hari < 1 or hari > jumlah_hari:
        return None
    
    total = hari
    for b in range(1, bulan):
        total += hari_didalam_bulan(tahun, b)
    
    return total


print(hari_pada_tahun(2000, 12, 31))

#12. Kuiz 26
def cek_prima(bilangan):
    # Bilangan prima harus lebih besar dari 1
    if bilangan <= 1:
        return False
    
    # Mengecek pembagi dari 2 hingga akar kuadrat dari bilangan
    for i in range(2, int(bilangan**0.5) + 1):
        if bilangan % i == 0:
            # Jika ditemukan pembagi lain, maka bukan prima
            return False
            
    # Jika tidak ada pembagi yang ditemukan, maka prima
    return True

# Bagian pemanggil fungsi (sesuai template di gambar)
for i in range(1, 20):
    if cek_prima(i + 1):
        print(i + 1, end=" ")
print()

#13. Kuiz 27
def cek_prima(bilangan):
    # Bilangan asli prima harus lebih besar dari 1
    if bilangan <= 1:
        return False
    
    # Mengecek apakah ada pembagi lain antara 2 sampai (bilangan - 1)
    # Kita menggunakan range(2, bilangan)
    for i in range(2, bilangan):
        if bilangan % i == 0:
            # Jika habis dibagi i, berarti bukan prima
            return False
            
    # Jika tidak ada pembagi yang ditemukan, berarti prima
    return True

# Bagian pemanggil fungsi sesuai template pada gambar
for i in range(1, 20):
    if cek_prima(i + 1):
        print(i + 1, end=" ")
print()


#14. Kuiz 28
def Liter100km_ke_mpg(liter):
    # Konstanta berdasarkan instruksi
    meter_per_mil = 1609.344
    liter_per_galon = 3.785411784
    
    # Konversi 100 km ke mil
    mil = 100000 / meter_per_mil
    # Konversi liter ke galon
    galon = liter / liter_per_galon
    
    return mil / galon

def mpg_ke_Liter100km(mpg):
    # Konstanta berdasarkan instruksi
    meter_per_mil = 1609.344
    liter_per_galon = 3.785411784
    
    # 1 mpg berarti 1 mil per 1 galon
    # Konversi 1 mil ke km (dibagi 1000) lalu ke satuan per 100km
    km100 = (meter_per_mil / 1000) / 100
    # Konversi 1 galon ke liter
    liter = liter_per_galon
    
    # Rumus: (Liter / Jarak dalam satuan 100km) / mpg
    return (liter / km100) / mpg

# Uji coba sesuai output yang diharapkan
print(Liter100km_ke_mpg(3.9))
print(Liter100km_ke_mpg(7.5))
print(Liter100km_ke_mpg(10.))
print(mpg_ke_Liter100km(60.3))
print(mpg_ke_Liter100km(31.4))
print(mpg_ke_Liter100km(23.5))

