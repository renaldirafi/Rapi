#perulangan kompleks adalah bentuk per-ulangan di mana di
#dalam suatu perulangan terdapat perulangan lain, sehingga terjadi perulangan bertingkat yang
#mengakibatkan waktu proses semakin lama.

x=int(input("Masukkan tinggi: "))
for i in range(1,x+1):
    for j in range(0,i):
        print("*",end="")
    print()