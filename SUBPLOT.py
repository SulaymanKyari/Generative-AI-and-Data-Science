# Subplots showing facewash and bathing soap 
# sales from the "company_sales_data"

import matplotlib.pyplot as plt

import pandas as pd

df = pd.read_csv("company_sales_data.csv")

plt.subplot(1, 2, 1) 

plt.plot(df["facewash"], marker = 'o')

plt.title('Facewash')
plt.xlabel('Month',)
plt.ylabel('Sales')
plt.grid()

df = pd.read_csv("company_sales_data.csv")

plt.subplot(1, 2, 2)

plt.plot(df["bathingsoap"], marker = 'o')

plt.title('Bathingsoap')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.grid()

plt.tight_layout(pad=3.0)

plt.show()

