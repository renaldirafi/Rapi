#Buatlah sebuah dictionary yang berisi angka dari inputan user
#keynya merupakan angka dari inputan user dari besar ke kecil dan valuenya merupakan 
#hasil dari key dikali 3

inp = int(input("Masukkan Angka: "))
kamus = dict()
for nilai in range(inp,0,-1):
    kamus[nilai] = nilai *3

print(kamus)