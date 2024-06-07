import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

# Mengubah data menjadi DataFrame pandas
data = {
    'tanggal': ['01/06/2024', '02/06/2024', '03/06/2024', '04/06/2024', '05/06/2024',
                '06/06/2024', '07/06/2024', '08/06/2024', '09/06/2024', '10/06/2024',
                '11/06/2024', '12/06/2024', '13/06/2024', '14/06/2024', '15/06/2024',
                '16/06/2024', '17/06/2024', '18/06/2024', '19/06/2024', '20/06/2024',
                '21/06/2024', '22/06/2024', '23/06/2024', '24/06/2024', '25/06/2024',
                '26/06/2024', '27/06/2024', '28/06/2024', '29/06/2024', '30/06/2024'],
    'nama_produk': ['mobil', 'roda', 'wiper', 'velg', 'mobil',
                    'roda', 'wiper', 'velg', 'mobil', 'roda',
                    'wiper', 'velg', 'mobil', 'roda', 'wiper',
                    'velg', 'mobil', 'roda', 'wiper', 'velg',
                    'mobil', 'roda', 'wiper', 'velg', 'mobil',
                    'roda', 'wiper', 'velg', 'mobil', 'roda'],
    'jumlah': [150, 120, 30, 43, 24, 20, 45, 30, 21, 34, 100, 230, 11, 200, 31, 123, 134, 234, 154, 72,
               80, 92, 77, 89, 34, 12, 34, 12, 31, 12],
    'harga_satuan': [50000, 3000, 100, 300, 40000, 3000, 400, 600, 800, 636, 681, 726, 771, 816, 861, 906, 951, 996, 1041, 1086,
                     1131, 1176, 1221, 1266, 1311, 1356, 1401, 1446, 1491, 1536],
    'total': [7500000, 360000, 3000, 12900, 960000, 60000, 18000, 18000, 16800, 21600, 68100, 167000, 8482, 163222, 26694, 111452, 127449, 233090, 160331, 78200,
              90489, 108202, 94026, 112684, 44578, 16273, 47638, 17353, 46224, 18433]
}

df = pd.DataFrame(data)

# Mengisolasi data penjualan mobil
mobil_df = df[df['nama_produk'] == 'mobil'].copy()

# Mengonversi tanggal menjadi format datetime
mobil_df['tanggal'] = pd.to_datetime(mobil_df['tanggal'], format='%d/%m/%Y')

# Mengubah tanggal menjadi fitur numerik (ordinal)
mobil_df['tanggal_ordinal'] = mobil_df['tanggal'].apply(lambda x: x.toordinal())

# Menyiapkan data untuk regresi
X = mobil_df[['tanggal_ordinal']]
y = mobil_df['jumlah']

# Membagi data menjadi training dan testing set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Membuat model regresi linear
model = LinearRegression()
model.fit(X_train, y_train)

# Prediksi penjualan mobil hingga akhir tahun
future_dates = pd.date_range(start='01/07/2024', end='31/12/2024', freq='D')
future_dates_ordinal = future_dates.map(lambda x: x.toordinal()).to_numpy().reshape(-1, 1)

# Melakukan prediksi
predictions = model.predict(future_dates_ordinal)

# Membuat DataFrame hasil prediksi
predictions_df = pd.DataFrame({
    'tanggal': future_dates,
    'prediksi_jumlah': predictions
})

# Visualisasi hasil prediksi dan penjualan mobil aktual
plt.figure(figsize=(10, 6))
plt.plot(mobil_df['tanggal'], mobil_df['jumlah'], label='Jumlah Penjualan Aktual', marker='o')
plt.plot(predictions_df['tanggal'], predictions_df['prediksi_jumlah'], label='Prediksi Jumlah Penjualan', linestyle='--', color='red')
plt.xlabel('Tanggal')
plt.ylabel('Jumlah Penjualan')
plt.title('Prediksi Jumlah Penjualan Mobil hingga Akhir Tahun 2024')
plt.legend()
plt.show()