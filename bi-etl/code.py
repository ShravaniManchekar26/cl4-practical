# ================================
# STEP 1: Import Libraries
# ================================
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ================================
# STEP 2: Extract Data
# ================================
df = pd.read_csv("sales_dataset(ETL - Data Visualization)(1).csv")

print("Raw Data:")
print(df.head())

# ================================
# STEP 3: Understand Dataset
# ================================
print("\nDataset Info:")
print(df.info())

print("\nStatistical Summary:")
print(df.describe())

print("\nColumns:")
print(df.columns)

# ================================
# STEP 4: Transformation
# ================================

# 1. Remove Missing Values
df = df.dropna()

# 2. Remove Duplicate Rows
df = df.drop_duplicates()

# 3. Convert Date Column (if exists)
if 'Order Date' in df.columns:
    df['Order Date'] = pd.to_datetime(df['Order Date'])

    # Feature Engineering
    df['Year'] = df['Order Date'].dt.year
    df['Month'] = df['Order Date'].dt.month

# 4. Create Profit Column (if not exists)
if 'Profit' not in df.columns and 'Sales' in df.columns and 'Cost' in df.columns:
    df['Profit'] = df['Sales'] - df['Cost']

# ================================
# STEP 5: Load Cleaned Data
# ================================
df.to_csv("cleaned_sales_data.csv", index=False)

print("\nCleaned Data:")
print(df.head())

# ================================
# STEP 6: Visualization
# ================================

# Bar Chart: Sales by Category
if 'Category' in df.columns and 'Sales' in df.columns:
    plt.figure()
    df.groupby('Category')['Sales'].sum().plot(kind='bar')
    plt.title("Sales by Category")
    plt.xlabel("Category")
    plt.ylabel("Sales")
    plt.show()

# Line Chart: Monthly Sales
if 'Month' in df.columns and 'Sales' in df.columns:
    plt.figure()
    df.groupby('Month')['Sales'].sum().plot(kind='line')
    plt.title("Monthly Sales Trend")
    plt.xlabel("Month")
    plt.ylabel("Sales")
    plt.show()

# Scatter Plot: Sales vs Profit
if 'Sales' in df.columns and 'Profit' in df.columns:
    plt.figure()
    plt.scatter(df['Sales'], df['Profit'])
    plt.title("Sales vs Profit")
    plt.xlabel("Sales")
    plt.ylabel("Profit")
    plt.show()

# Heatmap: Correlation
plt.figure()
sns.heatmap(df.corr(), annot=True)
plt.title("Correlation Heatmap")
plt.show()

# Pie Chart: Sales by Region
if 'Region' in df.columns and 'Sales' in df.columns:
    plt.figure()
    df.groupby('Region')['Sales'].sum().plot(kind='pie', autopct='%1.1f%%')
    plt.title("Sales by Region")
    plt.ylabel("")
    plt.show()
