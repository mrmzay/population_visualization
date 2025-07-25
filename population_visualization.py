import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv("API_SP.POP.TOTL_DS2_en_csv_v2_38144/API_SP.POP.TOTL_DS2_en_csv_v2_38144.csv", skiprows=4)


df = df[['Country Name', '2022']].dropna()
df.columns = ['Country', 'Population']
df = df[df['Population'] > 0]


top10 = df.sort_values(by='Population', ascending=False).head(10)


plt.figure(figsize=(12, 6))
sns.set(style='whitegrid')
sns.barplot(data=top10, x='Country', y='Population', palette='magma')
plt.title('Top 10 Countries by Population (2022)')
plt.xticks(rotation=45)
plt.ylabel('Population')
plt.xlabel('Country')
plt.tight_layout()
plt.show()