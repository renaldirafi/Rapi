#Rafi pergi ke sebuah KFC dan ingin membeli ayam goreng
#1 ayam goreng seharga 18000
#setiap pembelian ayam lebih dari 2 akan mendapatkan dikurang 1000 setiap 1 ayam
#Buatlah sebuah program untuk membantu membuat list harga

harga = 18000
total = 0
print("=============== SELAMAT DATANG ===============")
ayam = int(input("Masukkan Jumlah Ayam Yang ingin dibeli: "))
for i in range(1,ayam+1):
    total = total + harga
    harga = harga - 1000
    print (i,"Ayam Harganya",total)

print("Jumlah Yang harus dibayar adalah",total)