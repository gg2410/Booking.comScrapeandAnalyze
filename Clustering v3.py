#imports
import numpy as np
import pandas as pd
import random
import matplotlib.pyplot as plt

def euclidean_distance(A, B): #function to calculate euclidean distance 
   return(sum((A-B)**2))**0.5
 
def findingCluster(centroids, data): #function to find which cluster a point should fall under 
   cluster_list = [] 
   for x in data: #traversing through original data array 
       dist=[]
       for y in centroids: #traversing through current centroids array 
           dist.append(euclidean_distance(x,y)) #calculating eucledian distance of each point from the current centroids 
       cluster_list.append(np.argmin(dist)) #minimum distance point 
   return cluster_list

def gen_centroids(assigned_clusters, data, k): #function to find new centroids based on mean of cluster points
    updated_centroids = [] 
    for clstr in range(k): #traversing through clusters 
        updated_centroids.append(np.mean([data[x] for x in range(len(data)) if assigned_clusters[x] == clstr], axis=0)) #finding new centroid points from mean of cluster points
    return updated_centroids #new centroids array

def visualise_scatterplot(data, updated_clstr_assignment, k): #function to visualise the scatter plot
    plt.figure(figsize=(8, 6), dpi=80)
    while k > 0: #decrementing the value of k
        r = random.random()
        b = random.random()
        g = random.random()
        color = (r, g, b) #generating a random colour so that each cluster will have its unique colour 
        for index, item in enumerate(updated_clstr_assignment): #traversing through list which contains which cluster each datapoint belongs to
            if item==k-1: #k-1 because for if k=3, the clusters will be 0,1,2
                x = data[index][0] #x point is the x datapoint in data corresponding to the same index in updated_clstr_assignment 
                y = data[index][1] #y point is the y datapoint in data corresponding to the same index in updated_clstr_assignment 
                plt.scatter(x,y,c=np.array([color])) #plotting the point
        k = k-1 #decrementing k
    plt.scatter(np.array(centroids)[:, 0], np.array(centroids)[:, 1], color='black', marker='*') #plotting the centroid points 
    plt.show()

max_iterations = 100 #to ensure the program does not go on forever incase it does not stabilise on its own
 
df=pd.read_csv('Lab3\HotelListFinal.csv') #reading csv file
datafile=df[["Number-of-Hotels","Overall-Rating"]].head(100) #reading the specific columns in the csv file
data = np.array(datafile) #converting columns into a numpy array

k = int(input("Enter number of clusters:" )) #inputting number of clusters
index_centroid = random.sample(range(0, len(datafile)), k) #finding k random centroids 

centroid_array = []
for x in index_centroid: #traversing through random centroids 
   centroid_array.append(datafile.loc[x]) #list contains centroid points 
   centroids = np.array(centroid_array) #numpy array containing centroid points 
                        
iter_count = 0 #to count the number of iterations it takes for the algorithm to stabilise 
while True:
    matched_centroids = 0
    updated_clstr_assignment = findingCluster(centroids, data)
    updated_centroids = gen_centroids(updated_clstr_assignment, data, k)
    for x in range(k):
        if updated_centroids[x][0] == centroids[x][0] and updated_centroids[x][1] == centroids[x][1]:
            matched_centroids +=1
    centroids = updated_centroids
    iter_count += 1
    if matched_centroids==k or iter_count > max_iterations : 
        break

print("Number of iterations", iter_count) #printing the number of iterations it takes to stabilise 
print("Final Centroids", updated_centroids) #printing the final centroids
visualise_scatterplot(data, updated_clstr_assignment, k) #visualising the scatterplot




