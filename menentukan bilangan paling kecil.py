angka_1 = int (input("masukan angka pertama "))
angka_2 = int (input("masukan angka kedua "))
angka_3 = int (input("masukan angka kedua "))

if angka_1 < angka_2 & angka_3:
    hasil = "Angka pertama lebih kecil"
if angka_2 < angka_1 & angka_3:
    hasil = "Angka kedua lebih kecil"
else :
    hasil = "Angka ketiga lebih kecil"

print ( hasil )