#!/usr/bin/python

"""
    Skeleton code for k-means clustering mini-project.
"""




import pickle
import numpy
import matplotlib.pyplot as plt
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit




def Draw(pred, features, poi, mark_poi=False, name="image.png", f1_name="feature 1", f2_name="feature 2"):
    """ some plotting code designed to help you visualize your clusters """

    ### plot each cluster with a different color--add more colors for
    ### drawing more than five clusters
    colors = ["b", "c", "k", "m", "g"]
    for ii, pp in enumerate(pred):
        plt.scatter(features[ii][0], features[ii][1], color = colors[pred[ii]])

    ### if you like, place red stars over points that are POIs (just for funsies)
    if mark_poi:
        for ii, pp in enumerate(pred):
            if poi[ii]:
                plt.scatter(features[ii][0], features[ii][1], color="r", marker="*")
    plt.xlabel(f1_name)
    plt.ylabel(f2_name)
    plt.savefig(name)
    plt.show()



### load in the dict of dicts containing all the data on each person in the dataset
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )

### there's an outlier--remove it!
data_dict.pop("TOTAL", 0)

for k in data_dict.keys():
    if data_dict[k]["exercised_stock_options"] != 'NaN':
        max_so = data_dict[k]["exercised_stock_options"]
        min_so = data_dict[k]["exercised_stock_options"]
        break


for k in data_dict.keys():
    if data_dict[k]["exercised_stock_options"] != 'NaN':
        if max_so < data_dict[k]["exercised_stock_options"]:
            max_so = data_dict[k]["exercised_stock_options"]
        if min_so > data_dict[k]["exercised_stock_options"]:
            min_so = data_dict[k]["exercised_stock_options"]
print "Maximum Value(exercised_stock_options) : ", max_so
print "Minimum Value(exercised_stock_options) : ", min_so


for k in data_dict.keys():
    if data_dict[k]["salary"] != 'NaN':
        max_sal = data_dict[k]["salary"]
        min_sal= data_dict[k]["salary"]
        break


for k in data_dict.keys():
    if data_dict[k]["salary"] != 'NaN':
        if max_so < data_dict[k]["salary"]:
            max_sal = data_dict[k]["salary"]
        if min_so > data_dict[k]["salary"]:
            min_sal = data_dict[k]["salary"]

print "Maximum Value(salary) : ", max_sal
print "Minimum Value(salary) : ", min_sal

from sklearn.preprocessing import MinMaxScaler
import numpy as np
salary=[]
ex_stock=[]
for k in data_dict.keys():

    if data_dict[k]["salary"] != 'NaN':
        salary.append(float(data_dict[k]["salary"]))
    if data_dict[k]["exercised_stock_options"] != 'NaN':
        ex_stock.append(float(data_dict[k]["exercised_stock_options"]))
salary.append('200000.')
ex_stock.append('1000000.')

np_salary = np.array(salary).reshape(len(salary),-1)
np_stock = np.array(ex_stock).reshape(len(ex_stock),-1)


scaler = MinMaxScaler()
rescaled_sal = scaler.fit_transform(np_salary)
rescaled_stk = scaler.fit_transform(np_stock)

print rescaled_sal[len(salary)-1]
print rescaled_stk[len(ex_stock)-1]

### the input features we want to use
### can be any key in the person-level dictionary (salary, director_fees, etc.)
feature_1 = "salary"
feature_2 = "exercised_stock_options"
feature_3 = "total_payments"
poi  = "poi"
features_list = [poi, feature_1, feature_2]
##data = featureFormat(data_dict, features_list )
##poi, finance_features = targetFeatureSplit( data )

##data = zip(poi , rescaled_sal ,rescaled_stk)
data = zip(poi , feature1 ,feature2)

### in the "clustering with 3 features" part of the mini-project,
### you'll want to change this line to
### for f1, f2, _ in finance_features:
### (as it's currently written, the line below assumes 2 features)
for f1, f2 in zip(rescaled_sal,rescaled_stk):
    plt.scatter( f1, f2)
plt.show()

### cluster here; create predictions of the cluster labels
### for the data and store them to a list called pred
from sklearn.cluster import KMeans
km=KMeans(2)
km.fit(data)
pred=km.predict(data)

print km.cluster_centers_

### rename the "name" parameter when you change the number of features
### so that the figure gets saved to a different file
try:
    Draw(pred, finance_features, poi, mark_poi=False, name="clusters.pdf", f1_name=feature_1, f2_name=feature_2)
except NameError:
    print "no predictions object named pred found, no clusters to plot"
