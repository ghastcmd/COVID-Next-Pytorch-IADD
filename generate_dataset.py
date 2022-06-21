from dataset_transform.rename_files import rename_dataset_files
from dataset_transform.split_dataset import generate_split_dataset_files

if __name__ == '__main__':
    rename_dataset_files()
    generate_split_dataset_files()