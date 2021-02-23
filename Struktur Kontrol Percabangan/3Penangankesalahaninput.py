#pada sebuah Sekolah dasar akan diadakan sebuah lomba estafet karung
#para guru membagikan kelompok untuk berdasarkan kelas dari kelas 1-6
#berikut pembagian kelompoknya
#1. kelas 1-2 masuk kelompok 1
#2. kelas 3-4 masuk kelompok 2
#3. kelas 5-6 masuk kelompok 3

x= int(input("Anda Berada Kelas Berapa? "))
if x<=2:
    print("Kamu Masuk Di Kelompok 1")
elif x>2 and x<=4:
    print("Kamu masuk di kelompok 2")
elif x>4 and x<=6:
    print("Kamu masuk di kelompok 3")