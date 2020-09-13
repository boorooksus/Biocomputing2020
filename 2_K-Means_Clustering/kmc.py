from sys import stdin
from math import sqrt
import random

# getDist : get Euclidean distance of two vectors
# parameter : vector of a gene, center vector of cluster
# return Euclidean distance of two vectors
def getDist(data_vector, center_vector):
    res = 0.00  # sum of gaps between vector elements
    for i in range(len(data_vector)):
        res += (data_vector[i] - center_vector[i]) ** 2
    # return distance
    return sqrt(res)


# getCenter : get mean vector of a cluster
# parameter : vector list of a cluster
# return mean vector of vectors in the cluster
def getCenter(vectorList):
    #res = [0.00 for _ in range(79)]  # mean vector
    res = []
    # get average of each vector elements
    for i in range(len(vectorList[0])):
        temp = 0.00
        for j in range(len(vectorList)):
            temp += vectorList[j][i]
        # check denominator is not 0 before division
        if len(vectorList) != 0:
            res.append(temp / len(vectorList))
    # return mean vector
    return res


# kmc : k-means clustering
# parameters : k, center vector list
# return cluster list
def kmc(k, center):
    global geneNum
    cluster = [[] for _ in range(k)]  # list of cluster lists that save data vectors

    # repeat while there is no change in cluster centers
    while 1:
        # categorize data set into cluster
        for i in range(len(dataSet)):
            dist = [0.00 for _ in range(k)]  # distances of centers from the data vector
            # get distances from centers
            for j in range(k):
                dist[j] = getDist(dataSet[i], center[j])

            clusterNum = -1  # cluster number of the data vector
            minDist = 1000000.00  # minimum distance
            # find a cluster which has nearest center from the data vector
            for j in range(k):
                if dist[j] < minDist:
                    clusterNum = j
                    minDist = dist[j]

            # insert the data vector into cluster list
            cluster[clusterNum].append(dataSet[i])
            geneNum[clusterNum].append(i + 1)

        newCenter = []  # list of new centers which are means of vectors in each clusters
        # get mean vectors of each clusters
        for i in range(k):
            newCenter.append(getCenter(cluster[i]))

        # sort mean vectors in ascending order
        newCenter.sort()

        # break if there is no change in centers
        if newCenter == center:
            break

        else:
            # copy new centers and paste into center list
            center = newCenter[:]
            # clear the cluster list
            cluster = [[] for _ in range(k)]
            geneNum = [[] for _ in range(k)]

    return cluster


# get input data from user
print("input k (k is number of clusters)")
k = int(stdin.readline())  # number of clusters
print("input location of input file")
location = stdin.readline().strip()  # address of input file
print("input name of input file")
fileName = stdin.readline().strip()  # name of input file

dataSet = []  # data set for clustering
geneNum = [[] for _ in range(k)]  # list of gene number lists of each clusters

# open data set file and read
f = open("%s\%s" % (location, fileName), 'r')
# read lines in the file
while 1:
    line = f.readline()
    if not line:
        break
    # insert data vector into dataSet
    dataSet.append(list(float(i) for i in line.split()))
# close the file
f.close()

# select how to determine centers of cluster
print("input 's' or 'r'")
print("s : specifying the starting centers yourself")
print("r : Picking random data point as your starting centers")
center_type = stdin.readline().strip()

center = []  # list that saves centers

# get k vectors from user if input is 's'
if center_type == "s":
    print("input file name of center data")
    center_fn = stdin.readline().strip()
    # open the file
    f = open("%s\%s" % (location, center_fn), 'r')
    # read lines in the file
    while 1:
        line = f.readline()
        if not line:
            break
        #insert data vector into center
        center.append(list(float(i) for i in line.split()))
    # close the file
    f.close()

# pick k vectors randomly   if input is 'r'
else:
    for i in range(k):
        idx = random.randrange(0, len(dataSet))
        center.append(dataSet[idx])

print("clustering is started...")
# k-means clustering
cluster = kmc(k, center)


# make file of the result
# location of the files is same as input data file user designated
f = open("%s\kmc.out" %location, 'w')
line = "K = %s\n" % k
f.write(line)
line = "RIBO genes: gene number 1 to 121\n"
f.write(line)
line = "NONRIBO genes: gene number 122 to 2467\n"
f.write(line)
for i in range(len(geneNum)):
    line = "\n\nCluster %s\n" % (i + 1)
    f.write(line)
    line = "Total number of genes = %s\n" % (len(geneNum[i]))
    f.write(line)
    for j in range(len(geneNum[i])):
        line = "index: %s   Gene number = %s\n" %(j + 1, geneNum[i][j])
        f.write(line)
f.close()

print("clustering is completed")