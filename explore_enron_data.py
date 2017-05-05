#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))
keys = enron_data.keys()

print "Number of people in dataset :",len(enron_data)
print "Number of features of each person :", len(keys[0])

count = 0

for i in keys:
    if enron_data[i]["poi"] == 1:
	count = count+1
		
print "Number of persons of interest :",count

print "Value of Stock - James Prentice:" ,enron_data["PRENTICE JAMES"]["total_stock_value"]

print "Email Count - Colwell Wesley:", enron_data["COLWELL WESLEY"]["from_this_person_to_poi"]

print "Value of stock option - Jefrey Shiling :",enron_data["SKILLING JEFFREY K"]["exercised_stock_options"]

l = ["SKILLING JEFFREY K","FASTOW ANDREW S"]

ind ="LAY KENNETH L"
money_max = enron_data["LAY KENNETH L"]["total_payments"]

for i in l:
    total_pay = enron_data[i]["total_payments"]
    if money_max < total_pay:
	money_max=total_pay
	ind=i

print "Person who took the most money:",ind,money_max

count_sal = 0
count_email=0

for i in keys:
    if enron_data[i]["salary"] == "NaN":
	count_sal=count_sal+1
    if enron_data[i]["email_address"] == "NaN":
	count_email=count_email+1
    	     	
	 
print "Person with have quantified salary:" ,146-count_sal
print "Person with known email address:" ,146-count_email
		    
count_pay=0       	
for i in keys:
    if enron_data[i]["total_payments"]=='NaN':
	count_pay=count_pay+1

print "Person with no payment information:",count_pay,"(",round((float(count_pay)/(len(enron_data)))*100,2),"% of the whole enron data)" 
print "Person with no payment information(Special case):",count_pay+10,"(",round((float(count_pay+10)/(len(enron_data)+10))*100,2),"% of the whole enron data)" 


