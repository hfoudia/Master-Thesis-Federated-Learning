""" 
    Purpose: Run different tests with different algorithms and hyperparameters.
"""

import subprocess
import os
import time

# Tests to run
tests = {
    "test_FLAD_auto": {'training_mode': "flad", 'epochs': 0, 'batch_size': 0},
    "test_FedAvg_e1_b50": {'training_mode': "fedavg", 'epochs': 1, 'batch_size': 50},
    "test_FedAvg_e5_b50": {'training_mode': "fedavg", 'epochs': 5, 'batch_size': 50},
    "test_FLDDoS_e10_b100" : {'training_mode': "flddos", 'epochs': 10, 'batch_size': 100},
}

for test in tests:
    print(f"Running test {test}")

    # Create folder to save model
    folder_name = f"model-{tests[test]['training_mode']}_e{tests[test]['epochs']}_b{tests[test]['batch_size']}"
    folder_path = os.path.join("../models/training", folder_name)
    os.makedirs(folder_path, exist_ok=True)
    
    # Start timer
    start_time = time.time()

    # Run program
    program_command = f"python3 ../FLAD/flad_main.py --clients ../clients --training_mode {tests[test]['training_mode']} --local_epochs {tests[test]['epochs']} --batch_size {tests[test]['batch_size']} -o {folder_path} >> {folder_path}/output.txt"
    subprocess.run(program_command, shell=True)

    # Stop timer and calculate elapsed time in seconds
    elapsed_time = time.time() - start_time

    # Save elapsed time in seconds to a file
    time_file_path = os.path.join(folder_path, "time.txt")
    with open(time_file_path, "w") as time_file:
        time_file.write(str(elapsed_time))