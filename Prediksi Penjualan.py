import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Inisialisasi data
data = {
    'tanggal': ['01/06/2024', '02/06/2024', '03/06/2024', '04/06/2024', '05/06/2024',
                '06/06/2024', '07/06/2024', '08/06/2024', '09/06/2024', '10/06/2024',
                '11/06/2024', '12/06/2024', '13/06/2024', '14/06/2024', '15/06/2024',
                '16/06/2024', '17/06/2024', '18/06/2024', '19/06/2024', '20/06/2024',
                '21/06/2024', '22/06/2024', '23/06/2024', '24/06/2024', '25/06/2024',
                '26/06/2024', '27/06/2024', '28/06/2024', '29/06/2024', '30/06/2024'],
    'nama_produk': ['martabak kacang', 'martabak keju', 'martabak coklat', 'martabak kosongan', 'martabak kacang',
                    'martabak keju', 'martabak coklat', 'martabak kosongan', 'martabak kacang', 'martabak keju',
                    'martabak coklat', 'martabak kosongan', 'martabak kacang', 'martabak keju', 'martabak coklat',
                    'martabak kosongan', 'martabak kacang', 'martabak keju', 'martabak coklat', 'martabak kosongan',
                    'martabak kacang', 'martabak keju', 'martabak coklat', 'martabak kosongan', 'martabak kacang',
                    'martabak keju', 'martabak coklat', 'martabak kosongan', 'martabak kacang', 'martabak keju'],
    'jumlah': [150, 120, 30, 43, 24, 20, 45, 30, 21, 34, 100, 230, 11, 200, 31, 123, 134, 234, 154, 72,
               80, 92, 77, 89, 34, 12, 34, 12, 31, 12],
    'harga_satuan': [5, 3, 1, 3, 4, 3, 4, 6, 8, 6.36, 6.81, 7.26, 7.71, 8.16, 8.61, 9.06, 9.51, 9.96, 10.41, 10.86,
                     11.31, 11.76, 12.21, 12.66, 13.11, 13.56, 14.01, 14.46, 14.91, 15.36],
    'total': [750, 360, 30, 129, 96, 60, 180, 180, 168, 216.28, 681.11, 1670.06, 84.82, 1632.22, 266.94, 1114.52, 1274.49, 2330.9, 1603.31, 782,
              904.89, 1082.02, 940.26, 1126.84, 445.78, 162.73, 476.38, 173.53, 462.24, 184.33]
}

# Membuat DataFrame dari data
df = pd.DataFrame(data)

# Ekstraksi fitur tanggal
df['tanggal'] = pd.to_datetime(df['tanggal'], format='%d/%m/%Y')
df['bulan'] = df['tanggal'].dt.month
df['tahun'] = df['tanggal'].dt.year

# Memisahkan fitur dan target
X = df[['harga_satuan', 'bulan']]
y = df['jumlah']

# Membagi data menjadi data latih dan data uji
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Membuat model regresi linier
model = LinearRegression()

# Melatih model
model.fit(X_train, y_train)

# Melakukan prediksi
y_pred = model.predict(X_test)

# Menghitung mean squared error
mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error:", mse)

# Prediksi untuk bulan-bulan berikutnya dalam tahun yang sama
bulan_terakhir = df['bulan'].max()
tahun_terakhir = df['tahun'].max()
bulan_prediksi = range(bulan_terakhir + 1, 13)
tahun_prediksi = [tahun_terakhir] * len(bulan_prediksi)
tanggal_prediksi = pd.to_datetime(['01/{:02d}/{}'.format(bulan, tahun) for bulan, tahun in zip(bulan_prediksi, tahun_prediksi)])

# Memprediksi jumlah penjualan untuk setiap bulan berikutnya
X_prediksi = pd.DataFrame({'harga_satuan': df['harga_satuan'].mean(), 'bulan': bulan_prediksi})
jumlah_prediksi = model.predict(X_prediksi)


total_prediksi_tahunan = sum(jumlah_prediksi)

print("Total prediksi jumlah penjualan untuk bulan-bulan berikutnya dalam tahun yang sama:", total_prediksi_tahunan)

# Visualisasi data asli dan prediksi
plt.figure(figsize=(10, 6))
plt.plot(df['tanggal'], df['jumlah'], label='Data Asli')
plt.plot(tanggal_prediksi, jumlah_prediksi, 'r--', label='Prediksi')
plt.xlabel('Tanggal')
plt.ylabel('Jumlah')
plt.title('Prediksi Jumlah Penjualan Martabak')
plt.legend()
plt.grid(True)
plt.show()
