#Jessica sedang pergi ke sebuah mall di jakarta, ia ingin membeli sebuah baju yang terkenal
#tetapi dia ingin memperkirakan berapa total yang akan dikeluarkannya
#jika harga di ZARA 120.000/baju dan jika membeli 3 mendapatkan diskon 3%
#jika harga di H&M 100.000/baju dan jika membeli 3 mendapat diskon 5%
#jika harga di Champion 150.000/baju dan tidak ada diskon
#bantulah Jessica untuk menghitungnya

print("==== SELAMAT DATANG ====")
print("Pilih Merk yang ingin anda pilih")
print("1. ZARA")
print("2. H&M")
print("3. Champion")
x = int(input("Masukkan Pilihan Anda: "))

if x ==1:
    harga = 120000
    banyak = int(input("Berapa Baju yang ingin anda beli: "))
    if banyak >=3:
        dis = 3 #3%
        def diskon(harga,diskon):
            hasil = harga*banyak - ((harga*banyak*diskon)/100)
            return hasil
        total = diskon(harga,dis)
        print("Jumlah Yang harus dikeluarkan adalah ", total)
    else:
        def diskon(harga):
            hasil= harga*banyak
            return hasil
        total = diskon(harga)
        print("Jumlah Yang harus dikeluarkan adalah ", total)
elif x==2:
    harga = 100000
    banyak = int(input("Berapa Baju yang ingin anda beli: "))
    if banyak >=3:
        dis = 5 #5%
        def diskon(harga,diskon):
            hasil = harga*banyak - ((harga*banyak*diskon)/100)
            return hasil
        total = diskon(harga,dis)
        print("Jumlah Yang harus dikeluarkan adalah ", total)
    else:
        def diskon(harga):
            hasil = harga*banyak
            return hasil
        total = diskon(harga)
        print("Jumlah Yang harus dikeluarkan adalah ", total)
elif x==3:
    harga = 150000
    banyak = int(input("Berapa Baju yang ingin anda beli: "))
    def diskon(harga):
        hasil = harga*banyak
        return hasil
    total = diskon(harga)
    print("Jumlah Yang harus dikeluarkan adalah ", total)
else:
    print("Maaf Pilihan anda tidak ada tersedia")