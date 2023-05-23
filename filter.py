import matplotlib.pylab as plt
import numpy as np

img = plt.imread('./test.jpg').mean(axis=-1)
H, W = img.shape
print(H, W)

filter_x = np.array([[-1, 0, 1],
                    [-2, 0, 2],
                    [-1, 0, 1]])
filter_y = np.array([[1, 2, 1],
                    [0, 0, 0],
                    [-1, -2, -1]])
H_filter, W_filter = filter_x.shape
H_, W_ = H - H_filter + 1, W - W_filter + 1
print(H_, W_)

img_filtered = np.zeros(shape=(H_, W_))
for i in range(H_):
    for j in range(W_):
        window = img[i : i + 3, j : j + 3]
        z_x = np.sum(window * filter_x)
        z_y = np.sum(window * filter_y)
        img_filtered[i, j] = z_x**2 + z_y**2

fig, axes = plt.subplots(1, 2, figsize=(10, 5))
axes[0].imshow(img, cmap='gray')
axes[1].imshow(img_filtered, cmap='gray')
fig.tight_layout()
fig.savefig('tmp.png')
plt.show()
