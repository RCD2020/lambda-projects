import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

url = '/Users/colby/Documents/Lambda/01 Sprint 1/Project/sources/games.csv'

chess = pd.read_csv(url)

chess = chess[['winner', 'white_rating', 'opening_ply']]


#print(chess['white_rating'].describe())

chess.loc[(chess['white_rating'] >= 700) & (chess['white_rating'] <= 899), 'rate_cat'] = 0
chess.loc[(chess['white_rating'] >= 900) & (chess['white_rating'] <= 1099), 'rate_cat'] = 1
chess.loc[(chess['white_rating'] >= 1100) & (chess['white_rating'] <= 1299), 'rate_cat'] = 2
chess.loc[(chess['white_rating'] >= 1300) & (chess['white_rating'] <= 1499), 'rate_cat'] = 3
chess.loc[(chess['white_rating'] >= 1500) & (chess['white_rating'] <= 1699), 'rate_cat'] = 4
chess.loc[(chess['white_rating'] >= 1700) & (chess['white_rating'] <= 1899), 'rate_cat'] = 5
chess.loc[(chess['white_rating'] >= 1900) & (chess['white_rating'] <= 2099), 'rate_cat'] = 6
chess.loc[(chess['white_rating'] >= 2100) & (chess['white_rating'] <= 2299), 'rate_cat'] = 7
chess.loc[(chess['white_rating'] >= 2300) & (chess['white_rating'] <= 2499), 'rate_cat'] = 8
chess.loc[chess['white_rating'] >= 2500, 'rate_cat'] = 9

chess.loc[chess['winner'] == 'white', 'white_win'] = 1
chess.loc[chess['winner'] != 'white', 'white_win'] = 0

print(f"\033[93m{pd.crosstab(index=chess['rate_cat'], columns=chess['white_win'], margins=True)}")
joint = pd.crosstab(index=chess['rate_cat'], columns=chess['white_win'])

from scipy.stats import chi2_contingency
g, p, dof, expected = chi2_contingency(joint)

print('\n\033[31m\033[01mchi statistic:', g)
print('\033[35mp-value:', p)
print('\033[36mdegrees of freedom:', dof)
#print('expected results:', expected)

ax = sns.barplot(x='rate_cat', y='white_win', data=chess, ci=None)
ax.set_xticklabels(['0-7', '9-11', '11-13', '13-15', '15-17', '17-19', '19-21', '21-23', '23-25', '25+'])
ax.set_xlabel('Rating (x100)')
ax.set_ylabel('Win (Normalized)')
bars = ax.get_children()
# print(bars)
bars[0].set_color((0,.8,0))
bars[1].set_color((0,.6,.2))
bars[2].set_color((0,.4,.4))
bars[3].set_color((0,.2,.6))
bars[4].set_color((0,0,.8))
bars[5].set_color((.2,0,.6))
bars[6].set_color((.4,0,.4))
bars[7].set_color((.6,0,.2))
bars[8].set_color((.8,0,0))
bars[9].set_color((1,0,0))
ax.set_title('Win Distribution')
plt.show()