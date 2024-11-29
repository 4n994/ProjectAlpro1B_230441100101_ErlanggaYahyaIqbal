# TUGAS PRAKTIKUM NOMOR 1
# konversi suhu celcius ke farenheit,reamur dan kelvin
# input suhu dalam celcius 
# float(nilai desimal)
# suhu_celcius = 17

#  suhu_celcius = (input("masukkan celcius: "))
# print("suhucelcius")
suhu_celcius = 17

# Konversi ke Fahrenheit
suhu_fahrenheit = (suhu_celcius * 9/5) + 32

# Konversi ke Reamur
suhu_reamur = (suhu_celcius * 4/5) 

# Konversi ke Kelvin
suhu_kelvin = (suhu_celcius + 273)

# Menampilkan hasil konversi
print("Suhu yang ada didalam fahrenheit", suhu_fahrenheit, "F") 
print("Suhu yang ada didalam Reamur", suhu_reamur, "Re")
print("Suhu yang ada didalam Kelvin", suhu_kelvin, "K" )