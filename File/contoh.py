#Tono adalah seorang karyawan dari sebuah perusahaan ternama
#suatu ketika tono diberi tugas untuk mencatat penerima email dan menghitung jumlahnya
#tono diberi sebuah file notepad yang isinya banyak sekali
#si tono meminta aku untuk membantu mencatat dan menhitung jumlahnya
#bantulah si tono

nama=input("Masukkan Nama File: ")
baca = open(nama)
total = 0
for line in baca:
    if line.startswith("Received:"):
        total +=1
        line = line.strip().title()
        print(line)
print("Total penerima sebanyak:",total)