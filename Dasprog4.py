# kode_baju = input("Masukan Kode Baju [SP/AD] : ")
# ukuran = input("Masukan Ukuran Baju [S/M] : ")
#
# if kode_baju == "SP" or kode_baju == "sp":
#     merk = "SuperDry"
#     if ukuran == "S" or ukuran == "s":
#         harga = 450000
#     elif ukuran == "M" or ukuran == "m":
#         harga = 500000
#     else:
#         harga = 0
# elif kode_baju == "AD" or kode_baju == "ad":
#     merk = "Adidas"
#     if ukuran == "S" or ukuran == "s":
#         harga = 650000
#     elif ukuran == "M" or ukuran == "m":
#         harga = 700000
#     else:
#         harga = 0
# else:
#     merk = "Anda Salah Input Kode Merk"
#     harga = 0
#
# print("----------------------------")
# print("Merk Baju  :", str(merk))
# print("Harga Baju : Rp.", harga)

# pembeli = input("Input Nama Pembeli : ")
# no_hp = input("Input No. Handphone : ")
# jurusan = input("Input Jurusan [SBY/BL/LMP] : ")
#
# # Proses
# if jurusan == "SBY":
#     namajurusan = "Surabaya"
#     harga = 300000
# elif jurusan == "BL":
#     namajurusan = "Bali"
#     harga = 350000
# else:
#     namajurusan = "Lampung"
#     harga = 500000
#
# # Input Jumlah Beli
# jumlah = int(input("Masukkan Jumlah Beli : "))
#
# # Proses potongan
# if jumlah >= 3:
#     potongan = (jumlah * harga) * 0.1
# else:
#     potongan = 0
#
# total = (jumlah * harga) - potongan
#
# # Cetak Hasil
# print("--------------------------------------------")
# print("          PENJUALAN TIKET BUS")
# print("                  XYZ")
# print("--------------------------------------------")
# print("Nama Pembeli          : " + str(pembeli))
# print("No. Handphone         : " + str(no_hp))
# print("Kode Jurusan yang dipilih : " + str(jurusan))
# print("Nama Kota Tujuan      : " + str(namajurusan))
# print("Harga                 : ", harga)
# print("Jumlah Beli           : ", jumlah)
# print("--------------------------------------------")
# print("Potongan yang didapat : ", potongan)
# print("Total Bayar           : ", total)
#
# ubay = int(input("Masukkan Uang Bayar : "))
# uangkembali = ubay - total
# print("Uang Kembali          : ", uangkembali)

# nis = input("Masukkan NIS: ")
# nama = input("Masukkan Nama: ")
# jurusan = input("Masukkan Kode Jurusan [SI/SIA]: ")
#
# # Proses biaya berdasarkan jurusan
# if jurusan == "SI":
#     nama_prodi = "Sistem Informasi"
#     biaya = 2400000
# elif jurusan == "SIA":
#     nama_prodi = "Sistem Informasi Akuntansi"
#     biaya = 2000000
# else:
#     nama_prodi = "Kode Jurusan Tidak Valid"
#     biaya = 0
#
# # Output hasil
# print("\n--- Hasil Pendaftaran Mahasiswa Baru ---")
# print(f"NIS              : {nis}")
# print(f"Nama Mahasiswa   : {nama}")
# print(f"Program Studi    : {nama_prodi}")
# print(f"Biaya Kuliah     : Rp {biaya:,}")

# Tugas 1
# Input data karyawan
nama = input("Nama Karyawan: ")
golongan = int(input("Masukkan Golongan (1/2/3): "))
pendidikan = input("Masukkan Tingkat Pendidikan (SMA/D1/D3/S1): ")
jam_kerja = int(input("Masukkan Jumlah Jam Kerja: "))

# Gaji pokok
gaji_pokok = 300000

#persentase tunjangan jabatan berdasarkan golongan
if golongan == 1:
    tunjangan_jabatan_persen = 0.05
elif golongan == 2:
    tunjangan_jabatan_persen = 0.10
elif golongan == 3:
    tunjangan_jabatan_persen = 0.15
else:
    tunjangan_jabatan_persen = 0
    print("Golongan tidak valid!")

#persentase tunjangan pendidikan berdasarkan tingkat pendidikan
if pendidikan == "SMA" or pendidikan == "sma":
    tunjangan_pendidikan_persen = 0.025
elif pendidikan == "D1" or pendidikan == "d1" :
    tunjangan_pendidikan_persen = 0.05
elif pendidikan == "D3" or pendidikan == "D3":
    tunjangan_pendidikan_persen = 0.20
elif pendidikan == "S1" or pendidikan == "s1":
    tunjangan_pendidikan_persen = 0.30
else:
    tunjangan_pendidikan_persen = 0
    print("Pendidikan tidak valid!")

#hitung tunjangan jabatan dan tunjangan pendidikan
tunjangan_jabatan = gaji_pokok * tunjangan_jabatan_persen
tunjangan_pendidikan = gaji_pokok * tunjangan_pendidikan_persen

#hitung honor lembur
jam_lembur = max(0, jam_kerja - 8)
honor_lembur = jam_lembur * 3500

#hitung total gaji
total_gaji = gaji_pokok + tunjangan_jabatan + tunjangan_pendidikan + honor_lembur

#tampilkan hasil
print("\n--- Rincian Gaji Karyawan ---")
print(f"Karyawan yang bernama : {nama:}")
print(f"Gaji Pokok            : Rp {gaji_pokok:,}")
print(f"Tunjangan Jabatan     : Rp {tunjangan_jabatan:,}")
print(f"Tunjangan Pendidikan  : Rp {tunjangan_pendidikan:,}")
print(f"Honor Lembur          : Rp {honor_lembur:,}")
print(f"Total Gaji            : Rp {total_gaji:,}")