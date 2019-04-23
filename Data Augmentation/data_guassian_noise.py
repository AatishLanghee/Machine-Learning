#!/usr/bin/env python
# coding: utf-8

# # Data Augmentation flip code

# In[1]:


import cv2
import imageio
import imgaug as ia
get_ipython().run_line_magic('matplotlib', 'inline')
import os,glob
import scipy.misc
from imgaug import augmenters as iaa
ia.seed(4)

from os import listdir,makedirs

from os.path import isfile,join
path = '/home/ubuntu/Desktop/' # Source Folder
dstpath = '/home/ubuntu/Aatish/test1' # Destination Folder
try:
    makedirs(dstpath)
except:
    print ("Directory already exist, images will be written in same folder")
# Folder won't used

seq = iaa.Sequential([
    iaa.Affine(rotate=(0, -25)),
    iaa.AdditiveGaussianNoise(scale=(10, 60)),
    iaa.Crop(percent=(0, 0.2))
])



files = [f for f in listdir(path) if isfile(join(path,f))] 
for image in files:
    try:
        img = imageio.imread(os.path.join(path,image))
        #gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        rotate = iaa.Affine(rotate=(-25, 25))
        image_aug = seq.augment_image(img)
        dstPath = join(dstpath,image)
        scipy.misc.imsave(dstPath,image_aug)
    except:
        print ("{} is not converted".format(image))
for fil in glob.glob("*.jpg"):
    try:
        image = cv2.imread(fil) 
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # convert to greyscale
        cv2.imwrite(os.path.join(dstpath,fil),gray_image)
    except:
        print('{} is not converted')


# In[ ]:




