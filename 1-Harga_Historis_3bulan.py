# 1. Harga Historis Saham 3 bulan

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

sb.set(style = 'darkgrid')

df_xl = pd.read_csv('EXCL.JK.csv', parse_dates = ['Date'])
df_smartfren = pd.read_csv('FREN.JK.csv', parse_dates = ['Date'])
df_indosat = pd.read_csv('ISAT.JK.csv', parse_dates = ['Date'])
df_telkom = pd.read_csv('TLKM.JK.csv', parse_dates = ['Date'])

plt.figure('Telco Stock Figures', figsize = (13,9))
plt.plot(df_xl['Date'], df_xl['Close'], color = 'green', label = 'PT XL Axiata Tbk')
plt.plot(df_smartfren['Date'], df_smartfren['Close'], color = 'cyan', label = 'PT Smartfren Telecom Tbk')
plt.plot(df_indosat['Date'], df_indosat['Close'], color = 'blue', label = 'PT Indosat Tbk')
plt.plot(df_telkom['Date'], df_telkom['Close'], color = 'red', label = 'PT Telekomunikasi Indonesia Tbk')
plt.grid(True) 
plt.title('Harga Historis Saham Provider Telco Indonesia')
plt.xlabel('Tanggal')
plt.ylabel('Rupiah (IDR)')
plt.xticks(rotation = 45)

label = ['PT XL Axiata Tbk', 'PT Smartfren Telecom Tbk', 'PT Indosat Tbk', 'PT Telekomunikasi Indonesia Tbk']
plt.legend(label, loc = 0)
plt.tight_layout()

plt.show()