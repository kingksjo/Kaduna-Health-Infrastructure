import pandas as pd
df = pd.read_excel("data (3).xlsx")
missing_values = df.isnull().sum()
total_values = df.count() + missing_values
percentage_missing = (missing_values / total_values) * 100
print(percentage_missing)     