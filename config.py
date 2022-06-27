# General
name = "COVIDNext50_NewData"
gpu = True
batch_size = 32
n_threads = 4
random_seed = 1337

# Model
# Model weights path
weights = "" # ./experiments/ckpts/<model.pth>

# Optimizer
lr = 1e-4
weight_decay = 1e-4
lr_reduce_factor = 0.8
lr_reduce_patience = 5
early_stopping_patience = 10

# Data
train_imgs = "./dataset/Base IADD"
train_labels = "./dataset/Base IADD/train.txt"

val_imgs = "./dataset/Base IADD"
val_labels = "./dataset/Base IADD/test.txt"

#! Change this to modify the number of clases
# Categories mapping
mapping = {
    'Typical': 0,
    'Indeterminate and Atypical': 1,
}
# Loss weigths order follows the order in the category mapping dict
loss_weights = [0.05, 0.05]

width = 256
height = 256
n_classes = len(mapping)

# Training
epochs = 300
log_steps = 200
eval_steps = 400
ckpts_dir = "./experiments/ckpts"
