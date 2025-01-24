import calendar
import datetime
import statistics

# Bagian Input Tahun dan Bulan (Opsional)
# Jika ingin mencetak kalender untuk tahun tertentu:
# yy = int(input("Masukkan tahun: "))
# mm = int(input("Masukkan bulan dalam angka (1-12): "))
# print(calendar.calendar(yy))  # Cetak kalender untuk tahun tertentu
# print(calendar.month(yy, mm))  # Cetak kalender untuk bulan tertentu

#mendapatkan tanggal dan waktu saat ini
hariini = datetime.datetime.now()
tanggal = hariini.date()
waktu = hariini.time()

#menampilkan tanggal dan waktu
print("Hari ini adalah tanggal:", tanggal)
print("Jam sekarang adalah:", waktu.strftime("%H:%M:%S"))  # Format jam lebih rapi

#menghitung rata-rata menggunakan statistics
data = [5, 8, 6, 4]
mean_value = statistics.mean(data)
print("Rata-rata dari data", data, "adalah:", mean_value)


