from torchvision import transforms


def train_transforms():
    trans_list = [
        # transforms.Resize((height, width)),
        transforms.RandomVerticalFlip(p=0.6),
        transforms.RandomHorizontalFlip(p=0.6),
        transforms.RandomApply([
            transforms.RandomAffine(degrees=20,
                                    translate=(0.15, 0.15),
                                    scale=(0.8, 1.2),
                                    shear=5)], p=0.6),
        transforms.RandomApply([
            transforms.ColorJitter(brightness=0.3, contrast=0.3)], p=0.6),
        transforms.ToTensor(),
    ]
    return transforms.Compose(trans_list)


def val_transforms():
    trans_list = [
        transforms.ToTensor(),
    ]
    return transforms.Compose(trans_list)
