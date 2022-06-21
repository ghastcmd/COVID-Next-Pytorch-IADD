import os

def rename_dataset_files():
    base_folders = [
        './dataset/Base IADD/Atypical',
        './dataset/Base IADD/Indeterminate',
        './dataset/Base IADD/Typical',
    ]
    for base_folder in base_folders:
        for file in os.listdir(base_folder):
            if os.path.isfile(os.path.join(base_folder, file)):
                name, ext = file.split('.')
                os.rename(
                    os.path.join(base_folder, file),
                    os.path.join(base_folder, f'{name:0>4}.{ext}')
                )

if __name__ == '__main__':
    rename_dataset_files()