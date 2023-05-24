import numpy as np


def make_dataset(n_classes, n_class_sample, scale):
    X, Y = [], []
    for class_idx in range(n_classes):
        centroid = np.random.uniform(-5, 6, (2,))
        X_ = np.random.normal(loc=centroid, scale=scale,
                              size=(n_class_sample, 2))
        Y_ = class_idx * np.ones(shape=(n_class_sample))

        X.append(X_)
        Y.append(Y_)
    X = np.vstack(X)
    Y = np.concatenate(Y)
    return X, Y
