import pandas as pd
import matplotlib.pyplot as plt

# Mengubah data menjadi DataFrame pandas
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

df = pd.DataFrame(data)

# Scatterplot
plt.figure(figsize=(10, 6))
for produk in df['nama_produk'].unique():
    subset = df[df['nama_produk'] == produk]
    plt.scatter(subset['tanggal'], subset['jumlah'], label=produk)
plt.xlabel('Tanggal')
plt.ylabel('Jumlah')
plt.title('Scatterplot Jumlah Penjualan per Tanggal')
plt.legend()
plt.show()

# Histogram
plt.figure(figsize=(10, 6))
plt.hist(df['harga_satuan'], bins=10, color='skyblue', edgecolor='black')
plt.xlabel('Harga Satuan')
plt.ylabel('Frekuensi')
plt.title('Histogram Harga Satuan')
plt.show()

# Pie Chart
total_per_produk = df.groupby('nama_produk')['total'].sum()
plt.figure(figsize=(8, 8))
plt.pie(total_per_produk, labels=total_per_produk.index, autopct='%1.1f%%', startangle=140)
plt.title('Pie Chart Total Penjualan per Produk')
plt.show()
