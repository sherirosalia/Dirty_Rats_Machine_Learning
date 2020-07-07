import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt


df=pd.read_csv('csv_files/imp_feat.csv')
# print(df.head())
df=df[df['1']>.007]

df.plot.bar(x='0', y='1')

# plt.show()



