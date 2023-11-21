import pandas as pd
import numpy as np

from sklearn.pipeline import make_pipeline
from category_encoders import OrdinalEncoder
from sklearn.impute import SimpleImputer
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier

from sklearn.model_selection import train_test_split

import matplotlib.pyplot as plt

def color_percent(floaty):
  "Input a normalized number between 0 and 1, and get it in string form colored according to percentage."
  if floaty >= .5:
    green = 200
    red = int(500 * (1 - floaty))
  else:
    red = 255
    green = int(400 * floaty)

  return f'\033[38;2;{red};{green};0m{floaty}\033[00m'

df = pd.read_csv('files/ai4i2020.csv')
df = df.drop(columns=['TWF', 'HDF', 'PWF', 'OSF', 'RNF'])

# print(df.head())
# print(df.shape)

target = 'Machine failure'
X = df.drop(target, axis=1)
y = df[target]

X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

print('base:', color_percent(y_train.value_counts(normalize=True).max()))

# for x in X_train.columns:
#     tempMod = make_pipeline(
#         OrdinalEncoder(),
#         SimpleImputer(strategy='mean'),
#         RandomForestClassifier(
#             n_jobs=-1,
#             random_state=42
#         )
#     )

#     tempXtr, tempXvl = X_train.drop(columns=x), X_val.drop(columns=x)

#     tempMod.fit(tempXtr, y_train)

#     print('train:', color_percent(tempMod.score(tempXtr, y_train)))
#     print('val:', color_percent(tempMod.score(tempXvl, y_val)))


tempMod = make_pipeline(
    OrdinalEncoder(),
    SimpleImputer(strategy='mean'),
    RandomForestClassifier(
        n_jobs=-1,
        random_state=42
    )
)

tempXtr, tempXvl = X_train, X_val

tempMod.fit(tempXtr, y_train)

print('train:', color_percent(tempMod.score(tempXtr, y_train)))
print('val:', color_percent(tempMod.score(tempXvl, y_val)))

importances = tempMod.named_steps['randomforestclassifier'].feature_importances_
features = X_train.columns
feat_imp = pd.Series(importances, index=features).sort_values()
print(feat_imp)
# feat_imp.plot(kind='barh')
# plt.xlabel('Reduction in Gini Impurity')
# plt.show()

modelXgb = make_pipeline(
    OrdinalEncoder(),
    SimpleImputer(strategy='mean'),
    XGBClassifier(
        random_state=42,
        n_jobs=-1
    )
)
modelXgb.fit(X_train, y_train)

print('train:', modelXgb.score(X_train, y_train))
print('val:', modelXgb.score(X_val, y_val))