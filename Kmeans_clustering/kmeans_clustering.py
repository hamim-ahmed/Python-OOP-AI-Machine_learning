import numpy as np
import matplotlib.pyplot as plt
import random

#-----------------------------------Implementation start---------------------------------------------

class KmeansClustering:

  def __init__(self, num_clusters=1):
    '''Within this constructor declare an instance variable that will store the value of 'num_clusters' argument'''
    self.k = num_clusters

  def read_data(self, file_name):
    '''Read all the data from the file 'file_name' as a 2D numpy array
        and store the numpy array to an instance variable'''
    self.datapoints = np.genfromtxt(file_name, delimiter=",")
    print(self.datapoints)
    
  def initial_centers(self):
    '''Use the random.sample(...) function to randomly choose the initial cluster centers
        and return the cluster centers as a 2D numpy array.'''
    initial_center = random.sample(self.datapoints.tolist(), self.k)   #random.sample works in list >>> so, converting "datapoints" numpy array in list.
    # print(initial_center)
    return np.array(initial_center)
    
  def plot_initial_data(self, cluster_centers):
    '''Will scatter plot all the data points (already stored in instance variable of this class)
        and also scatter plot all the 'cluster_centers' using a different symbol and color.'''
    x = self.datapoints[:,0]
    y = self.datapoints[:,1]
    plt.scatter(x,y, s= 1, marker="x", label = "initial data")
    cx = cluster_centers[:, 0]
    cy = cluster_centers[:, 1]
    plt.scatter(cx, cy, s = 100, color = "r", marker="p", label = "initial centers")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("Initial data points")
    plt.legend()
    plt.show()


    
  def decide_cluster(self, point, cluster_centers):

    '''Will take input a 'point' and 'cluster_centers' data. 
    Calculate the distance from the point to all the other cluster_centers using Euclidean distance 
    and return the cluster number (0/1/2...) where the point belongs to.'''

    distancearr = (cluster_centers - point)**2
    #print(distancearr.sum(axis = 1))
    print(distancearr.shape)
    return (np.argmin(distancearr.sum(axis=1)))

    
  def cluster_formation(self, cluster_centers):
    '''Will take input the 'cluster_centers' and assign all the data points to the closest cluster.
    Return a dictionary of the following form:
    
    full_cluster={
      0:[[1,2],[3,4],[5,6]], #Key 0 is the cluster number and the values are the points of that cluster.
      1:[[7,8],[9,10]],
      ...
    }

    Steps:
    - Initialize full_cluster to an empty dictionary 
    - For each data point call the decide_cluster(...) function 
    and according to the return value of decide_cluster() assign the point to the appropriate cluster in full_cluster.
    '''
    full_cluster = {0: [], 1: [], 2: [], 3: [], 4: [], 5: []}       #delclaring the cluster dictionary.

    for eachpoints in self.datapoints:                               #access each dataset points
      index = self.decide_cluster(eachpoints, cluster_centers)       #passing each dataset point to calculate distance from center and the return the desire index
      full_cluster[index].append(eachpoints)                         #append the point into the center(index/key) with min distance
      # print(full_cluster)
    return full_cluster


    
  def new_center(self, full_cluster):
    '''Will take input the full_cluster dictionary object as input
        and will calculate the center for all the clusters.
        It will return all the centers of the clusters as a 2D numpy array.'''
    # print(full_cluster.items())
    new_centers = np.empty((6,2),float)

    for eachcenter in range(0,self.k):
      # print(eachcenter)
      nparray = np.array(full_cluster[eachcenter])
      mean_value = nparray.mean(axis=0)
      # print(mean_value)
      new_centers[eachcenter:eachcenter+1,0:2] = mean_value

    return new_centers


  def switch_counts(self, prevcluster, newcluster):
    '''Will take input two full_cluster objects and will compare them 
    and return the count of how many points have changed their groups.'''
    count = 0
    for key in range(0, self.k):
      for items in np.array(prevcluster[key]):
        if items in np.array(newcluster[key]):
          pass
        else:
          count = count + 1
    print(count)
    return count


  def kmeans_algo(self):
    '''
    1. Call the initial_centers(...) method to set the initial centers.
    2. Call the plot_initial_data(...) method to show the initial plot of the data
    3. Call the cluster_formation(...) method to build the initial cluster (for example, old_cluster)
    4. While True:
    5.      Call the new_center(...) method to calculate the new_centers from the old_cluster
    6.      Call the cluster_formation(...) method to again build updated cluster (for example, new_cluster)
    7.      Call the switch_counts(...) method to compare both the old and new clusters
    8.      If the total number of switches are less than 10 then exit from this while loop
    9.      Else set the new_cluster as old_cluster and rotate again
    10.End While
    11.return the old_cluster as your final result

    '''
    initial_center = self.initial_centers()
    self.plot_initial_data(initial_center)
    initial_full_cluster = self.cluster_formation(initial_center)     #assigning every datapoint to a spicific center among k no of center.
    # print("initial full cluster: ",initial_full_cluster)
    print("Number of errors:")
    while True:
      self.new_centers = self.new_center(initial_full_cluster)
      new_full_cluster = self.cluster_formation(self.new_centers)
      compare = self.switch_counts(initial_full_cluster,new_full_cluster)
      if compare<10:
        break
      initial_full_cluster = new_full_cluster

    return new_full_cluster


  def plot_final_cluster(self, clusters):
    '''Will take input a full cluster dictionary object as input.
    For each cluster draw a different scatter plot and also show the centers of the each cluster'''
    for key in range(0, self.k):
      points_list = clusters[key]
      numpy_list = np.array(points_list)
      cx = numpy_list[:, 0]
      cy = numpy_list[:, 1]
      plt.scatter(cx, cy, s=2, marker="p")
      plt.xlabel("X")
      plt.ylabel("Y")
      plt.title("Final clusters")
    x = self.new_centers[:, 0]
    y = self.new_centers[:, 1]
    plt.scatter(x, y, s=100, color='r', marker="p", label="final center")
    plt.legend()
    plt.show()
    
#---------------------------------------------End of your implementation--------------------------------------------------	



#Creating the object and calling necessary methods
#I have implemented this section for you ;)
obj=KmeansClustering(6)
obj.read_data("data.csv")                  #will read the data from the file and store in a 2D numpy array (for example, datapoints)
final_cluster=obj.kmeans_algo()            #calling the main kmeans clustering algorithm for cluster formation
obj.plot_final_cluster(final_cluster)      #will scatter plot all the clusters with corresponding centers

#====================test=====================
