import pandas as pd

from sklearn.metrics import mean_absolute_error

from sklearn.ensemble import RandomForestRegressor

from sklearn.model_selection import train_test_split

def color_percent(floaty):
  "Input a normalized number between 0 and 1, and get it in string form colored according to percentage."
  if floaty >= .5:
    green = 200
    red = int(500 * (1 - floaty))
  else:
    red = 255
    green = int(400 * floaty)

  return f'\033[38;2;{red};{green};0m{floaty}\033[00m'


df = pd.read_csv('files/lending-club-subset.csv', skipinitialspace=True)

empty = ['member_id', 'next_pymnt_d']
df = df.drop(columns=empty)
weird = ['deferral_term', 'hardship_length', 'hardship_type']
df = df.drop(columns=weird)
constant = ['hardship_flag', 'policy_code', 'out_prncp_inv', 'out_prncp', 'pymnt_plan']
df = df.drop(columns=constant)
useless = ['url', 'id', 'emp_title', 'desc', 'title', 'zip_code']
df = df.drop(columns=useless)
leakage = ['fico_range_low', 'last_fico_range_high', 'last_fico_range_low']
df = df.drop(columns=leakage)

df['int_rate'] = df['int_rate'].str.strip('%').astype(float)
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
df['emp_length'] = df['emp_length'].apply(numberinator)
df['revol_util'] = df['revol_util'].str.strip('%').astype(float)
df['term'] = df['term'].apply(numberinator)
grades = {'A': 4, 'B': 3, 'C': 2, 'D': 1}
grader = lambda grade : grades[grade]
df['grade'] = df['grade'].apply(grader)
grader2 = lambda grade : grades[grade[0]] * int(grade[1])
df['sub_grade'] = df['sub_grade'].apply(grader2)

for x in df.columns:
    if df[x].dtype == object:
        df = df.drop(columns=x)


# print(df['emp_length'])
# print(df['title'].value_counts())


# for col in df.columns:
#     if df[col].nunique() < 3:
#         print('----------------------------------------------------------')
#         print(col)
#         print(f"{df[col].nunique()}/{len(df)}")
#         print()

# print(df['loan_status'].value_counts())

target = 'fico_range_high'
X = df.drop(target, axis=1)
y = df[target]

X_train, y_train = X.head(70000), y[:70000]
X_val, y_val = X[70000:85000], y[70000: 85000]
X_test, y_test = X[85000:], y[85000:]

y_pred_b1 = [y_train.mean()] * len(y_train)
print('Mean interest rate', y_train.mean())
print('Baseline MAE', mean_absolute_error(y_train, y_pred_b1))

model_rf = RandomForestRegressor()
model_rf.fit(X_train, y_train)