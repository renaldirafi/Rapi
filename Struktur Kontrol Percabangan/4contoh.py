#pada sebuah Sekolah dasar akan diadakan sebuah lomba estafet karung
#para guru membagikan kelompok untuk berdasarkan kelas dari kelas 1-6 dan nomor absen
#jika setiap kelas memiliki 20 siswa bantulah siswa untuk mengetahui kelompoknya
#berikut pembagian kelompoknya
#1. jika kelas 1-2 memiliki nomor absen 1-10 maka masuk ke kelompok 1 
#dan nomor absen 11-20 masuk kelompok 2
#2. jike kelas 3-4 memiliki nomor absen 1-10 maka masuk ke kelompok 3
#dan nomor absen 11-20 masuk kelompok 4
#3. jike kelas 5-6 memiliki nomor absen 1-10 maka masuk ke kelompok 5
#4. karna guru hanya membuat 5 kelompok maka untuk kelas 5-6 dengan nomor absen 11-20
#akan dibagi rata kesetiap kelompok 1-5

print("==== KELOMPOK LOMBA KARUNG ====")
x= input("Masukkan Nama Anda: ")
a= int(input("Anda Kelas Berapa: "))
b= int(input("Nomor Absen Anda: "))
if a<=2:
    if b <= 10:
        print("Kamu Masuk Kelompok 1")
    elif b > 10 and b <= 20:
        print("Kamu Masuk Kelompok 2")
elif a>2 and a<=4:
    if b <= 10:
        print("Kamu Masuk Kelompok 3")
    elif b >10 and b <= 20:
        print("Kamu Masuk Kelompok 4")
elif a>4 and a<=6:
    if b <= 10:
        print("Kamu Masuk Kelompok 5")
    elif b>10 and b<=12:
        print("Kamu Masuk Kelompok 1")
    elif b>12 and b<=14:
        print("Kamu Masuk Kelompok 2")
    elif b>14 and b<=16:
        print("Kamu Masuk Kelompok 3")
    elif b>16 and b<=18:
        print("Kamu Masuk Kelompok 4")
    elif b>18 and b <=20:
        print("Kamu masuk kelompok 5")
    
