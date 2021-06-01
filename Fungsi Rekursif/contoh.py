#sean suka matematika tetapi dia tidak suka perkalian bilangan ganjil yang nilainya besar
#sean meminta kamu untuk membuat program rekursif perkalian bilangan ganjil
#bantulah sean


def ganjil(angka):
    if angka %2==1:
        if angka == 1:
            return angka
        else:
            return angka*ganjil(angka-2)
    else:
        print("Maaf, Yang anda masukkan bukanlah angka ganjil")


angka = int(input("Masukkan Angka Ganjil: "))
print(ganjil(angka))