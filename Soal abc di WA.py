angka_1 = int (input("masukan angka pertama "))
angka_2 = int (input("masukan angka kedua "))
angka_3 = int (input("masukan angka ketiga "))
#menentukan satu angka terbesar 
if angka_1 == angka_2 == angka_3 :
    hasil1 = "ketiga angka sama besar"
elif angka_1 > angka_2 & angka_3:
    hasil1 = "Angka pertama yang terbesar"
elif angka_2 > angka_1 & angka_3:
    hasil1 = "Angka kedua yang terbesar"
elif angka_3 > angka_1 & angka_2:
    hasil1 = "Angka ketiga yang terbesar"

#menentukan 2 angka sama besar 
elif angka_1 == angka_2 > angka_3 :
    hasil = "dan angka kesatu serta kedua sama besar dan lebih besar dari angka ketiga"
elif angka_1 == angka_3 > angka_2 :
    hasil = "dan angka kesatu serta ketiga sama besar dan lebih besar dari angka kedua"
elif angka_2 == angka_3 > angka_1 :
    hasil = "dan angka kedua serta ketiga sama besar dan lebih besar dari angka kesatu"
else :
    hasil = "tidak ada angka yang sama besar"


print (hasil1,hasil )
