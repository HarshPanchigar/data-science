import pandas as pd

df = pd.read_excel("student.xlsx", engine="openpyxl")
print(df)