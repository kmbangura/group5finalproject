import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans, AgglomerativeClustering, DBSCAN
from sklearn.mixture import GaussianMixture
from sklearn.metrics import silhouette_score, silhouette_samples
from sklearn.preprocessing import StandardScaler
from tkh_utils import PALETTE
---

import pandas as pd

df = pd.read_csv("student_data.csv"
                 
np.random.seed(7)
X_demo, true_demo = make_blobs(n_samples=45, centers=3, cluster_std=0.65, random_state=7)
km_demo = KMeans(n_clusters=3, n_init=10, random_state=7).fit(X_demo)
demo_colors = [PALETTE['accent'], PALETTE['secondary'], PALETTE['primary']]

fig, axes = plt.subplots(1, 2, figsize=(11, 4.5))

axes[0].scatter(X_demo[:, 0], X_demo[:, 1], color=PALETTE['muted'], s=60, alpha=0.8)
axes[0].set_title('Before: unlabeled data')
axes[0].set_xlabel('Feature 1')
axes[0].set_ylabel('Feature 2')

for k in range(3):
    mask = km_demo.labels_ == k
    axes[1].scatter(X_demo[mask, 0], X_demo[mask, 1], color=demo_colors[k],
                     s=60, alpha=0.8, label=f'Cluster {k}')
axes[1].scatter(km_demo.cluster_centers_[:, 0], km_demo.cluster_centers_[:, 1],
                 color='black', marker='x', s=180, linewidths=2, label='Centroid')
axes[1].set_title('After: k-means finds 3 clusters')
axes[1].set_xlabel('Feature 1')
axes[1].set_ylabel('Feature 2')
axes[1].legend()

plt.tight_layout()
plt.show()
