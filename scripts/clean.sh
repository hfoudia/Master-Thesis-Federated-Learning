#!/bin/bash

# Define the directory paths
directory1="../models"
directory2="../plots"

# Check if the first directory exists
if [ -d "$directory1" ]; then
    # Remove all folders in the first directory
    rm -rf "$directory1"/*/
    echo "All folders in $directory1 have been removed."
else
    echo "Directory $directory1 does not exist."
fi

# Check if the second directory exists
if [ -d "$directory2" ]; then
    # Remove all folders in the second directory
    rm -rf "$directory2"/*/
    echo "All folders in $directory2 have been removed."
else
    echo "Directory $directory2 does not exist."
fi