import matplotlib.pylab as plt
import numpy as np

img = plt.imread('./test3.jpg').mean(axis=-1)[0:600, 0:400]
H, W = img.shape

filter_x = np.array([
    [-1, 0, 1],
    [-2, 0, 2],
    [-1, 0, 1]
])
filter_y = np.array([
    [1, 2, 1],
    [0, 0, 0],
    [-1, -2, -1]
])

H_filter, W_filter = filter_x.shape
H_, W_ = H - H_filter + 1, W - W_filter + 1

img_filtered_x = np.zeros(shape=(H_, W_))
img_filtered_y = np.zeros(shape=(H_, W_))
img_filtered_xy = np.zeros(shape=(H_, W_))

img_filtered = np.zeros(shape=(H_, W_))
for i in range(H_):
    for j in range(W_):
        window = img[i: i + 3, j: j + 3]
        z_x = np.sum(window * filter_x)
        img_filtered_x[i, j] = abs(z_x)

        z_y = np.sum(window * filter_y)
        img_filtered_y[i, j] = abs(z_y)

        img_filtered[i, j] = z_x ** 2 + z_y ** 2

fig, axes = plt.subplots(2, 2, figsize=(10, 10))
axes[0, 0].imshow(img, cmap='gray')
axes[0, 1].imshow(img_filtered_x, cmap='gray')
axes[1, 0].imshow(img_filtered_y, cmap='gray')
axes[1, 1].imshow(img_filtered_xy, cmap='gray')
fig.tight_layout()
fig.savefig('tmp.png')
plt.show()
