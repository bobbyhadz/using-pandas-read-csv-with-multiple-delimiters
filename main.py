# Using pandas.read_csv() with multiple delimiters in Python

import pandas as pd

df = pd.read_csv(
    'employees.csv',
    sep=r',|;|@',
    encoding='utf-8',
    engine='python'
)

#   first_name last_name        date
# 0      Alice     Smith  2023-01-05
# 1      Bobby      Hadz  2023-03-25
# 2       Carl     Lemon  2021-01-24
print(df)