import pandas as pd

df = pd.read_csv('paperclips.csv')

yomi = df[['RANDOM', 'A100', 'B100', 'GREEDY', 'GENEROUS', 'MINIMAX', 'TIT_FOR_TAT', 'BEAT_LAST']]
place = df[['RANDOM_PLACE', 'A100_PLACE', 'B100_PLACE', 'GREEDY_PLACE', 'GENEROUS_PLACE', 'MINIMAX_PLACE', 'TIT_FOR_TAT_PLACE', 'BEAT_LAST_PLACE']]

print(yomi.mean().sort_values(ascending=False))
#print(yomi.sum().sort_values(ascending=False))
print(place.mean().sort_values())