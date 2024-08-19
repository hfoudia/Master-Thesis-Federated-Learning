# Master Thesis: Federated Learning for Intrusion Detection Systems (IDS)

This repository contains the code and resources used for my Master’s thesis on Federated Learning Algorithms applied to the CIC-IDS 2017 dataset for anomaly detection. The thesis explores the effectiveness of various federated learning Algorithms in detecting network intrusions across distributed datasets.

## Repository Structure

The repository is organized as follows:

- **`FLAD/`**: Contains the FLAD code used for the experiments. This code implements the FLAD algorithm to train and evaluate models in a federated learning environment. Source : https://github.com/doriguzzi/flad-federated-learning-ddos
  
- **`LUCID/`**: Contains the necessary LUCID scripts for data preprocessing. These scripts are used to prepare the CIC-IDS 2017 dataset for model training and evaluation. Source : https://github.com/doriguzzi/lucid-ddos
  
- **`clients/`**: Contains the client subfolders and associated logs. Note that the actual data files were too large to be included in the repository. The folder structure represents the distribution of data among different clients for federated learning.
  
- **`models/`**: Contains all the different models created for testing. This includes various algorithms with different hyperparameters used during the experiments.
  
- **`plots/training/`**: Includes plots showing the progress of the F1 score per client during the training process. These visualizations help in understanding the performance of the models over time.
  
- **`scripts/`**: Contains additional scripts and tools required for testing the models and generating the various plots. This includes scripts for training, evaluation, and result visualization.

## Running the Experiments

### 1. Clients Setup

- Create a subfolder for each client within the `clients/` directory. Assign each pcap file corresponding to a specific day to a client.
- Due to memory limitations and the large size of the pcap files (ranging between 8.2GB and 12GB), each pcap file should be split into chunks of 200MB to prevent memory crashes.

### 2. Environment Setup

- Ensure that you have Conda (Miniconda) installed. Activate the Conda environment by running the following command:

    ```
    conda activate python39
    ```

### 3. Data Preprocessing

- Navigate to the `scripts/` folder and preprocess the CIC-IDS 2017 dataset by executing the following script:

    ```
    python3 pre_process_clients.py
    ```

- This script will generate four files for each client, along with a log file. The three most important files are:
  - **`10t-10n-IDS2017-dataset-test.hdf5`**: The test file used to evaluate the final model.
  - **`10t-10n-IDS2017-dataset-train.hdf5`**: The training file used to train the model.
  - **`10t-10n-IDS2017-dataset-val.hdf5`**: The validation file used during training to validate the model.

### 4. Models Training

- Generate and train the models by running the following command:

    ```
    python3 test_algorithms_training_data.py
    ```

### 5. Evaluation

- Evaluate the trained models on the test data of each client using the following command:

    ```
    python3 test_algorithms_unseen_data.py
    ```

### 6. Generate Plots

- Visualize the results of the training process by generating plots with the following command:

    ```
    python3 generate_plots_training.py
    ```
