import pandas as pd

df = pd.read_csv('../data/raw_data.csv', encoding='latin1', sep=';')

df['Order Date'] = df['Order Date'].str.replace('.', '/')
df['Order Date'] = pd.to_datetime(df['Order Date'], errors='coerce')

df['Ship Date'] = df['Ship Date'].str.replace('.', '/')
df['Ship Date'] = pd.to_datetime(df['Ship Date'], errors='coerce')

df['Quantity'] = pd.to_numeric(df['Quantity'], errors='coerce').fillna(1)

df['Customer Name'] = df['Customer Name'].astype(str).str.strip().str.title()
df['Ship Mode'] = df['Ship Mode'].fillna("SCONOSCIUTO")
df['City'] = df['City'].fillna("SCONOSCIUTO")

df.to_csv('../data/cleaned_data.csv', index=False, encoding="utf-8")
