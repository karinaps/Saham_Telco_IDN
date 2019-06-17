# 2. Harga Saham April

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

sb.set(style = 'darkgrid')

df_xl = pd.read_csv('EXCL.JK.csv', parse_dates = ['Date'])
df_xl_04 = df_xl[(df_xl['Date'] > '2019-03-29') & (df_xl['Date'] < '2019-05-01')]

df_smartfren = pd.read_csv('FREN.JK.csv', parse_dates = ['Date'])
df_smartfren_04 = df_smartfren[(df_smartfren['Date'] > '2019-03-29') & (df_smartfren['Date'] < '2019-05-01')]

df_indosat = pd.read_csv('ISAT.JK.csv', parse_dates = ['Date'])
df_indosat_04 = df_indosat[(df_indosat['Date'] > '2019-03-29') & (df_indosat['Date'] < '2019-05-01')]

df_telkom = pd.read_csv('TLKM.JK.csv', parse_dates = ['Date'])
df_telkom_04 = df_telkom[(df_telkom['Date'] > '2019-03-29') & (df_telkom['Date'] < '2019-05-01')]

plt.figure('Telco Stock Figures', figsize = (13,9))
plt.plot(df_xl_04['Date'], df_xl_04['Close'], color = 'green', label = 'PT XL Axiata Tbk')
plt.plot(df_smartfren_04['Date'], df_smartfren_04['Close'], color = 'cyan', label = 'PT Smartfren Telecom Tbk')
plt.plot(df_indosat_04['Date'], df_indosat_04['Close'], color = 'blue', label = 'PT Indosat Tbk')
plt.plot(df_telkom_04['Date'], df_telkom_04['Close'], color = 'red', label = 'PT Telekomunikasi Indonesia Tbk')
plt.grid(True) 
plt.title('Harga Historis Saham Provider Telco Indonesia (April 2019)')
plt.xlabel('Tanggal')
plt.ylabel('Rupiah (IDR)')
plt.xticks(rotation = 45)

label = ['PT XL Axiata Tbk', 'PT Smartfren Telecom Tbk', 'PT Indosat Tbk', 'PT Telekomunikasi Indonesia Tbk']
plt.legend(label, loc = 0)
plt.tight_layout()

plt.show()