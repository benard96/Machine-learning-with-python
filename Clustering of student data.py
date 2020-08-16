import pandas as pd 
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import random as rd
import math


data = pd.read_csv('student-data.csv')
data.head()

x = data[['passed','absences']]



#number of clusters
k=2
#select random obv as centroids
Centroids= (x.sample(n=k))
#assign all the points to the closest cluster centroid
#recompute centroids of the newly formed clusters
#repeat step 3 and 4

diff=1
j=0

while(diff!=0):
    XD=x
    i=1
    for index1,row_c in Centroids.iterrows():
        ED=[]
        for index2,row_d in XD.iterrows():
            d1=((row_c['absences']) -  (row_d['absences']))**2
            d2=((row_c['passed'])- (row_d['passed']))**2
            d=np.sqrt(d1+d2)
            ED.append(d)
        x[i]=ED
        i=i+1
C=[]
for index,row in x.iterrow():
    min_dist=row[1]
    pos=1
    for i in range(k):
        if row[i+1]< min_dist:
            min_dist=row[i+1]
            pos=i+1
        C.append(pos)
x['Cluster']=C
Centroids_new=x.groupby(['Cluster']).mean()[['passed','absences']]
if j==0:
    diff=1
    j=j+1
else:
    diff=(Centroids_new['passed'] - Centroids['passed']).sum() + (Centroids_new['absences'] - Centroids['absences']).sum()
Centroids= x.groupby(['Cluster']).mean()[['passed','absences']]

color=['blue','green','cyan']
for k in range(k):
    data=x[x['Cluster']==k+1]
    plt.scatter(data['absences'],data['passed'],c=color[k])
plt.scatter(Centroids['absences'],Centroids['passed'],c='red')
plt.xlabel('passed')
plt.ylabel('absences')
plt.show()

plt.scatter(x['absences'],x['passed'],c='blue')
plt.scatter(Centroids['absences'],Centroids['passed'],c='red')
plt.xlabel('Student sup per academic year')
plt.ylabel('Student pass records per academic year')
plt.show()
