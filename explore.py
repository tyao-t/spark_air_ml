# import pandas as pd

# file_path = '2023/01017099999.csv'

# data = pd.read_csv(file_path)

# # print(data.head(10))
# print(data.columns)

# print("LONGITUDE 10:")
# print(data['LONGITUDE'].head(5))

# print("\nLATITUDE 10:")
# print(data['LATITUDE'].head(5))

# print("\nELEVATION 10:")
# print(data['ELEVATION'].head(5))

# print("\nWND 10:")
# print(data['WND'].head(5))

# print("\nCIG 10:")
# print(data['CIG'].head(5))

# print("\n\VIS 10:")
# print(data['VIS'].head(5))

# print("\n\TMP 10:")
# print(data['TMP'].head(5))

# print("\n\DEW 10:")
# print(data['DEW'].head(5))

# print("\n\SLP 10:")
# print(data['SLP'].head(5))


import os
import random
import shutil

def count_and_sample_files(directory, sample_size=200):
    # Get the list of all entries in the directory
    entries = os.listdir(directory)
    
    # Filter out only files (not directories)
    files = [entry for entry in entries if os.path.isfile(os.path.join(directory, entry))]
    
    # Count the number of files
    num_files = len(files)
    
    # Randomly sample the files
    sampled_files = random.sample(files, min(sample_size, num_files))
    
    return num_files, sampled_files

def copy_sampled_files(source_directory, sampled_files):
    # Define the destination directory
    destination_directory = os.path.join('./sample')
    
    # Create the destination directory if it does not exist
    if not os.path.exists(destination_directory):
        os.makedirs(destination_directory)
    
    # Copy each sampled file to the destination directory
    for file_name in sampled_files:
        source_file_path = os.path.join(source_directory, file_name)
        destination_file_path = os.path.join(destination_directory, file_name)
        shutil.copy(source_file_path, destination_file_path)
    
    print(f"Copied {len(sampled_files)} files to {destination_directory}")

if __name__ == "__main__":
    source_directory = "./2023/"  # Replace with your directory path
    sample_size = 200
    
    num_files, sampled_files = count_and_sample_files(source_directory, sample_size)
    
    print(f"Total number of files: {num_files}")
    print(f"Randomly sampled files: {sampled_files}")
    
    copy_sampled_files(source_directory, sampled_files)