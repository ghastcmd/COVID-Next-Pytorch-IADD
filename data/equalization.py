from __future__ import print_function
import cv2 as cv
import matplotlib.pyplot as plt


src = cv.imread('./dataset/Base IADD/Atypical/0001.png')
if src is None:
    print('Could not open or find the image:')
    exit(0)
print(src.shape)
src = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
dst = cv.equalizeHist(src)
#cv.imshow('Source image', src)
#cv.imshow('Equalized Image', dst)
cv.imwrite('./dataset/Base IADD/Atypical2/0001.png', dst)
#plt.imsave('./dataset/Atypical2/0001.png', dst)
#cv.waitKey()