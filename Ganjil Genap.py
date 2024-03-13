nilai = int (input(" masukan angka "))
#menentukan ganjil genap
if nilai % 2 == 0 :
    artinya = "genap"
else :
    artinya = "ganjil"
#menentukan positif negatif 
if nilai > 0 :
    hasil = "Positif"
if nilai == 0 :
    hasil = "nilai Nol"
else :
    hasil = "negatif"
print ("angka yang anda masukan adalah angka",hasil , "dan termasuk angka", artinya )


