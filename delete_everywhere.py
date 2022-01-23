# This script deletes a given directory recursives in all of the subdirectories of the parent folder
# Pre-requisites : You have to have python 3.x or greater installed on your machine
# 1. Run the script
# 2. Provide Parent directory path
# 3. Provide the name of the directory to be deleted
# 4. Deletion will take a while to complete depending upon the processor
# 5. Wait until you see the message 'Directory list in which <Directory to be deleted> is present now'
# Example use case: Parent Directory: Any drive or path, Directory to be deleted: node_modules
# Enter the Parent directory path: D:
# Enter the directory to be deleted: node_modules
# Future improvements : Choose to delete a directory or file everywhere inside the specified parent folder
# Authors : Sai Srinivasa Bhardhwaj, Sai Bala Krishna Allamsetty

import os
import shutil
directories_list = []


def fetch_func(parent_folder, directory_to_deleted):
    dir_list = [name for name in os.listdir(
        parent_folder) if os.path.isdir(os.path.join(parent_folder, name))]
    for dir in dir_list:
        if dir != directory_to_deleted:
            fetch_func(os.path.join(parent_folder, dir), directory_to_deleted)
        else:
            directories_list.append(os.path.join(
                parent_folder, directory_to_deleted))


def delete_directories(directories_list):
    for dir in directories_list:
        print('Trying to delete: ', dir)
        shutil.rmtree(dir, ignore_errors=True)
        print("Deleted", dir)


parent_folder = input('Enter the Parent directory path: ')
directory_to_deleted = input('Enter the directory to be deleted: ')


fetch_func(parent_folder, directory_to_deleted)
print('Directory list in which ', directory_to_deleted,
      'is present: \n ', directories_list)
delete_directories(directories_list)
fetch_func(parent_folder, directory_to_deleted)
print('Directory list in which ', directory_to_deleted,
      'is present now: \n ', directories_list)
print(directories_list)
