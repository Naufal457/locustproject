#print("hello world")


a = 10
x = 5 
panjang = 1000
print("Nilai a = ", a)
print("Nilai a = ", x)
print("Nilai a = ", panjang)

#penamaan
nilai_y = 15 # dengan menggunakan underscore
juta10 = 1000000 #ini boleh
nilaiZ = 17.5 #ini boleh

#Pemanggilan kedua
print("Nilai a = ", a)

#assignment indirect
b = a
print("Nilai b = ", b)
#python -m py_compile Main.py

#tipe data : Angka  satuan (Integer)
data_integer = 1
print("data: ",data_integer, ",bertipe: ", type(data_integer))

#tipe data: angka dengan koma (float)
data_float = 1.5
print("data: ",data_float)

#tipe data string: kumpulan karakter
data_string="ucup"

#tipe data boolean : biner/false(boolean)
data_bool = True #/False

#tipe data khusus
#bilangan kompleks
print("data: ", complex(5,6))

#tipe data dari bahasa C
from ctypes import c_double

data_c_double = c_double(10.5)
 #python episode 6

 #Belajar Casting

data_int = 9
#konversi

data_float = float(data_int)
data_str = str(data_int)
data_bool = bool(data_int)

#mengambil input data user
#data yang dimasukkan pasti bernilai string
data = input ("Masukkan Data: ")
#print("data =",data)

print("data =",data, "type=", type(data))

#jika kita ingin mengambil int, maka 
data_int = int(input("masukkan angka: "))

print("data =",data_int,"type=",type(data_int))

biner = bool(int(input("Masukkan nilai boolean: ")))

print("data =",biner,"type =",type(biner))


#Operasi Matematika

a = 10
b = 3

#Operasi tambah +
hasil = a + b
print(a,'+',b,'=',hasil)

#latihan komparasi dan logika

#Membuat gabungan area rentang dari angka
print ("\n", 10*"=", "\n")

inputUser = float ( input("Masukkan Angka yang bernilai\nkurang dari 3 \natau \nlebih besar dari 10"))

#memeriksa angka kurang dari 3

isKurangDari = (inputUser < 3)
print("Kurang dari 3 =",isKurangDari)

#Memeriksa lebih dari 10 
isLebihDari = (inputUser > 10)
print("Lebih dari 10 =i",isLebihDari)

#Memeriksa Logika OR

isCorrect = isKurangDari or isLebihDari
print ("angka yang anda masukkan:", isCorrect)


#Kasus Irisan pada Bilangan Tersebut
inputUser = float ( input("Masukkan Angka yang bernilai\n Lebih dari 3 \n dan \n Kurang dari 10"))

#Memerika lebih dari 3
isLebihDari = inputUser > 3
print("Lebih dari 3 =",isLebihDari)

#Memerika Kurang dari 10
isLebihDari = inputUser < 10
print("Kurang dari 10 =", isKurangDari)

#Memeriksa Irisan
isCorrect = isKurangDari and isLebihDari
print("Angka yang anda masukan: ", isCorrect)

#Operator Bitwise
az = 9
bz = 5

# bitwise OR (||)
c = a | b
print('\n ==== OR =============')
print ('nilai:', a, ',binary : ',format(a,'08b'))
print ('nilai:', b, ',binary : ',format(b,'08b'))
print('\n ---------------------(|)')
print('nilai: ',c, ', binary:', format(c,'08b'))

# bitwise AND (&)
c = a | b
print('\n ==== AND =============')
print ('nilai:', a, ',binary : ',format(a,'08b'))
print ('nilai:', b, ',binary : ',format(b,'08b'))
print('\n ---------------------(&)')
print('nilai: ',c, ', binary:', format(c,'08b'))

# bitwise XOR (^)

c = a ^ b
print('\n ==== XOR =============')
print ('nilai:', a, ',binary : ',format(a,'08b'))
print ('nilai:', b, ',binary : ',format(b,'08b'))
print('\n ---------------------(^)')
print('nilai: ',c, ', binary:', format(c,'08b'))

# bitwise NOT (^)
c = ~a
print('\n ==== NOT =============')
print ('nilai:', a, ',binary : ',format(a,'08b'))
print('\n ---------------------(~)')
print('nilai: ',c, ', binary:', format(c,'08b'))

# Shift Right (>>)
c = a >> 2
print('\n ==== Shift Right =============')
print ('nilai:', a, ',binary : ',format(a,'08b'))
print('\n ---------------------(~)')
print('nilai: ',c, ', binary:', format(c,'08b'))



# Shift Left (>>)
c = a << 2
print('\n ==== Shift Left =============')
print ('nilai:', a, ',binary : ',format(a,'08b'))
print('\n ---------------------(~)')
print('nilai: ',c, ', binary:', format(c,'08b'))

#Operator Asigment - 14 Kelas Terbuka
# https://youtu.be/49KDyhzgCmA?si=m-yWhfNMZgQBW4R5

#Operasi yang dapat dilakukan dengan penyingkatan
#operasi ditambah dengan assignment

a= 5 #adalah assignment
print ("nilai a =", a)

a += 1 #artinya adalah a = a + 1
print ("nilai a += 1,  nilai a menjadi", a)


a -= 2
print ("nilai a -= 2,  nilai a menjadi", a)

#Pengenalan String

data = "ini adalah string"
print (data)
print (type(data))

# 1. Cara Membuat String

data = 'Menggunakan single quote'
print(data)

data = "Menggunakan double quote"
print(data)

# 2. Menggunakan tanda \

# Membuat tanda ' menjadi string
print('mari shalat jum\'at')
print('g\'day, isn\n\'t it ?')

#backslash
print("C:\\user\\ucup")

#tab
print("ucup\t\t\totong, semakin jauhan")