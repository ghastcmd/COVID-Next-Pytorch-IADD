import os 
import random

from sklearn.model_selection import train_test_split

def pair_shuffle(list1, list2, seed):
    assert(len(list1) == len(list2))
    
    random.seed(seed)
    index_list = [x for x in range(len(list1))]
    random.shuffle(index_list)
    
    return_list1 = []
    return_list2 = []

    for index in index_list:
        return_list1.append(list1[index])
        return_list2.append(list2[index])
        
    return return_list1, return_list2

def split(input_list, labels, ratio, seed):
    return_list, return_labels = pair_shuffle(input_list, labels, seed)

    index = int(len(input_list) - len(input_list) * ratio)
    return (return_list[:index], return_list[index:],
            return_labels[:index], return_labels[index:])

def write_to_folder(dir_name, file_name, iter_list_x, iter_list_y):
    assert(len(iter_list_x) == len(iter_list_y))

    with open(os.path.join(dir_name, file_name), 'w+') as fp:
        fp.write('img_path,label\n')
        for line, label in zip(iter_list_x, iter_list_y):
            fp.write(f'{line},{label}\n')

def generate_split_dataset_files():
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
    
    ant_labels = [0 for _ in range(len(atypical_n_typical))]
    ind_labels = [1 for _ in range(len(indeterminate))]

    ant_x_train, ant_x_test, ant_y_train, ant_y_test = split(atypical_n_typical, ant_labels, 0.3, 123)
    ind_x_train, ind_x_test, ind_y_train, ind_y_test = split(indeterminate, ind_labels, 0.3, 123)

    total_x_train = ant_x_train + ind_x_train
    total_x_test = ant_x_test + ind_x_test
    
    total_y_train = ant_y_train + ind_y_train
    total_y_test = ant_y_test + ind_y_test
    
    total_x_train, total_y_train = pair_shuffle(total_x_train, total_y_train, 123)
    total_x_test, total_y_test = pair_shuffle(total_x_test, total_y_test, 123)

    write_to_folder(base_dir, 'train.txt', total_x_train, total_y_train)
    write_to_folder(base_dir, 'test.txt', total_x_test, total_y_test)
    
if __name__ == '__main__':
    generate_split_dataset_files()