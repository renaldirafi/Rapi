#Break
#Perintah ini digunakan untuk menghentikan proses perulangan yang sedang terjadi. Biasanya
#disebabkan oleh suatu kondisi tertentu yang diimple-mentasikan menggunakan perintah IF.
#Continue
#Perintah continue menyebabkan proses perulangan kembali ke awal mula, dengan mengabaikan
#statement-statement berikutnya setelah continue.
#Biasanya perintah continue juga diimplementasikan menggunakan perintah IF.


#for i in range(1,11):
 #   if i ==7:
  #      break
   # else:
    #    print(i)

for i in range(1,11):
    if i ==7:
        continue
    else:
        print(i)