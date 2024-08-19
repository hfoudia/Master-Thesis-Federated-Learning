import pandas as pd
import matplotlib.pyplot as plt
import os

# Load the CSV file
training_dir = '../models/training/'


for folder in os.listdir(training_dir):
    subfolder_path = os.path.join(training_dir, folder)

    df = pd.read_csv(subfolder_path + '/federated-tuning.csv')

    # Extract the rounds and F1 scores for each client
    rounds = df['Round']
    clients_f1_scores = df.filter(like='client-').filter(like='(f1)')

    # Plot each client's F1 score over the rounds
    plt.figure(figsize=(10, 6))
    for client in clients_f1_scores.columns:
        plt.plot(rounds, clients_f1_scores[client], label=client)

    # Add labels, title, and legend
    plt.xlabel('Number of Rounds')
    plt.ylabel('F1 Score')
    plt.title('F1 Score per Client over Rounds')
    plt.legend(title='Clients')
    plt.grid(True)

    # Create the 'training' folder if it doesn't exist
    os.makedirs('../plots/training', exist_ok=True)
    
    # Save & Show the plot
    plt.savefig(f'../plots/training/{folder}_f1_scores_per_client.png', dpi=300)
    plt.show()
