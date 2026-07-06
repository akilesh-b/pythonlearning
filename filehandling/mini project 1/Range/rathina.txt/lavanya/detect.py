import pandas as pd
import numpy as np

data = {
    'emp_id': [101, 101, 101,
               102, 102, 102,
               103, 103, 103],

    'emp_name': ['rathina', 'rathina', 'rathina',
                 'praveen', 'praveen', 'praveen',
                 'ramu', 'ramu', 'ramu'],

    'year': [2023, 2024, 2025,
             2023, 2024, 2025,
             2023, 2024, 2025],

    'salary': [50000, 55000, 60000,
               45000, 45000, 47000,
               60000, 65000, 70000]
}

df = pd.DataFrame(data)

# Previous year's salary
df['previous_salary'] = df.groupby('emp_id')['salary'].shift(1)

# Salary difference
df['salary_increase'] = df['salary'] - df['previous_salary']

# Trend column
df['trend'] = np.where(
    df['salary_increase'] > 0, 'Increased',
    np.where(df['salary_increase'] < 0, 'Decreased', 'No Change')
)

print(df)