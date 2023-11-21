import pandas as pd

from sklearn.metrics import mean_absolute_error

from sklearn.ensemble import RandomForestRegressor

from sklearn.model_selection import train_test_split

from pdpbox.pdp import pdp_isolate, pdp_plot, pdp_interact, pdp_interact_plot
import shap

def color_percent(floaty):
  "Input a normalized number between 0 and 1, and get it in string form colored according to percentage."
  if floaty >= .5:
    green = 200
    red = int(500 * (1 - floaty))
  else:
    red = 255
    green = int(400 * floaty)

  return f'\033[38;2;{red};{green};0m{floaty}\033[00m'

def numberinator(num):
    nums = '0123456789'
    numy = ''
    if type(num) == str:
        for char in num:
            if char in nums:
                numy += char

    if numy == '':
        numy = None
    else:
        numy = float(numy)

    return numy


df = pd.read_csv('files/lending-club-subset.csv', skipinitialspace=True)

keep = ['loan_amnt', 'funded_amnt', 'funded_amnt_inv', 'term', 'int_rate', 'annual_inc', 'inq_last_6mths', 'dti', 'open_acc', 'revol_bal', 'total_acc', 'total_pymnt_inv', 'total_rec_late_fee', 'fico_range_low', 'fico_range_high']
df = df[keep]

df['term'] = df['term'].apply(numberinator)
df['int_rate'] = df['int_rate'].str.strip('%').astype(float)
df['fico_avg'] = (df['fico_range_low'] + df['fico_range_high']) / 2
df = df.drop(columns=['fico_range_low', 'fico_range_high'])
df['dti'] = df['dti'].fillna(df['dti'].mean())


target = 'fico_avg'
X = df.drop(target, axis=1)
y = df[target]

X_train, y_train = X[:70000], y[:70000]
X_val, y_val = X[70000:85000], y[70000: 85000]
X_test, y_test = X[85000:], y[85000:]

y_pred_b1 = [y_train.mean()] * len(y_train)
print('Mean credit score', y_train.mean())
print('Baseline MAE', mean_absolute_error(y_train, y_pred_b1))

model_rf = RandomForestRegressor()
model_rf.fit(X_train, y_train)

print('Train MAE:', mean_absolute_error(y_train, model_rf.predict(X_train)))
print('Validation MAE:', mean_absolute_error(y_val, model_rf.predict(X_val)))
print('R2 score:', model_rf.score(X_val, y_val))


# Partial Dependence Plot
isolate = pdp_isolate(model_rf, dataset=X_val, model_features=X_val.columns, feature='int_rate')
pdp_plot(isolate, feature_name='int_rate')