CL4-BI-3

# ================================
# STEP 1: IMPORT LIBRARIES
# ================================
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.linear_model import LogisticRegression


# ================================
# STEP 2: LOAD DATASET
# ================================
data = load_iris()

# Convert to DataFrame
df = pd.DataFrame(data.data, columns=data.feature_names)
df['target'] = data.target

print("First 5 rows of dataset:")
print(df.head())


# ================================
# STEP 3: DATA UNDERSTANDING
# ================================
print("\nDataset Info:")
print(df.info())

print("\nStatistical Summary:")
print(df.describe())

print("\nMissing Values:")
print(df.isnull().sum())


# ================================
# STEP 4: DATA PREPROCESSING
# ================================
# Separate features and target
X = df.drop('target', axis=1)
y = df['target']

# Feature Scaling
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)


# ================================
# STEP 5: TRAIN-TEST SPLIT
# ================================
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42
)


# ================================
# STEP 6: MODEL TRAINING
# ================================
model = LogisticRegression()
model.fit(X_train, y_train)


# ================================
# STEP 7: PREDICTION
# ================================
y_pred = model.predict(X_test)


# ================================
# STEP 8: MODEL EVALUATION
# ================================
# Accuracy
accuracy = accuracy_score(y_test, y_pred)
print("\nAccuracy:", accuracy)

# Confusion Matrix
cm = confusion_matrix(y_test, y_pred)
print("\nConfusion Matrix:\n", cm)

# Classification Report
print("\nClassification Report:\n")
print(classification_report(y_test, y_pred))


# ================================
# STEP 9: VISUALIZATION
# ================================
# Confusion Matrix Heatmap
plt.figure(figsize=(6,4))
sns.heatmap(cm, annot=True, cmap='Blues')
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Confusion Matrix")
plt.show()


# Pairplot Visualization
sns.pairplot(df, hue='target')
plt.show()


# ================================
# STEP 10: EXTRA (DECISION TREE)
# ================================
from sklearn.tree import DecisionTreeClassifier

dt_model = DecisionTreeClassifier()
dt_model.fit(X_train, y_train)

y_pred_dt = dt_model.predict(X_test)

print("\nDecision Tree Accuracy:", accuracy_score(y_test, y_pred_dt))

