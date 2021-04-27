#eng2ind = dict()
#eng2ind['one'] = 'satu'
#print (eng2ind)

#eng2ind = {'one':'satu','two':'dua','three':'tiga','five':'lima'}
#print (len(eng2ind))

kata = 'brontosaurus'
kamus = dict()
for huruf in kata:
    if huruf not in kamus:
        kamus[huruf] = 1
    else:
        kamus[huruf] +=1
print (kamus)