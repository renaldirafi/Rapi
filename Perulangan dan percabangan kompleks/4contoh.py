#buatlah sebuah Program berulang membuat garis horizontal dan vertikal
#pada vertikal baris pertama menunjukkan angka baris
#pada horizontal kolom pertama menunjukkan angka kolom
#total baris atau kolom diinput oleh user
#buatlah menggunakan while true

while True:
    print("===== SELAMAT DATANG =====")
    print("1. Horizontal")
    print("2. Vertikal")
    print("3. Exit")
    x = input("Masukkan Pilihan Anda: ")
    if x == '1':
        a = 1
        y = int(input("Masukkan Jumlah Kolom: "))
        for i in range(1,y*2+2,1):
            for j in range(1,y+1):
                if i == 1:
                    print(a,"",end="")
                    a = a + 1
                elif i%2==1:
                    print("- ",end="")
                else:
                    print("",end="")
            print()
    elif x =="2":
        a=1
        y = int(input("Masukkan Jumlah Baris: "))
        for i in range(1,y+1):
            for j in range(1,y*2+2,1):
                if j ==1:
                    print(a,"",end="")
                    a = a+1
                elif j%2==1:
                    print("| ",end="")
                else:
                    print("",end="")
            print()
    elif x =="3":
        break
    else:
        print("Tidak Terdefinisi")