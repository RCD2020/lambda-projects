import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

url = 'sources/archive/indexData.csv'
pres_url = 'https://raw.githubusercontent.com/awhstin/Dataset-List/master/presidents.csv'
pres_url_edit = 'sources/pres.1.csv'

stock = pd.read_csv(url)

nya = stock[(stock['Index'] == 'IXIC')]

pull_year = lambda date : int(date.split('-')[0])

nya['Year'] = nya['Date'].apply(pull_year)



party = pd.read_csv(pres_url_edit)


previous = 528
for x in range(1965, 2022):
    try:
        sme = int(nya[nya['Year'] == x]['Adj Close'].tail(1))
        party.loc[party['year'] == x, 'adj_close'] = sme
        party.loc[party['year'] == x, 'change'] = round(sme - previous, 2)
        previous = sme
    except:
        pass

print(party[party['party'] == 'Republican']['change'].sum())
print(party[party['party'] == 'Democratic']['change'].sum())