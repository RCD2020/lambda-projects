import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

url = '/Users/colby/Documents/Lambda/01 Sprint 1/Project/sources/games.csv'

chess = pd.read_csv(url)

#print(chess.columns)

chess = chess[['rated', 'turns', 'victory_status', 'winner', 'white_rating', 'black_rating']]


# print(chess['victory_status'].value_counts())
# print(chess['winner'].value_counts())

# outtime = chess[chess['victory_status'] != 'draw']

# print(outtime['winner'].value_counts())

# group1 = chess[:10029]
# group2 = chess[10029:]

chess.loc[chess.index <= 10028, 'white'] = 0
chess.loc[chess.index >= 10029, 'white'] = 1

chess.loc[(chess['white'] == 1) & (chess['winner'] == 'white'), 'won'] = 1
chess.loc[(chess['white'] == 1) & (chess['winner'] != 'white'), 'won'] = 0
chess.loc[(chess['white'] == 0) & (chess['winner'] == 'black'), 'won'] = 1
chess.loc[(chess['white'] == 0) & (chess['winner'] != 'black'), 'won'] = 0

percent_group = chess['white'].value_counts(normalize=True) * 100
# print(percent_group)
# print(chess['won'].value_counts(normalize=True) * 100)

print(f"\033[93m{pd.crosstab(index=chess['white'], columns=chess['won'], margins=True)}\033[00m")


conditional_dist = pd.crosstab(index=chess['white'], columns=chess['won'], margins=True, normalize=True,) * 100
# print(conditional_dist)

from scipy.stats import chi2_contingency
g, p, dof, expctd = chi2_contingency(pd.crosstab(index=chess['white'], columns=chess['won']))

print('\n\033[31m\033[01mchi statistic:', g)
print('\033[35mp-value:', p)
print('\033[36mdegrees of freedom:', dof)
#print('expected results:', expctd)

# ax = sns.barplot(x='white', y='won', data=chess, ci=None)
# ax.set_xticklabels(['Black', 'White'])
# ax.set_xlabel('Color')
# ax.set_ylabel('Win (Normalized)')
# bars = ax.get_children()
# bars[0].set_color((0,0,0))
# bars[1].set_color((.8,.8,.8))
# ax.set_title('Win Distribution')
# plt.show()