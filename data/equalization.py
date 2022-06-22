import os

import cv2 as cv


def equalize_all_imgs():
    base_dir = '.\\dataset\\Base IADD\\'
    
    folders = [
        'Atypical',
        'Indeterminate',
        'Typical',
    ]
    
    for folder in folders:
        folder = os.path.join(base_dir, folder)
        for file in os.listdir(folder):
            file = os.path.join(folder, file)
            
            src = cv.imread(file)
        
            src = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
            dst = cv.equalizeHist(src)

            cv.imwrite(file, dst)