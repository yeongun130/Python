import matplotlib.pyplot as plt
import numpy as np

a = np.random.randint(-5, 7, ())
x = np.random.normal(0, 1, (100, ))
y = a * x
noise = 0.3 * np.random.normal(0, 1, (100, ))
y = y + noise

fig, ax = plt.subplots(figsize=(5, 5))
ax.scatter(x, y, alpha=0.8)

cmap = plt.get_cmap('rainbow', lut=100)
a = np.random.randint(-5, 7, ())
x_lim = np.array(ax.get_xlim())
y_lim = a * x_lim
ax.plot(x_lim, y_lim, color=cmap(0))

for i, (x, y) in enumerate(zip(x, y)):
    pred = a * x
    dpred_dx = 2 * x * (pred - y)

    a = a - 0.01 * dpred_dx

    y_lim = a * x_lim
    ax.plot(x_lim, y_lim, color=cmap(i), alpha=0.3)

fig.tight_layout()
plt.show() 
