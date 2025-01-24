# number = [4,5,3,2,1,7,8,9,0]
# sum = 0
#
# for each in number:
#     sum=sum+each
#
# print("Jumlah semuanya : ",sum)

# #1
# angka = 1
# while(angka<=30):
#     print(angka)
#     angka=angka+2

#2
# angka2=50
# while(angka2>=1):
#     print(angka2)
#     angka2=angka2-2
#3
# angka3=3
# while(angka3<=100):
#     print(angka3)
#     angka3=angka3+3

# ulang = 2
# for i in range(ulang):
#     print("Data ke -" + str(i+1))
#     nama=input("Masukan nama anda : ")
#     uts=int(input("Masukan nilai UTS anda : "))
#     uas=int(input("Masukan nilai UAS anda : "))
#     print("nama anda adalah",nama,"nilai uts anda",uts,"nilai uas anda",uas,)
#     print("-------------------- ---------------------------------\n")

#latihan (berdasarkan chatgpt )
# Daftar harga ayam
# harga_ayam = {
#     "D": 2500,  # Dada
#     "P": 2000,  # Paha
#     "S": 1500  # Sayap
# }
#
# # Pajak sebesar 10%
# pajak = 0.10
#
# # Input jumlah jenis potong ayam yang dibeli
# banyak_jenis = int(input("Masukkan banyak jenis potong yang dibeli: "))
#
# # Inisialisasi variabel total
# total_harga = 0
# detail_pembelian = []
#
# # Loop berdasarkan banyaknya jenis potong yang dibeli
# for jenis_ke in range(1, banyak_jenis + 1):
#     print(f"Jenis ke-{jenis_ke}:")
#
#     # Input kode potong ayam
#     kode_potong = input("Masukkan kode potong (D/P/S): ").upper()
#
#     # Cek validitas kode potong
#     if kode_potong in harga_ayam:
#         # Input banyak potong
#         banyak_potong = int(input("Masukkan banyak potong: "))
#
#         # Hitung harga untuk jenis ini
#         harga_satuan = harga_ayam[kode_potong]
#         harga_total = harga_satuan * banyak_potong
#
#         # Tambahkan ke total harga keseluruhan
#         total_harga += harga_total
#
#         # Simpan detail pembelian
#         detail_pembelian.append({
#             "jenis": kode_potong,
#             "harga_satuan": harga_satuan,
#             "banyak_potong": banyak_potong,
#             "harga_total": harga_total
#         })
#     else:
#         print("Kode potong tidak valid! Ulangi input.")
#         jenis_ke -= 1  # Kurangi jenis_ke agar tidak dianggap satu loop
#
# # Hitung pajak
# total_pajak = total_harga * pajak
#
# # Hitung total pembayaran
# total_bayar = total_harga + total_pajak
#
# # Tampilkan hasil
# print("\n===== GEROBAK FRIED CHICKEN =====")
# print("------------------------------------------")
# print("No.  Jenis Potong  Harga Satuan  Banyak Beli  Jumlah Harga")
# print("------------------------------------------")
# for idx, item in enumerate(detail_pembelian, 1):
#     print(
#         f"{idx}    {item['jenis']}            Rp. {item['harga_satuan']}        {item['banyak_potong']}        Rp. {item['harga_total']}")
#
# print("------------------------------------------")
# print(f"Jumlah Bayar: Rp. {total_harga}")
# print(f"Pajak 10%   : Rp. {total_pajak}")
# print(f"Total Bayar : Rp. {total_bayar}"


# latihan
