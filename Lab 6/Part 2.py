# David Ziama
# Class ID 3
# Lab Assignment 6
# Part 2
# Solve T Shirt size problem as illustrated in class using any of the clustering methods



from pylab import plot,show
#This is to import the pylab module and to import the plot and show so it can be presented to user
from numpy import vstack,array
#This is to import the numpy module and to have the vstack and array imported to use within the program
from numpy.random import rand
#This is to have the random function of numpy imported
from scipy.cluster.vq import kmeans,vq
#This is to import scipy module with cluster and kmeans to be used within the program

info = vstack((rand(250,2) + array([.5,.5]),rand(250,2)))
#This is to generate the data information, I randomized it for the data point
cent,_ = kmeans(info,3)
#This is to compute the kmean vaule with clusters and indicating 3 cluster points
var,_ = vq(info,cent)
#This is to assign the sample to each specific cluster

plot(info[var==0,3],info[var==0,1],'aa',
     #this is to plot with indexing for the plot points
     info[var==1,0],info[var==1,3],'bb')
     # this is to plot with indexing for the plot points
plot(cent[:,0],cent[:,1],'ee',markersize=8)
#This is to have the plot with specific centorid points and to indicate the size of those centroids
show()
#This is to show the plot
cent,_ = kmeans(info,5)
#This is to compute the kmean vaule with clusters and indicating 5 cluster points
var,_ = vq(info,cent)
#This is to assign the sample to each specific cluster
plot(info[var==0,0],info[var==0,1],'aa',
     #This is to plot with indexing for the plot poihts
     info[var==1,0],info[var==1,1],'bb',
     #This is to plot with indexing for the plot poihts
     info[var==2,0],info[var==2,1],'cc') # third cluster points
    #This is to plot with indexing for the plot poihts
plot(cent[:,0],cent[:,1],'dd',markersize=8)