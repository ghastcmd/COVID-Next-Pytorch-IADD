# General
name = "COVIDNext50_NewData"
gpu = True
batch_size = 16
n_threads = 4
random_seed = 1337

# Model
# Model weights path
weights = "" # ./experiments/ckpts/<model.pth>

# Optimizer
lr = 1e-4
weight_decay = 1e-3
lr_reduce_factor = 0.7
lr_reduce_patience = 5

# Data
train_imgs = "./dataset/Base IADD"
train_labels = "./dataset/Base IADD/train.txt"

val_imgs = "./dataset/Base IADD"
val_labels = "./dataset/Base IADD/test.txt"

#! Change this to modify the number of clases
# Categories mapping
mapping = {
    'Typical and Atypical': 0,
    'Indeterminate': 1,
}
# Loss weigths order follows the order in the category mapping dict
loss_weights = [0.05, 0.05]

width = 256
height = 256
n_classes = len(mapping)

# Training
epochs = 600
log_steps = 1
eval_steps = 1
ckpts_dir = "./experiments/ckpts"
