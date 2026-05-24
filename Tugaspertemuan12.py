#1.
def sapa_nama():
    nama = "Cindy"   # ini adalah variabel lokal
    print("Halo,", nama)

sapa_nama()

# print(nama)  # ini akan error kalau dibuka

#2.
def penjumlahan(x):
    bilangan = 7   # variabel lokal (hanya di dalam fungsi)
    return x + bilangan

hasil = penjumlahan(4)
print(hasil)

# print(bilangan)  # ini akan error kalau dijalankan

#3.
angka = 10   # variabel global (di luar fungsi)

def tambah_lima():
    hasil = angka + 5
    print("Hasilnya:", hasil)

tambah_lima()

#4.
angka = 10   # variabel global

def ubah_angka():
    global angka
    angka = angka + 5   # mengubah variabel global
    print("Di dalam fungsi:", angka)

ubah_angka()
print("Di luar fungsi:", angka)

#5.
def hitung_imt(berat, tinggi):
    # Rumus IMT: Berat (kg) / (Tinggi (m) * Tinggi (m))
    imt = berat / (tinggi * tinggi)
    return imt

# Input dari user (pastikan dikonversi ke float untuk angka desimal)
berat = float(input("Masukkan berat badan (kg): "))
tinggi = float(input("Masukkan tinggi badan (m): "))

# Memanggil fungsi
index_massa_tubuh = hitung_imt(berat, tinggi)
kategori = ["Normal", "Gemuk", "Obesitas"]

# Mengkategorikan nilai IMT berdasarkan standar pada gambar
if index_massa_tubuh <= 25.0:
    print("Index massa tubuh anda adalah ", index_massa_tubuh, "termasuk kategori ", kategori[0])
elif 25.0 < index_massa_tubuh <= 27.0:
    print("Index massa tubuh anda adalah ", index_massa_tubuh, "termasuk kategori ", kategori[1])
else: 
    print("Index massa tubuh anda adalah ", index_massa_tubuh, "termasuk kategori ", kategori[2], ". Anda harus diet!")

#6.
def cek_segitiga(a, b, c):
    if a + b <= c:
        return False
    if b + c <= a:
        return False
    if c + a <= b:
        return False
    return True

print(cek_segitiga(1, 1, 1)) # Output: True (Bisa jadi segitiga)
print(cek_segitiga(1, 1, 3)) # Output: False (Nggak bisa)

#7.
# Versi 1: Pakai "or"
def cek_segitiga_v1(a, b, c):
    if a + b <= c or b + c <= a or c + a <= b:
        return False
    return True

# Versi 2: Paling singkat (Satu baris saja!)
def cek_segitiga_v2(a, b, c):
    return a + b > c and b + c > a and c + a > b

print(cek_segitiga_v2(1,1,1))
print(cek_segitiga_v2(1,1,3))

#8.
def jenis_segitiga(a, b, c):
    if a + b > c and b + c > a and c + a > b: # Cek dulu bisa jadi segitiga gak
        if a == b == c:
            return "Segitiga Sama Sisi"
        elif a == b or b == c or a == c:
            return "Segitiga Sama Kaki"
        else:
            return "Segitiga Sembarang"
    else:
        return "Bukan Segitiga"

print(jenis_segitiga(3, 3, 3)) # Output: Sama Sisi
print(jenis_segitiga(3, 3, 5)) # Output: Sama Kaki
print(jenis_segitiga(3, 4, 5)) # Output: Sembarang

#9.
def faktorial(n):
    # bilangan yang akan difaktorial harus lebih besar dari 0
    if n < 0:
        return None
    # 0! dan 1! nilainya sama (1)
    if n < 2:
        return 1
    
    hasil = 1
    for i in range(2, n + 1):
        hasil = hasil * i
    
    return hasil

n = int(input("Masukkan nilai yang ingin di faktorial: "))
print(n, "! = ", faktorial(n))

#10.
def fibonacci(n):
    if n < 1:
        return None
    if n < 3:
        return 1

    elem_1 = elem_2 = 1
    hasil_jumlah = 0 #untuk menampung hasil dari penjumlahan 2 elemen
    
    for i in range(3, n + 1):
        hasil_jumlah = elem_1 + elem_2 #Proses jumlah
        # Tukar elemen: geser posisi orang tua untuk hitungan berikutnya
        elem_1 = elem_2
        elem_2 = hasil_jumlah
        
    return hasil_jumlah

#test
for i in range(1, 10):
    print(i, "->", fibonacci(i))
    
#11.
def faktorial_rekursif(n):
    # Base Case: Titik berhenti supaya tidak memanggil terus-menerus
    if n <= 1:
        return 1
    # Recursive Case: Fungsi memanggil dirinya sendiri
    else:
        return n * faktorial_rekursif(n - 1)

n = int(input("Masukkan angka: "))
print(f"{n}! = {faktorial_rekursif(n)}")

#12.
def fibonacci(n):
    if n <= 0:
        return None
    if n <= 2:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

n = int(input("Masukkan angka: "))
print(f"Fibonacci ke-{n} = {fibonacci(n)}")
