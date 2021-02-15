#Seorang Mahasiswa sedang mengantri giliran di sebuah rumah sakit.
#tepat disebelah tempat ia duduk ada sebuah timbangan berat badan
#dan pengukur tinggi badan. setelah menimbang dan mengukur ia ingin tahu
#apakah dia memiliki berat badan ideal atau tidak. karena ia sedang di rumah sakit
#ia meminta aku untuk menghitung berat badan ideal menggunakan BMI(Body Mass Index)
#diketahui BMI<18.5 = Kekurangan Berat Badan 
#BMI 18.5 - 24.9 = Normal (Ideal)
#BMI 25.0 - 29.9 = Kelebihan Berat Badan
#BMI => 30.0 = Kegemukan (Obesitas)

#x = berat badan user
#y = tinggi badan user

x= float(input("Masukkan Berat Anda(Kg): "))
y= float(input("Masukkan Tinggi anda(m): "))
BMI= x/(y**2)
print("Nilai BMI anda Adalah ", BMI)
