# Analysis_of_Hurricane_Harvey_Tweets
Clustering types used are as follows,
K means
Spectral Clustering
DBSCAN

Description:

k_for_kmeans:
This function calculates inertia for each value of k. The values of k range from 1 to 25. Using the elbow constraint, we pick the value of k as 5. 
    Changes to be made in k_means:
         While implementing k_for_kmeans function, line number 11 - line number 15 should be commented and line number 17 should be uncommented.

k_means:
We pass the number of clusters as the parameter. While implementing this function, comment line 17 and uncomment line number 11 - line number 15. The function returns a graph that has k clusters in it.

spectral_clustering:
We pass the number of clusters as the parameter. The function returns a graph that has n clusters in it.

DBSCAN_clustering:
We just pass the input and the value of epsilon is mentioned inside the function. In this type of clustering, the number of clusters need not be mentioned. The function returns a graph that has n number of clusters in it.
