import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

url = '/Users/colby/Documents/Lambda/01 Sprint 1/Project/sources/Palmer_Drought_Severity_Index__1895-2016.csv'

water = pd.read_csv(url)

water = water[water['pdsi'] >= -10]

print(water.head())
#print(water['statefips'].value_counts())

sns.scatterplot(x='year', y='pdsi', data=water[(water['statefips'] == 49) & (water['month'] == 1) & (water['countyfips'] == 49049)])
plt.show()
