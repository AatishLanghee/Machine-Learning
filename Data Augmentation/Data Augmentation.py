#!/usr/bin/env python
# coding: utf-8

# In[17]:


import imageio
import imgaug as ia
get_ipython().run_line_magic('matplotlib', 'inline')

image = imageio.imread("/home/ubuntu/1.jpg")

print("Original:")
ia.imshow(image)


# In[26]:


from imgaug import augmenters as iaa
ia.seed(4)

rotate = iaa.Affine(rotate=(-25, 25))
image_aug = rotate.augment_image(image)

print("Augmented:")
ia.imshow(image_aug)

import scipy.misc
scipy.misc.imsave('outfile.jpg', image_aug)


# In[ ]:





# In[32]:


from imgaug import augmenters as iaa
ia.seed(4)

rotate = iaa.Affine(rotate=(20, 55))
image_aug = rotate.augment_image(image)

print("Augmented:")
ia.imshow(image_aug)

import scipy.misc
scipy.misc.imsave('outfile2.jpg', image_aug)


# In[ ]:





# In[ ]:





# In[33]:


from imgaug import augmenters as iaa
ia.seed(4)

rotate = iaa.Affine(rotate=(-20, -55))
image_aug = rotate.augment_image(image)

print("Augmented:")
ia.imshow(image_aug)

import scipy.misc
scipy.misc.imsave('outfile3.jpg', image_aug)


# In[ ]:





# In[ ]:





# In[34]:


from imgaug import augmenters as iaa
ia.seed(4)

rotate = iaa.Affine(rotate=(-50, -90))
image_aug = rotate.augment_image(image)

print("Augmented:")
ia.imshow(image_aug)

import scipy.misc
scipy.misc.imsave('outfile4.jpg', image_aug)


# In[ ]:





# In[28]:


import numpy as np

images = [image]
images_aug = rotate.augment_images(images)

print("Augmented batch:")
ia.imshow(np.hstack(images_aug))
import scipy.misc
scipy.misc.imsave('outfile1.jpg', image_aug)


# In[ ]:





# In[ ]:





# In[9]:


seq = iaa.Sequential([
    iaa.Affine(rotate=(-25, 25)),
    iaa.AdditiveGaussianNoise(scale=(10, 60)),
    iaa.Crop(percent=(0, 0.2))
])

images_aug = seq.augment_images(images)

print("Augmented:")
ia.imshow(np.hstack(images_aug))


# In[ ]:





# In[ ]:





# In[38]:


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
dstpath = '/home/ubuntu/test1/' # Destination Folder
try:
    makedirs(dstpath)
except:
    print ("Directory already exist, images will be written in same folder")
# Folder won't used
files = [f for f in listdir(path) if isfile(join(path,f))] 
for image in files:
    try:
        img = imageio.imread(os.path.join(path,image))
        #gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        rotate = iaa.Affine(rotate=(-25, 25))
        image_aug = rotate.augment_image(img)
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





# In[ ]:




