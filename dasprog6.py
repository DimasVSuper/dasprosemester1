# mylist = ["i","love","python","programming", 2017]
#
# print(mylist[0])
# print(mylist[2])
#
# yourlist=["hello", [1,2,3], "python"]
# print(yourlist[1][0])
# print(yourlist[1][2])
#
# ourlist=['a','b','c']
# print(ourlist[-1])
# print(ourlist[-2])
# print(ourlist[-3])
#
# # mylist[6] error
#
# # mengubah anggota list
# ganjil = [1,3,4,7,9]
# ganjil[2]=5
# print(ganjil)
#
# #mengubah dalam jumlah banyak
# ganjil[2:5]=[11,13,15]
# print(ganjil)
#
# # menambahkkan data pada list
# genap=[2,4,6]
# genap.append(8)
# print(genap)
#
# genap.extend([10,12,14])
# print(genap)

# studi kasus

# list2d = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]

# print("baris pertama, kolom pertama adalah :",list2d[0][0])
# print("baris pertama, kolom kedua adalah :",list2d[0][1])
# print("baris pertama, kolom ketiga adalah :",list2d[0][2])
# print("baris kedua, kolom pertama adalah :",list2d[1][0])
# print("baris kedua, kolom kedua adalah :",list2d[1][1])
# print("baris kedua, kolom ketiga adalah :",list2d[1][2])
# print("baris ketiga, kolom pertama adalah :",list2d[2][0])
# print("baris ketiga, kolom kedua adalah :",list2d[2][1])
# print("baris ketiga, kolom ketiga adalah :",list2d[2][2])

# lamaulang = input("lama ulang : ")
# if 1<=  lamaulang <= 3:
#     for i in range(lamaulang):
#         print("baris ke ",i + 1,":",list2d[i])
# else:
#     print("tidak boleh lebih dari 4 atau di bawah 1")

# lamaulang = int(input("Lama ulang: "))
# if 1 <= lamaulang <= 3:  # Memastikan bahwa input berada dalam batas 1 hingga 3
#     for i in range(lamaulang):
#         print("Baris ke", i + 1, ":", list2d[i])  # Menggunakan list2d untuk mencetak data yang sesuai
# else:
#
#     print("Lama ulang tidak boleh lebih dari 3 atau kurang dari 1.")
import pandas as pd

# Variable yang berulang menggunakan List/matriks
list_nim = []
list_uts = []
list_uas = []
list_total = []
ulang = 2

# Input data
for i in range(ulang):
    print(f"Data Ke - {i + 1}")
    list_nim.append(input("Masukkan Nim Anda: "))
    list_uts.append(int(input("Masukkan Nilai UTS Anda: ")))
    list_uas.append(int(input("Masukkan Nilai UAS Anda: ")))

# Proses menghitung total nilai
for i in range(ulang):
    list_total.append((list_uts[i] + list_uas[i]) / 2)

# Membuat DataFrame
tamu = {
    "NIM": list_nim,
    "UTS": list_uts,
    "UAS": list_uas,
    "Total": list_total
}
datamahasiswa = pd.DataFrame(tamu)

# Cetak DataFrame dengan format rapi
print("=========================================================")
print("Data Mahasiswa")
print("=========================================================")
print(datamahasiswa.to_string(index=False))
print("=========================================================")

#
# for i in range(ulang):
#     print("%s \t %d \t\t %d \t\t %d" % (list_nim[i], list_uts[i], list_uas[i], list_total[i]))
#
# print("=========================================================")

# latihan
# listjenis = [
#              ]
# listharga = [
#     ]
# jumlahbeli = [
#
# ]
# subtotal = [
#
# ]
#
# print("Selamat datang di toko")
# y = int(input("Masukan jenis barang : "))
# for i in range(y):
#     print("Barang ke -",i+1)
#     namabarang = listjenis.append(input("Nama barang :"))
#     listharga.append(input("Harga barang :"))
#     jumlahbeli.append( input("Jumlah beli :"))
#     subtotal.append(subtotal[i] * jumlahbeli[i])



import pandas as pd


# Daftar untuk menyimpan data barang
# listjenis = []
# listharga = []
# jumlahbeli = []
# subtotal = []
#
# print("Selamat datang di toko")
#
# # Memasukkan jumlah jenis barang
# y = int(input("Masukkan jumlah jenis barang: "))
#
# for i in range(y):
#     print("Barang ke -", i + 1)
#     # Menambahkan nama barang ke listjenis
#     listjenis.append(input("Nama barang: "))
#     # Menambahkan harga barang ke listharga dan mengonversinya ke int
#     listharga.append(int(input("Harga barang: ")))
#     # Menambahkan jumlah beli ke jumlahbeli dan mengonversinya ke int
#     jumlahbeli.append(int(input("Jumlah beli: ")))
#     # Menghitung subtotal untuk barang tersebut dan menambahkannya ke list subtotal
#     subtotal.append(listharga[i] * jumlahbeli[i])
#
# # Menampilkan hasil
# print("\nDaftar Pembelian:")
# print("No | Nama Barang | Harga Satuan | Jumlah Beli | Subtotal")
# print("-----------------------------------------------")
# for i in range(y):
#     print(f"{i+1}  | {listjenis[i]}         | Rp{listharga[i]:,}       | {jumlahbeli[i]}          | Rp{subtotal[i]:,}")
#
# # Menghitung total pembelian sebelum pajak
# total_pembelian = sum(subtotal)
# print("\nTotal Pembelian Sebelum Pajak: Rp", total_pembelian)
#
# # Menghitung pajak 10%
# pajak = total_pembelian * 0.1
# # Menghitung total pembelian setelah pajak
# total_setelah_pajak = total_pembelian + pajak
#
# # Menampilkan total pembelian setelah pajak
# print("Pajak 10%: Rp", pajak)
# print("Total Pembelian Setelah Pajak: Rp", total_setelah_pajak)


















