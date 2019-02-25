#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """

    ### your code goes here
    import numpy as np

    predictions = predictions.flatten()
    ages = ages.flatten()
    net_worths = net_worths.flatten()
    
    number_to_keep = len(predictions) * 9 // 10
    errors = np.abs(predictions - net_worths)
    idx_to_keep = np.argsort(errors)[0:number_to_keep]

    cleaned_data = [(ages[i], net_worths[i], errors[i]) for i in idx_to_keep]

    return cleaned_data 