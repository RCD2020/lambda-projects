import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

url = 'sources/supermarket_sales - Sheet1.csv'

sales = pd.read_csv(url)

print(sales.head())

#female = sales[sales['Gender'] == 'Female']
#male = sales[sales['Gender'] == 'Male']

#member = sales[sales['Customer type'] == 'Member']
#normal = sales[sales['Customer type'] == 'Normal']

fashion = sales[sales['Product line'] == 'Fashion accessories']
food = sales[sales['Product line'] == 'Food and beverages']
electronic = sales[sales['Product line'] == 'Electronic accessories']
sport = sales[sales['Product line'] == 'Sports and travel']
home = sales[sales['Product line'] == 'Home and lifestyle']
health = sales[sales['Product line'] == 'Health and beauty']

print(fashion.describe()[1:2])
print(food.describe()[1:2])
print(electronic.describe()[1:2])
print(sport.describe()[1:2])
print(home.describe()[1:2])
print(health.describe()[1:2])

#print(member['Gender'].value_counts())
#print(normal['Gender'].value_counts())

#print(member.describe())
#print(normal.describe())