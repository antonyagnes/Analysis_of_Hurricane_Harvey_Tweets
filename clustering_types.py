import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.cluster import KMeans, SpectralClustering, DBSCAN



def k_means(X,n,x,y):
    sc = KMeans(n_clusters = n)
    y_pred = sc.fit_predict(X)

    plt.scatter(x, y, c = y_pred)
    plt.xlabel("column 1")
    plt.ylabel("column 2")
    plt.title("Column 1 Vs column 2 - K means")
    plt.show()

    #return sc.inertia_

def k_for_k_means(list_a,x,y):
    inertia_list = []
    for i in range(1,26):
        k_means_inertia = k_means(list_a,i,x,y)
        inertia_list.append(k_means_inertia)
    x = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
    plt.plot(x,inertia_list)
    plt.xlabel("k")
    plt.ylabel("inertia")
    plt.title("k vs inertia - K means")
    plt.show()

def spectral_clustering(X,n,x,y):
    sc = SpectralClustering(n_clusters = n)
    y_pred = sc.fit_predict(X)
    plt.scatter(x, y, c = y_pred)
    plt.xlabel("column 1")
    plt.ylabel("column 2")
    plt.title("Column 1 Vs column 2 - Spectral Clustering")
    plt.show()

def DBSCAN_Clustering(X,x,y):
    sc = DBSCAN(eps=1.5)
    y_pred = sc.fit_predict(X)
    plt.scatter(x, y, c=y_pred)
    plt.xlabel("column 1")
    plt.ylabel("column 2")
    plt.title("Column 1 Vs column 2 - DBSCAN")
    plt.show()

list_a = []
with open('/Users/User/Downloads/Clustering-dataset 2/Clustering1.txt') as read_file:
    for line in read_file:
            a = (line.strip('\n').strip('\t'))
            list_a.append(a.split('\t'))
list_a.pop(0)
x = []
y = []
for i in list_a:
    x.append(i[0])
    y.append(i[1])
#k_for_k_means(list_a,x,y)
#k_means(list_a,5,x,y)
#spectral_clustering(list_a,5,x,y)
#DBSCAN_Clustering(list_a,x,y)