""" 
    Purpose: This script is used to test the performance of the algorithms on unseen data.
"""

# Importing the necessary libraries
import sys
sys.path.append('../FLAD/') # This is to add the root directory to the path to import the necessary modules

from util_functions import *
from ann_models import *
from tensorflow.keras.models import load_model
import os
import csv

models = {'model-fedavg_e1_b50' : {'Algorithm' : 'FedAvg', 'Epochs' : 1, 'Batch_size' : 50},
          'model-fedavg_e5_b50' : {'Algorithm' : 'FedAvg', 'Epochs' : 5, 'Batch_size' : 50},
          'model-flddos_e10_b100' : {'Algorithm' : 'FLDDoS', 'Epochs' : 10, 'Batch_size' : 100},
          'model-flad_e0_b0' : {'Algorithm' : 'FLAD', 'Epochs' : 'auto', 'Batch_size' : 'auto'}}

NUM_CLIENTS = len(next(os.walk('../clients/'))[1]) # get number of directories in clients folder

FIELDS = ['Client', 'Algorithm', 'Epochs', 'Batch_size', 'Accuracy', 'Loss']

# Iterate over the models
for model_file in models:

    rows = [] # List to store the results

    # CSV file to save the results
    os.makedirs('../models/evaluation/' + model_file + '/', exist_ok=True) # Create the folder if it doesn't exist
    csv_file = '../models/evaluation/' + model_file + '/' + 'unseen-data-results.csv'

    # Load the model
    model = load_model('../models/training/' + model_file + '/10t-10n-mlp-global-model.h5')
    compileModel(model)

    # print("Model: ", model_file, "Algorithm: ", models[model_file]['Algorithm'], "Epochs: ", models[model_file]['Epochs'], "Batch_size: ", models[model_file]['Batch_size'])

    for x in range(1, NUM_CLIENTS+1):
        # Load the data
        X_test, y_test = load_dataset(f'../clients/client-{x}/10t-10n-IDS2017-dataset-test.hdf5')
        results = model.evaluate(X_test, y_test)

        rows.append([f'Client-{x}', models[model_file]['Algorithm'], models[model_file]['Epochs'], models[model_file]['Batch_size'], results[1], results[0]])

    # Save the results to the csv file
    with open(csv_file, 'w', newline='') as file:
        writer = csv.writer(file)
        
        writer.writerow(FIELDS)
        writer.writerows(rows)
