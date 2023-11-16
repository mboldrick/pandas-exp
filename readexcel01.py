# import os
import pandas as pd

# print(os.listdir())
df = pd.read_excel("sample.xlsx", sheet_name="Sheet2")
print(df)
