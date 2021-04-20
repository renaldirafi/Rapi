#andi adalah seorang panitia dari sebuah lomba dan akan mengumumkan pemenang lomba makan pisang
#tetapi hasil dari lomba tersebut sangat tidak rapi.
#isi dari hasil itu adalah "Juara 1 adalah putri Juara 2 adalah putra Juara 3 adalah dendi"
#andi meminta kamu untuk mengubah hasil tersebut menjadi rapi melalui list

kalimat = "Juara 1 adalah Putri Juara 2 adalah putra Juara 3 adalah dendi"
daftar = kalimat.split("Juara ")
print("===== PEMENANG LOMBA MAKAN PISANG =====")
for i in daftar:
    if i == '':
        continue
    else:
        print("Juara", i)
