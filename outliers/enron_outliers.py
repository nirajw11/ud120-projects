#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
for k in data_dict.keys():
    if data_dict[k]["salary"] != 'NaN' and data_dict[k]["salary"]>= 26600000:
        print k,data_dict[k]["salary"],data_dict[k]["bonus"]

data_dict.pop("TOTAL",0)

for k in data_dict.keys():
    if data_dict[k]["salary"] != 'NaN' and data_dict[k]["salary"]>= 1000000 and data_dict[k]["bonus"] >= 5000000:
        print k,data_dict[k]["salary"],data_dict[k]["bonus"]

features = ["salary", "bonus"]
data = featureFormat(data_dict, features)
### your code below


for point in data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter( salary, bonus )

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()
