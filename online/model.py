import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def find_closest_centroids(X, centroids):
    """
    Computes the centroid memberships for every example
    Args:
        X: (m, n)
        centroids: (K, n)
    Returns:
        idx: (m,) closest centroids
    """
    K = centroids.shape[0]

    idx = np.zeros(X.shape[0], dtype=int)
    distances_squared = np.sum((X[:, np.newaxis, :] - centroids) ** 2, axis=2)
    # shape of X[: np.newaxis, :] is (m,1,n)
    # subtraction is broadcasted, so we have K*(m,1,n) - m*(K,n) -> (m,K,n)
    idx = np.argmin(distances_squared, axis=1)
    return idx

def compute_centroids(X, idx, K):
    """
    Returns the new centroids by computing the means of the
    data points assigned to each centroid.

    Args:
        X: (m, n) Data points
        idx: (m,) idx[i] contains the index of
             the centroid closest to example i
        K: number of centroids

    Returns:
        centroids: (K, n) New centroids computed
    """
    m, n = X.shape
    centroids = np.zeros((K, n))
    for c in range(K):
        mask = (idx == c)
        acc = np.sum(X[mask], axis=0)
        cnt = np.sum(mask)
        if cnt==0:
            centroids[c] = acc
            continue
        centroids[c] = acc / cnt
    return centroids

def kMeans_init_centroids(X, K):
    """
    This function initializes K centroids that are to be
    used in K-Means on the dataset X
    Args:
        X: Data points
        K: number of centroids
    Returns:
        centroids: Initialized centroids
    """
    randidx = np.random.permutation(X.shape[0])
    centroids = X[randidx[:K]]
    return centroids

def run_kMeans(X, initial_centroids, max_iters=10, plot_progress=False):
    """
    Runs the K-Means algorithm on data matrix X, where each row of X
    is a single example
    """
    m, n = X.shape
    K = initial_centroids.shape[0]
    centroids = initial_centroids
    previous_centroids = centroids
    idx = np.zeros(m)

    for i in range(max_iters):
        print("K-Means iteration %d/%d" % (i, max_iters-1))
        idx = find_closest_centroids(X, centroids)
        centroids = compute_centroids(X, idx, K)
    return centroids, idx

K = 20  # Choose K accordingly (maybe some heuristic)
max_iters = 10

def process_image(image, k):
    K = k
    X_img = np.reshape(image, (image.shape[0] * image.shape[1], 3))
    initial_centroids = kMeans_init_centroids(X_img, K)
    centroids, idx = run_kMeans(X_img, initial_centroids, max_iters)

    idx = find_closest_centroids(X_img, centroids)
    X_recovered = centroids[idx, :]
    X_recovered = np.reshape(X_recovered, image.shape)
    return X_recovered
