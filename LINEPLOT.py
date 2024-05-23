# Line plot showing the total profit for all months 
# from the "company_sales_data"  

import matplotlib.pyplot as plt

import pandas as pd

df = pd.read_csv('company_sales_data.csv')

plt.plot(df["total_profit"], marker = 'o')

plt.title("TOTAL PROFIT",)
plt.xlabel('Month')
plt.ylabel('Total_profit')
plt.grid()

plt.show()



