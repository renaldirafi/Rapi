#Anonymous function adalah fungsi tanpa nama
#Lambda merupakan fitur tambahan pada python, bukan fitur utama

def tambah(a,b):
    hasil = a+b
    return hasil
print(tambah(4,7))

tambah= lambda a,b:a+b
print(tambah(4,7))