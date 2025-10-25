import matplotlib.pyplot as plt

# Data
jenis = ['Mobil Penumpang', 'Bus', 'Truk', 'Sepeda Motor']
jumlah = [2333391, 36381, 520051, 9167512]

# Membuat grafik histogram (bar chart)
plt.bar(jenis, jumlah, color=['skyblue', 'orange', 'green', 'red'])

# Menambahkan label dan judul
plt.title('Jumlah Kendaraan Bermotor Menurut Jenis Kendaraan di DKI Jakarta (2024)')
plt.xlabel('Jenis Kendaraan')
plt.ylabel('Jumlah Kendaraan (unit)')

# Menampilkan nilai di atas batang
for i, val in enumerate(jumlah):
    plt.text(i, val + 100000, f'{val:,}', ha='center', fontsize=9)

# Menampilkan grafik
plt.tight_layout()
plt.show()
