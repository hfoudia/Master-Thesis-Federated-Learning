# Importing the necessary libraries
import sys
sys.path.append('../FLAD/') # This is to add the root directory to the path to import the necessary modules

from util_functions import *
import os


NUM_CLIENTS = len(next(os.walk('../clients/'))[1]) # get number of directories in clients folder

for x in range(1, NUM_CLIENTS+1):
    # Load the data
    X_train, y_train = load_dataset(f'../clients/client-{x}/10t-10n-IDS2017-dataset-train.hdf5')
    X_test, y_test = load_dataset(f'../clients/client-{x}/10t-10n-IDS2017-dataset-test.hdf5')
    X_val, y_val = load_dataset(f'../clients/client-{x}/10t-10n-IDS2017-dataset-val.hdf5')

    print(f'Client-{x} Train Data Shape: {X_train.shape, y_train.shape}')
    print(f'Client-{x} Test Data Shape: {X_test.shape, y_test.shape}')
    print(f'Client-{x} Validation Data Shape: {X_val.shape, y_val.shape}')