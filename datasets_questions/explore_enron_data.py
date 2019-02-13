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

print [p for p in enron_data.keys() if p.startswith('LAY')]
print [p for p in enron_data.keys() if p.startswith('FASTOW')]

print 'number of people:', len(enron_data)
print 'people:', enron_data.keys()
print 'features per person:', len(enron_data.items()[0][1])
print 'features:', enron_data.items()[0][1].keys()
print 'number of POIs:', len([True for _, p in enron_data.iteritems() if p.get('poi')])
print 'value of stock for James Prentice:', enron_data.get('PRENTICE JAMES').get('total_stock_value')
print 'number of emails from Wesley Colwell to POI:', enron_data.get('COLWELL WESLEY').get('from_this_person_to_poi')
print 'value of stock options for Jeff Skilling:', enron_data.get('SKILLING JEFFREY K').get('exercised_stock_options')
print 'total payments for Lay, Skilling, and Fastow:', [(p, enron_data.get(p).get('total_payments')) for p in ['SKILLING JEFFREY K', 'LAY KENNETH L', 'FASTOW ANDREW S']]
print 'number of people with salary data:', len([True for _, p in enron_data.iteritems() if p.get('salary') != 'NaN'])
print 'number of people with an email address:', len([True for _, p in enron_data.iteritems() if p.get('email_address') != 'NaN'])
print 'percentage of people with no total payments value:', len([True for _, p in enron_data.iteritems() if p.get('total_payments') == 'NaN']) * 100.0 / len(enron_data)
print 'percentage of POIs with no total payments value:', len([True for _, p in enron_data.iteritems() if (p.get('poi') and p.get('total_payments') == 'NaN')]) * 100.0 / len(enron_data)
print 'number of people with no total payments value:', len([True for _, p in enron_data.iteritems() if p.get('total_payments') == 'NaN'])

# print [p.get('email_address') for p in enron_data.itervalues()]