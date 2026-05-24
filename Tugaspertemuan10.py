#1.
angka = [1, 2, 3, 4, 5]

kuadrat = [x**2 for x in angka]

print(kuadrat)

#2.
data = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(data[0][1])

#3.
data = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for baris in data:
    for nilai in baris:
        print(nilai, end=" ")
        
#4.
def sapa(nama):
    print("Halo", nama)

sapa("Cindy")

#5. Kuiz 1
hasil = [x * 3 for x in range(1, 11) if x % 2 == 0]

print(hasil)

#6. Kuiz 2
data = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for baris in data:
    for nilai in baris:
        print(nilai, end=" ")
        
#7. Kuiz 3
data = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

flatten = [nilai for baris in data for nilai in baris]

print(flatten)

#8. Kuiz 4
def luas_persegi_panjang(panjang, lebar):
    return panjang * lebar

hasil = luas_persegi_panjang(8, 5)
print(hasil)

