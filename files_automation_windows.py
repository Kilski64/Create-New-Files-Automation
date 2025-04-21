import os
import shutil

# specify the source directory containining the files you want to add
source_dir = r'INSERT FILE PATH'

# specify the destination directory in windows file explorer
destination_dir = r'INSERT FILE PATH DESTINATION'

# repeat the process # of times
for i in range(10):
    # Get a list of files in the source directory
    files = os.listdir(source_dir)

    # copy each file from the source directory to the destination directory
    for file in files:
        source_file_path = os.path.join(source_dir, file)
        destination_file_path = os.path.join(destination_dir, file)
        shutil.copy(source_file_path, destination_file_path)

    print(f"Iteration {i+1}: Files added to windows file explorer.")

print("All iterations completed.")