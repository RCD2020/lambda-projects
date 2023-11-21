import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

url = '/Users/colby/Documents/Lambda/01 Sprint 1/Project/sources/games.csv'

chess = pd.read_csv(url)

chess = chess[['rated', 'turns', 'victory_status', 'winner', 'white_rating', 'black_rating', 'opening_ply']]

#print(chess['opening_ply'].value_counts())

chess.loc[chess['winner'] == 'white', 'white_win'] = 1
chess.loc[chess['winner'] != 'white', 'white_win'] = 0

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

category = chess[chess['rate_cat'] == 9]

# print(category['opening_ply'].value_counts())

################
# 2    27
# 1    12
# 3    11
# 4     6
# 5     2
# 7     1
# 6     1



move = category[category['opening_ply'] == 22]

print(move['white_win'].value_counts(normalize=True) * 100)


#####################
# 3     3490    51.48
# 4     3308    51.36
# 2     2935    51.95
# 5     2730    53.00
# 6     2020    50.44
# 7     1344    52.97
# 8     1116    50.17
# 1     1097    56.06
# 9      687    50.94
# 10     432    52.54
# 11     425    50.82
# 12     142    50.70
# 13     127    57.48
# 14      57    56.14
# 15      43    51.16
# 17      37    51.35
# 16      31    58.06
# 18      12    50.00
# 19      11    63.63
# 20       8    62.50
# 28       4    75.00
# 24       1    100.0
# 22       1    100.0