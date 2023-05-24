import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets

dataset = datasets.load_digits()
x_data = dataset.data
y_data = dataset.target
K = 11

fig, axes = plt.subplots(3, 3, figsize=(10, 10))
for ax_idx, ax in enumerate(axes.flatten()):
    ax.imshow(x_data[ax_idx].reshape(8, 8),
              cmap='gray')
fig.tight_layout()
plt.show()
print(x_data.shape)

target_idx = 500
target_x = x_data[target_idx]
target_y = y_data[target_idx]
print("Answer: ", target_y)

n_samples = len(y_data)
n_corrects = 0
for target_idx in range(n_samples):
    target_x = x_data[target_idx]
    target_y = y_data[target_idx]
    dists = []
    for data_idx in range(n_samples):
        x = x_data[data_idx]
        dist = np.sum((x - target_x) ** 2)
        dists.append(dist)

    close_K_indices = np.argsort(dists)[:K]
    close_Y = y_data[close_K_indices]

    uniques, cnts = np.unique(close_Y, return_counts=True)
    pred = uniques[np.argmax(cnts)]

    if target_y == pred: n_corrects += 1

accuracy = n_corrects / n_samples
print(f"accuracy: {accuracy:.3f}")
