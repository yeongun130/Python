import matplotlib.pylab as plt
import numpy as np

img = plt.imread('./test.jpg').mean(axis=-1)
H, W = img.shape
print(H, W)

filter_ = np.array([[0, 255, 255],
                    [0, 255, 255],
                    [0, 255, 255]])
H_filter, W_filter = filter_.shape
H_, W_ = H - H_filter + 1, W - W_filter + 1
print(H_, W_)

img_filtered = np.zeros(shape=(H_, W_))
for i in range(H_):
    for j in range(W_):
        window = img[i : i + 3, j : j + 3]
        z = np.sum(window * filter_)
        img_filtered[i, j] = np.abs(z)

fig, axes = plt.subplots(1, 2, figsize=(10, 5))
axes[0].imshow(img, cmap='gray')
axes[1].imshow(img_filtered, cmap='gray')
fig.tight_layout()
plt.show()
