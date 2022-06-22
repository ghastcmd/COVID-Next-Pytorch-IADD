from dataset_transform.rename_files import rename_dataset_files
from dataset_transform.split_dataset import generate_split_dataset_files

from data.equalization import equalize_all_imgs

if __name__ == '__main__':
    rename_dataset_files()
    equalize_all_imgs()
    generate_split_dataset_files()