#1.
while True:
    print("nyangkut di perulangan tak hingga")

#2.
counter = 5
while counter > 2:
    print(counter)
    counter -= 1

#3.
angka  = 1
ganjil = 0
genap  = 0

while angka <= 10:
    if angka % 2 == 0:
        genap += 1
    else:
        ganjil += 1
    angka += 1
print("Jumlah angka genap:", genap)
print("Jumlah angka ganjil:", ganjil)

#4.Kuiz 15
secret_number = 777

print("""
+======================================+
| Selamat datang di game saya, muhhle! |
| masukkan suatu angka dan tebak       |
| angka berapa yang saya pilih         |
| untuk kamu.                          |
| Jadi, berapa angka rahasianya?       |
+======================================+  
""")

while True:
    tebakan = int(input("Masukkan tebakan kamu: "))

    if tebakan == secret_number:
        print("Selamat, Muggle kamu bebas sekarang!")
        break
    else:
        print("hahaha! kamu nyangkut deh di loop saya")

#5.
a = 10
b = 25
c = 15
d = 30
e = 20

data     = [a, b, c, d, e]
terbesar = data[0]

for nilai in data:
    if nilai > terbesar:
        terbesar = nilai
print("Nilai terbesar adalah", terbesar)

#6.
n     = 5
hasil = 1

for i in range(n):
    hasil *= 2

print("Hasil 2 pangkat", n, "adalah", hasil)

#7.contoh Break dan continue
#Break
for i in range(1, 6):
    if i == 3:
        break
    print(i)

#Continue
for i in range(1, 6):
    if i == 3:
        continue
    print(i)

#8.Kuiz 16 (implementasi break)
secret_number = 777

print("=== Game Tebal Angka Rahasia ===")

while True:
    tebakan = int(input("Masukkan angka tebakan kamu: "))

    if tebakan == secret_number:
        print("Selamat, Muggle kamu bebas sekarang!")
        break
    else:
        print("hahaha! kamu nyangkut deh di loop saya, coba lagi!")

#9.Kuiz 17 (implementasi continue)
# meminta user memasukkan suatu kata
user_word = input("Masukkan sebuah kata: ")

# ubah ke huruf kapital
user_word = user_word.upper()

#perulangan tiap huruf
for huruf in user_word:
    if huruf in ["A", "I", "U", "E", "O"]:
        continue
    else:
        print(huruf)

#10.
i = 1

while i <=5:
    print(i)
    i += 1
else:
    print("Perulangan selesai")

#11.
for i in range(1, 6):
    print(i)
else:
    print("Perulangan selesai")

#12.
a = 10
b = 5
c = 10

# ekspresi logika
print(a > b)        # True
print(a == b)       # True
print(a != c)       # True
print(a < b)        # False

# menggunakan operator logika
print(a > b and a == c)     # True
print(a > b or b > c)       # True
print(not(a < b))           # True

#13.
# logical
a = True
b = False

print(a and b)      # False
print(a or b)       # True
print(not a)        # False

# Bitwise
a = 5       # 0101
b = 3       # 0011

print(a & b)    # 1  (0001)
print(a | b)    # 7  (0111)
print(a ^ b)    # 6  (0110)
print(~a)       # -6

#14.
a = 8       # 1000 dalam biner

# Geser ke kiri
print(a << 1)   # 16 (10000)

# Geser ke kanan
print(a >> 1)   # 4 (0100)

#15.
x = 4
y = 1

a = x & y
b = x | y
c = ~x
d = x ^ 5
e = x >> 2
f = x << 2

print(a, b, c, d, e, f)

