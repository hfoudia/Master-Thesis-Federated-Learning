""" 
    Purpose: Pre-process the dataset for each client using the lucid_dataset_parser.py script 
"""

import subprocess
import os

NUM_CLIENTS = len(next(os.walk('../clients/'))[1]) # get number of directories in clients folder

for x in range(1, NUM_CLIENTS+1):
    subprocess.run(f'python3 ../LUCID/lucid_dataset_parser.py \
                    --dataset_type IDS2017 \
                    --dataset_folder ../clients/client-{x}/ \
                    --packets_per_flow 10 \
                    --dataset_id IDS2017 \
                    --traffic_type all \
                    --time_window 10 \
                    && python3 ../LUCID/lucid_dataset_parser.py \
                    --preprocess_folder ../clients/client-{x}/', shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
    
    print(f'Client-{x} pre-processed\n')

# subprocess.run(["shutdown"]) # shutdown the system after pre-processing all clients