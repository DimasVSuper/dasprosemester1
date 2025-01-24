from contextlib import nullcontext


def garis():
    print("================================================")
#
# import math  # Modul untuk konstanta dan fungsi matematika, seperti π (pi)
#
# def segitiga(alas, tinggi):
#     return (alas * tinggi) / 2
#
# def persegipanjang(panjang, lebar):
#     return panjang * lebar
#
# def lingkaran(jari_jari):
#     return math.pi * jari_jari ** 2  # π * r^2
#
#
# pilihan = int(input("Pilihan bangun datar :"))
#
# if pilihan == 1:
#     tinggi=int(input("tinggi segitiga : "))
#     alas=int(input("alas segitiga : "))
#     print("luas segitiga adalah : ",segitiga(alas, tinggi))
# elif pilihan == 2:
#     panjang=int(input("panjang persegipanjang : "))
#     lebar=int(input("lebar persegipanjang :"))
#     print("luas persegipanjang : ", persegipanjang(panjang, lebar))
# elif pilihan == 3:
#     jarijari=int(input("jari jari : "))
#     print(f"hasil nya : ", lingkaran(jarijari))
# else:
#     print("salah")


# tugas
import pandas as pd

while True:
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")

    # Cek jika username dan password benar
    if username == "admin" and password == "admin":
        print("Login berhasil!")

        # Daftar untuk menyimpan data barang
        listjenis = []
        listharga = []
        jumlahbeli = []
        subtotal = []

        print("Selamat datang di toko dimas")

        # Memasukkan jumlah jenis barang
        y = int(input("Masukkan jumlah jenis barang: "))

        for i in range(y):
            print("Barang ke -", i + 1)
            # Menambahkan nama barang ke listjenis
            listjenis.append(input("Nama barang: "))
            # Menambahkan harga barang ke listharga dan mengonversinya ke int
            listharga.append(int(input("Harga barang: ")))
            # Menambahkan jumlah beli ke jumlahbeli dan mengonversinya ke int
            jumlahbeli.append(int(input("Jumlah beli: ")))
            # Menghitung subtotal untuk barang tersebut dan menambahkannya ke list subtotal
            subtotal.append(listharga[i] * jumlahbeli[i])

        # Menampilkan hasil
        print("\nDaftar Pembelian:")
        print("No | Nama Barang | Harga Satuan | Jumlah Beli | Subtotal")
        print("-----------------------------------------------")
        for i in range(y):
            print(f"{i+1}  | {listjenis[i]}         | Rp{listharga[i]:,}       | {jumlahbeli[i]}          | Rp{subtotal[i]:,}")

        # Menghitung total pembelian sebelum pajak
        total_pembelian = sum(subtotal)
        print("\nTotal Pembelian Sebelum Diskon: Rp", total_pembelian)
        if total_pembelian >= 100000:
            #Menghitung diskon 10%
            diskon = total_pembelian * 0.1
            totaldiskon = total_pembelian - diskon
        else:
            nullcontext

        # Menghitung total pembelian setelah pajak

        # Menampilkan total pembelian setelah pajak
        print("Total Pembelian Setelah Diskon: Rp", totaldiskon)

        break  # Keluar dari loop jika login berhasil
    else:
        print("Akses ditolak karena username atau password salah")

        # Loop untuk menanyakan apakah ingin mencoba lagi
        while True:
            ulangi = input("Apakah Anda ingin mencoba lagi? (Y/N): ").upper()
            if ulangi == "Y":
                break  # Keluar dari loop login dan meminta input ulang
            elif ulangi == "N":
                print("Terima kasih. Program selesai.")
                break  # Keluar dari loop login
            else:
                print("Input tidak valid. Silakan masukkan 'Y' untuk mencoba lagi atau 'N' untuk keluar.")
        if ulangi == "N":
            break  # Keluar dari loop utama jika memilih tidak ingin mencoba lagi

