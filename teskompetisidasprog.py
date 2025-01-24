# 1.

# def hitung_biaya_parkir(jenis, jam_masuk, jam_keluar):
#     lama_parkir = jam_keluar - jam_masuk
#     if lama_parkir <= 0:
#         return "Jam keluar harus lebih besar dari jam masuk."

#     if jenis.lower() == "mobil":
#         biaya = 5000 + max(0, lama_parkir - 1) * 2000
#     elif jenis.lower() == "motor":
#         biaya = 3000 + max(0, lama_parkir - 1) * 1000
#     else:
#         return "Jenis kendaraan tidak valid."

#     return f"Lama parkir: {lama_parkir} jam\nBiaya parkir: Rp {biaya}"

# # Input dari pengguna
# jenis = input("Jenis [Mobil/Motor]: ").strip()
# jam_masuk = int(input("Jam Masuk (24 jam format): "))
# jam_keluar = int(input("Jam Keluar (24 jam format): "))

# print("\nHappy Park")
# print(hitung_biaya_parkir(jenis, jam_masuk, jam_keluar))

# 2. 


def hitung_tarif(kode_buku, jumlah_pinjam):
    # Menentukan tarif berdasarkan kode buku
    tarif_per_buku = {
        'C': 5000,  # Cerpen
        'K': 10000, # Komik
        'N': 20000  # Novel
    }
    
    tarif = tarif_per_buku.get(kode_buku.upper(), 0)
    total_bayar = tarif * jumlah_pinjam
    return total_bayar

def main():
    print("Perpustakaan Negeri Angin")
    nama = input("Nama Penyewa Buku: ")
    jumlah_buku = int(input("Jumlah jenis buku yang dipinjam: "))
    total_pembayaran = 0

    for i in range(1, jumlah_buku + 1):
        print(f"\nBuku ke-{i}")
        kode_buku = input("Kode Buku [C/K/N]: ").upper()
        banyak_pinjam = int(input("Banyak Pinjam: "))
        
        if kode_buku not in ['C', 'K', 'N']:
            print("Kode buku tidak valid. Silakan masukkan ulang.")
            continue
        
        jenis_buku = {
            'C': 'Cerpen',
            'K': 'Komik',
            'N': 'Novel'
        }.get(kode_buku)

        biaya = hitung_tarif(kode_buku, banyak_pinjam)
        total_pembayaran += biaya
        
        print(f"Jenis Buku: {jenis_buku}")
        print(f"Biaya untuk buku ke-{i}: Rp{biaya}")

    print(f"\nTotal pembayaran yang harus dibayar oleh {nama}: Rp{total_pembayaran}")

# Menjalankan program
main()



# from pymongo import MongoClient 

# # Fungsi untuk menghitung tarif
# def hitung_tarif(kode_buku, jumlah_pinjam):
#     # Menentukan tarif berdasarkan kode buku
#     tarif_per_buku = {
#         'C': 5000,  # Cerpen
#         'K': 10000, # Komik
#         'N': 20000  # Novel
#     }
    
#     tarif = tarif_per_buku.get(kode_buku.upper(), 0)
#     total_bayar = tarif * jumlah_pinjam
#     return total_bayar

# # Fungsi utama program
# def main():
#     # Koneksi ke MongoDB
#     client = MongoClient("mongodb://localhost:27017/")  # Sesuaikan dengan URL MongoDB Anda
#     db = client["perpustakaan"]  # Pilih database
#     koleksi_buku = db["buku"]  # Koleksi untuk menyimpan data buku dan peminjaman

#     print("Perpustakaan Negeri Angin")
#     nama = input("Nama Penyewa Buku: ")  # Input nama peminjam
#     jumlah_buku = int(input("Jumlah jenis buku yang dipinjam: "))
#     total_pembayaran = 0
#     detail_buku = []

#     # Proses peminjaman buku
#     for i in range(1, jumlah_buku + 1):
#         print(f"\nBuku ke-{i}")
#         kode_buku = input("Kode Buku [C/K/N]: ").upper()
#         banyak_pinjam = int(input("Banyak Pinjam: "))
        
#         if kode_buku not in ['C', 'K', 'N']:
#             print("Kode buku tidak valid. Silakan masukkan ulang.")
#             continue
        
#         jenis_buku = {
#             'C': 'Cerpen',
#             'K': 'Komik',
#             'N': 'Novel'
#         }.get(kode_buku)

#         biaya = hitung_tarif(kode_buku, banyak_pinjam)
#         total_pembayaran += biaya
        
#         print(f"Jenis Buku: {jenis_buku}")
#         print(f"Biaya untuk buku ke-{i}: Rp{biaya}")
        
#         # Menyimpan detail buku yang dipinjam
#         detail_buku.append({
#             "kode_buku": kode_buku,
#             "jenis_buku": jenis_buku,
#             "banyak_pinjam": banyak_pinjam,
#             "biaya": biaya
#         })

#     print(f"\nTotal pembayaran yang harus dibayar oleh {nama}: Rp{total_pembayaran}")
    
#     # Menyimpan data penyewa dan buku ke MongoDB
#     penyewa_data = {
#         "nama": nama,  # Nama peminjam yang dimasukkan oleh pengguna
#         "total_pembayaran": total_pembayaran,
#         "buku_dipinjam": detail_buku  # Menyimpan informasi buku yang dipinjam
#     }
    
#     # Menyisipkan data penyewa ke koleksi
#     koleksi_buku.insert_one(penyewa_data)
#     print("Data penyewa berhasil disimpan ke MongoDB.")

#     # Menampilkan semua data buku yang dipinjam oleh peminjam yang baru disimpan
#     print("\nInformasi Penyewa yang Tersimpan di MongoDB:")
#     print(penyewa_data)

# # Menjalankan program
# main()

# from pymongo import MongoClient
# import pandas as pd  # Import pandas untuk membuat data frame

# # Fungsi untuk menghitung tarif
# def hitung_tarif(kode_buku, jumlah_pinjam):
#     # Menentukan tarif berdasarkan kode buku
#     tarif_per_buku = {
#         'C': 5000,  # Cerpen
#         'K': 10000, # Komik
#         'N': 20000  # Novel
#     }
    
#     tarif = tarif_per_buku.get(kode_buku.upper(), 0)
#     total_bayar = tarif * jumlah_pinjam
#     return total_bayar

# # Fungsi utama program
# def main():
#     # Koneksi ke MongoDB
#     client = MongoClient("mongodb://localhost:27017/")  # Sesuaikan dengan URL MongoDB Anda
#     db = client["perpustakaan"]  # Pilih database
#     koleksi_buku = db["buku"]  # Koleksi untuk menyimpan data buku dan peminjaman

#     print("Perpustakaan Negeri Angin")
#     nama = input("Nama Penyewa Buku: ")  # Input nama peminjam
#     jumlah_buku = int(input("Jumlah jenis buku yang dipinjam: "))
#     total_pembayaran = 0
#     detail_buku = []

#     # Proses peminjaman buku
#     for i in range(1, jumlah_buku + 1):
#         print(f"\nBuku ke-{i}")
#         kode_buku = input("Kode Buku [C/K/N]: ").upper()
#         banyak_pinjam = int(input("Banyak Pinjam: "))
        
#         if kode_buku not in ['C', 'K', 'N']:
#             print("Kode buku tidak valid. Silakan masukkan ulang.")
#             continue
        
#         jenis_buku = {
#             'C': 'Cerpen',
#             'K': 'Komik',
#             'N': 'Novel'
#         }.get(kode_buku)

#         biaya = hitung_tarif(kode_buku, banyak_pinjam)
#         total_pembayaran += biaya
        
#         print(f"Jenis Buku: {jenis_buku}")
#         print(f"Biaya untuk buku ke-{i}: Rp{biaya}")
        
#         # Menyimpan detail buku yang dipinjam
#         detail_buku.append({
#             "kode_buku": kode_buku,
#             "jenis_buku": jenis_buku,
#             "banyak_pinjam": banyak_pinjam,
#             "biaya": biaya
#         })

#     print(f"\nTotal pembayaran yang harus dibayar oleh {nama}: Rp{total_pembayaran}")
    
#     # Menyimpan data penyewa dan buku ke MongoDB
#     penyewa_data = {
#         "nama": nama,  # Nama peminjam yang dimasukkan oleh pengguna
#         "total_pembayaran": total_pembayaran,
#         "buku_dipinjam": detail_buku  # Menyimpan informasi buku yang dipinjam
#     }
    
#     # Menyisipkan data penyewa ke koleksi
#     koleksi_buku.insert_one(penyewa_data)
#     print("Data penyewa berhasil disimpan ke MongoDB.")

#     # Menampilkan data buku yang dipinjam dalam bentuk DataFrame
#     buku_df = pd.DataFrame(detail_buku)  # Mengonversi list of dict ke dalam DataFrame pandas
#     print("\nInformasi Buku yang Dipinjam:")
#     print(buku_df.to_string(index=False))  # Menampilkan DataFrame tanpa index
    
#     # Menampilkan informasi lengkap tentang peminjam
#     print("\nInformasi Penyewa yang Tersimpan di MongoDB:")
#     print(f"Nama: {penyewa_data['nama']}")
#     print(f"Total Pembayaran: Rp{penyewa_data['total_pembayaran']}")
#     print("\nDetail Buku yang Dipinjam:")
#     print(buku_df.to_string(index=False))  # Menampilkan tabel yang lebih rapi

# # Menjalankan program
# main()




