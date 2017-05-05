#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []

    ### your code goes here
    err_data = []	
    for i in range(len(ages)):
	err = float(net_worths[i] - predictions[i])
	err_data.append(err**2)
    
    age =[]
    for i in ages:
	age.append(i[0])
    
    net_worth =[]
    for i in net_worths:
	net_worth.append(i[0])

    t = zip(age,net_worth,err_data)   
    sorted_t = sorted(t,key = lambda t : t[2])
    len_t = 0.9 * len(sorted_t)+1
    cleaned_data = sorted_t[0:int(len_t)]
  
    return cleaned_data


