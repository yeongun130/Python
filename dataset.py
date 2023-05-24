import numpy as np
import matplotlib.pyplot as plt

from utils import make_dataset

n_class_sample = 100
n_classes = 3
scale = 0.5
K = 5

X, Y = make_dataset(n_classes, n_class_sample, scale)
test_X = np.random.uniform(-4, 5, (2, ))

dists = []
n_samples, _ = X.shape
for samples_idx in range(n_samples):
    sample = X[samples_idx]
    dist = np.sum((sample - test_X)**2)
    dists.append(dist)

close_K_indices = np.argsort(dists)[:K]
print(Y[close_K_indices])

fig, ax = plt.subplots(figsize=(10, 10))
for class_idx in range(n_classes):
    X_ = X[Y == class_idx, :]
    ax.scatter(X_[:, 0], X_[:, 1],
               label=f'class {class_idx}')
ax.legend(fontsize=15)
ax.scatter(test_X[0], test_X[1], color='red', s=200)
plt.show()


