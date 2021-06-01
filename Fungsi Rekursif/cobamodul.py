#def faktorial(val):
#    if val == 1:
#        return val
#    else:
#        return val*faktorial(val-1)

#print(faktorial(5))

def perkalian(bil1,bil2):
    if bil2 == 1:
        print(bil1,'+',end="")
        return bil1
    else:
        print(bil1,'+',end="")
        return bil1 +perkalian(bil1,bil2-1)


print(perkalian(2,4))