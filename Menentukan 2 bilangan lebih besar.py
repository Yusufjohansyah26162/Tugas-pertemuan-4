angka_1 = int (input("masukan angka pertama "))
angka_2 = int (input("masukan angka kedua "))
angka_3 = int (input("masukan angka ketiga "))

if angka_1 > angka_2 and angka_1 > angka_3 :
    hasil = "angka kesatu paling besar"
elif angka_2 > angka_1 and angka_2 > angka_3 :
    hasil = "angka kedua paling besar"
elif angka_3 > angka_1 and angka_3 > angka_2 :
      hasil = "angka ketiga paling besar"
elif angka_1 == angka_2 and angka_1 > angka_3 :
     hasil = " angka kesatu dan kedua sama besar dan lebih besar dari angka ketiga"
elif angka_2 == angka_3 and angka_2 > angka_1 :
     hasil = " angka kedua dan ketiga sama besar dan lebih besar dari angka kesatu"
elif angka_3 == angka_1 and angka_3 > angka_2 :
     hasil = " angka ketiga dan kesatu sama besar dan lebih besar dari angka kedua"
else:
     hasil = "semua bilangan sama besar"
     
print ( hasil )
