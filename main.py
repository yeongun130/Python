import matplotlib.pyplot as plt
import numpy as np

img = plt.imread('./test.jpg')
print(img.shape)
img = img.mean(axis=-1)
print(img.shape)

ifg, ax = plt.subplots(figsize=(5, 5))
img_cropped = img[30:100, 310:390]
ax.imshow(img_cropped, cmap='gray')
plt.show()
