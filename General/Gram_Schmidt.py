import numpy as np


def gram_schmidt():
    orthogonal_vectors = []
    for v in vectors:
        for u in orthogonal_vectors:
            projection = v.dot(u) / u.dot(u) * u
            v = v - projection
        orthogonal_vectors.append(v)
    return orthogonal_vectors


vectors = np.array([[4, 1, 3, -1],
                    [2, 1, -3, 4],
                    [1, 0, -2, 7],
                    [6, 2, 9, -5]])
print(gram_schmidt())
