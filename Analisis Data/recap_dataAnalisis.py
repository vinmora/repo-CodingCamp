import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('data.csv')


print("Lima baris pertama data:")
print(df.head())


print("\nInformasi dataset:")
print(df.info())

print("\nStatistik deskriptif:")
print(df.describe())

df.iloc[:, 0].hist(bins=20, edgecolor='black')
plt.xlabel('Nilai')
plt.ylabel('Frekuensi')
plt.title('Distribusi Data')
plt.show()