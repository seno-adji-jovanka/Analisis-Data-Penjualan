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

# Menambahkan kolom grup berdasarkan setiap 5 hari
df['grup'] = (df.index // 5) + 1



# Visualisasi tabel menggunakan Matplotlib
plt.figure(figsize=(12, 6))
plt.axis('tight')
plt.axis('off')
table = plt.table(cellText=grouped_df.values, colLabels=grouped_df.columns, cellLoc='center', loc='center', colColours=['lightgrey']*len(grouped_df.columns))
table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(1.2, 1.2)
plt.title('Tabel Penjualan Produk per 5 Hari')
plt.show()

# Scatterplot per 5 hari
plt.figure(figsize=(10, 6))
for produk in grouped_df['nama_produk'].unique():
    subset = grouped_df[grouped_df['nama_produk'] == produk]
    plt.scatter(subset['grup'], subset['jumlah'], label=produk)
plt.xlabel('Grup (Per 5 Hari)')
plt.ylabel('Jumlah')
plt.title('Scatterplot Jumlah Penjualan per 5 Hari')
plt.legend()
plt.show()