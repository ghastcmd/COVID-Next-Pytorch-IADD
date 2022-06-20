import logging

from torch.utils.data import DataLoader

from data import transforms
from data.dataset import COVIDxFolder
import config

log = logging.getLogger(__name__)

use_gpu = config.gpu

log.info("Loading train dataset")
train_dataset = COVIDxFolder(config.train_imgs, config.train_labels,
                                transforms.train_transforms(config.width,
                                                            config.height))

log.info('Loaded the file loader dataset')

train_loader = DataLoader(train_dataset,
                            batch_size=config.batch_size,
                            shuffle=True,
                            drop_last=True,
                            num_workers=config.n_threads,
                            pin_memory=use_gpu)
log.info("Number of training examples {}".format(len(train_dataset)))