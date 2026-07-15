# -*- coding: utf-8 -*-
"""Khushi_Sharma_project2_EDA.ipynb

by Colab.

Original file is located at
    https://colab.research.google.com/drive/1jSfEO4VkizLxblyVrJbm-37kYkGw9Wks
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

file_path ='/content/data.xlsx'
df = pd.read_excel(file_path)

df.head()

print("Missing Values Per Column:")
print(df.isnull().sum())


completeness = (df.notnull().sum().sum() / df.size) * 100
print(f"\nData Completeness: {completeness:.2f}%")

import pandas as pd
import numpy as np


total_rows = len(df)
total_cells = df.size


total_missing = df.isnull().sum().sum()
missing_percentage = (total_missing / total_cells) * 100



invalid_dates = pd.to_datetime(df['Date'], errors='coerce').isnull().sum()

invalid_numeric = 0
for col in ['Quantity', 'UnitPrice', 'TotalPrice']:
    invalid_numeric += pd.to_numeric(df[col], errors='coerce').isnull().sum()

total_format_errors = invalid_dates + invalid_numeric
format_error_percentage = (total_format_errors / total_cells) * 100


valid_percentage = 100 - (missing_percentage + format_error_percentage)


print("--- PROJECT 2: DATA DIAGNOSIS BREAKDOWN ---")
print(f"✅ Valid Records: {valid_percentage:.2f}%")
print(f"❌ Missing Values: {missing_percentage:.2f}%")
print(f"⚠️ Format Errors: {format_error_percentage:.2f}%")

import pandas as pd


file_path ='/content/data.xlsx'
df = pd.read_excel(file_path)


df.describe()

print("Total rows in dataset:", len(df))

import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize=(8, 4))

sns.histplot(df['TotalPrice'], kde=True, color='purple', bins=30)
plt.title('Distribution Shape of Total Price')
plt.xlabel('Total Price')
plt.ylabel('Frequency')
plt.show()


print(f"Skewness Value: {df['TotalPrice'].skew():.2f}")

plt.figure(figsize=(6, 4))
sns.heatmap(df[['Quantity', 'UnitPrice', 'TotalPrice']].corr(), annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Matrix')
plt.show()

plt.figure(figsize=(8, 3))
sns.boxplot(x=df['TotalPrice'], color='orange')
plt.title('Outlier Detection using Boxplot')
plt.xlabel('Total Price')
plt.show()

import pandas as pd
df_check = pd.read_excel('/content/data.xlsx')
print(df_check.columns.tolist())
