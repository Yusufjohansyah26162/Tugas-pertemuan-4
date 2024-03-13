sisi_a = int (input("masukan angka sisi A "))
sisi_b = int (input("masukan angka sisi B "))
sisi_c = int (input("masukan angka sisi C "))

if sisi_a == sisi_b == sisi_c :
    hasil = " Segitiga Sama Sisi"
elif sisi_a == sisi_b and sisi_a != sisi_c :
    hasil = " Segitiga Sama Kaki"
else :
    hasil = " Segitiga sembarang "

print(hasil)
