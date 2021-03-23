#Buat Suatu Program yang mendeteksi jumlah kemunculan suatu kata dalam sebuah kalimat
#kalimat di masukkan oleh inputan user
#dan output yang dihasilkan adalah jumlah kata yang dicari dalam kalimat

kalimat = input("Kalimat yang diinginkan: ")
dicari = input("Kata yang dicari: ")
a = 0
kata = kalimat.split(" ")
for i in kata:
    hasil = i[:len(dicari)]
    x = hasil.count(dicari)
    a =a+x
print('Kata',dicari,"berjumlah",a)
