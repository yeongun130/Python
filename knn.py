import numpy as np
import matplotlib.pyplot as plt

n_samples = 1000
n_test_sample = 10
X = np.random.normal(0, 1, (n_samples, 2))
test_X = np.random.normal(0, 1, (n_test_sample, 2))
print(X)
print(X[:, 0])  # 첫번째 column
print(X[:, 1])  # 두번째 column

print(X[0, :], X[0])  # 첫번째 row(행)
print(X[1, :], X[1])  # 두번째 row(행)

for data_idx in range(n_samples):
    print(X[data_idx])

fig, ax = plt.subplots(figsize=(10, 10))
ax.scatter(X[:, 0], X[:, 1], alpha=0.5)
ax.scatter(test_X[:, 0], test_X[:, 1], alpha=0.5,
           color='red', s=100)
ax.tick_params(labelsize=20)
plt.show()


