import numpy as np
import outlier_cleaner

def test_outliearCleaner():
    predictions = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    ages = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    net_worths = np.array([1, 2, 3, 4, 10, 6, 7, 8, 9, 10])
    output = outlier_cleaner.outlierCleaner(predictions, ages, net_worths)
    print output