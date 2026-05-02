
CL4-BI-4


# ================================
# STEP 1: IMPORT LIBRARIES
# ================================
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score

# ================================
# STEP 2: LOAD DATASET
# ================================
from sklearn.datasets import load_iris

data = load_iris()
df = pd.DataFrame(data.data, columns=data.feature_names)

df.head()

# ================================
# STEP 3: CHECK DATA
# ================================
df.info()
df.describe()

# ================================
# STEP 4: FEATURE SCALING
# ================================
scaler = StandardScaler()
scaled_data = scaler.fit_transform(df)

# ================================
# STEP 5: ELBOW METHOD
# ================================
wcss = []

for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, random_state=42)
    kmeans.fit(scaled_data)
    wcss.append(kmeans.inertia_)

plt.plot(range(1, 11), wcss, marker='o')
plt.xlabel("Number of Clusters")
plt.ylabel("WCSS")
plt.title("Elbow Method")
plt.show()

# ================================
# STEP 6: APPLY K-MEANS
# ================================
kmeans = KMeans(n_clusters=3, random_state=42)
clusters = kmeans.fit_predict(scaled_data)

df['Cluster'] = clusters

# ================================
# STEP 7: VISUALIZATION
# ================================
plt.scatter(df.iloc[:, 0], df.iloc[:, 1], c=df['Cluster'], cmap='viridis')
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.title("Cluster Visualization")
plt.show()

# ================================
# STEP 8: EVALUATION
# ================================
score = silhouette_score(scaled_data, clusters)
print("Silhouette Score:", score)
