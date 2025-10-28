import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
x,y=make_blobs(n_samples=200,centers=3,cluster_std=0.6)
plt.scatter(x[:,0],x[:,1],s=39)
plt.show()
k=KMeans(n_clusters=3)
k.fit(x)
cen=k.cluster_centers_
l=k.labels_
plt.scatter(x[:,0],x[:,1],c=l,cmap='rainbow',s=30)
plt.scatter(cen[:,0],cen[0:,1],c='black',marker='x',s=200)


plt.legend()
plt.show()
