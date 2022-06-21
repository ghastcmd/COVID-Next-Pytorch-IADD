import os 
import random

from sklearn.model_selection import train_test_split

def split(input_list, ratio, seed):
    random.seed(seed)
    random.shuffle(input_list)
    index = int(len(input_list) - len(input_list) * ratio)
    return input_list[:index], input_list[index:]

def write_to_folder(dir_name, file_name, iter_list):
    with open(os.path.join(dir_name, file_name), 'w+') as fp:
        for line in iter_list:
            fp.write(f'{line}\n')

if __name__ == '__main__':
    base_dir = './dataset/Base IADD/'
    
    types_folder = [
        ('Atypical', 474, []),
        ('Typical', 474, []),
        ('Indeterminate', 948, []),
    ]

    for type_folder, max_files, to_append in types_folder:
        current_dir = os.path.join(base_dir, type_folder)
        for file in os.listdir(current_dir):
            to_append.append(os.path.join(type_folder, file))

    atypical_n_typical = []
    indeterminate = []
    
    random.seed(123)
    
    for type_folder, max_files, files_list in types_folder:
        to_iter_list = [x for x in range(len(files_list))]
        random.shuffle(to_iter_list)
        
        for num in to_iter_list[:max_files]:
            file_name = f"{num:0>4}.png"
            full_name = os.path.join(type_folder, file_name)
            
            if type_folder == 'Atypical' or type_folder == 'Typical':
                atypical_n_typical.append(full_name)
            elif type_folder == 'Indeterminate':
                indeterminate.append(full_name)
    
    
    ant_train, ant_test = split(atypical_n_typical, 0.3, 123)
    ind_train, ind_test = split(indeterminate, 0.3, 123)

    total_train = ant_train + ind_train
    total_test = ant_test + ind_test
    
    random.seed(123)
    random.shuffle(total_train)
    random.shuffle(total_test)

    write_to_folder(base_dir, 'train.txt', total_train)
    write_to_folder(base_dir, 'test.txt', total_test)