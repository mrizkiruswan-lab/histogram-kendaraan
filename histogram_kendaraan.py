import matplotlib.pyplot as plt
import numpy as np

# Data
jenis = ['Mobil Penumpang', 'Bus', 'Truk', 'Sepeda Motor']
jumlah = np.array([2333391, 36381, 520051, 9167512])

# Hitung mean dan median
mean_val = np.mean(jumlah)
median_val = np.median(jumlah)

# Membuat grafik bar
plt.bar(jenis, jumlah, color='skyblue', edgecolor='black')

# Membuat kurva lembut (tanpa scipy, pakai numpy polyfit)
x = np.arange(len(jumlah))
coef = np.polyfit(x, jumlah, 3)  # polynomial derajat 3 untuk kurva halus
poly = np.poly1d(coef)
x_smooth = np.linspace(0, len(jumlah) - 1, 200)
y_smooth = poly(x_smooth)
plt.plot(x_smooth, y_smooth, color='blue', linewidth=2, label='Kurva Tren')

# Garis mean dan median (vertikal)
plt.axhline(mean_val, color='red', linestyle='--', linewidth=2, label=f'Mean: {mean_val:,.0f}')
plt.axhline(median_val, color='green', linestyle='--', linewidth=2, label=f'Median: {median_val:,.0f}')

# Menambahkan label dan judul
plt.title('Jumlah Kendaraan Bermotor Menurut Jenis Kendaraan di DKI Jakarta (2024)')
plt.xlabel('Jenis Kendaraan')
plt.ylabel('Jumlah Kendaraan (unit)')

# Menampilkan nilai di atas batang
for i, val in enumerate(jumlah):
    plt.text(i, val + 100000, f'{val:,}', ha='center', fontsize=9)

# Tambahkan legenda
plt.legend()

# Menampilkan grafik
plt.tight_layout()
plt.show()
