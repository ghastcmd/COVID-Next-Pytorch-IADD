import os

if __name__ == '__main__':
    os.system('py ./dataset_transform/rename_files.py')
    os.system('py ./dataset_transform/split_dataset.py')