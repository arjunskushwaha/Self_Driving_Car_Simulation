
# coding: utf-8

# In[8]:


import numpy as np
import pandas as pd
import cv2
import matplotlib.pyplot as plt
from sklearn.utils import shuffle


# In[9]:


IMG_HEIGHT, IMG_WIDTH, IMG_CHANNELS = 76, 280, 3
INPUT_IMG_SHAPE = (IMG_HEIGHT,IMG_WIDTH,IMG_CHANNELS)


# In[10]:


def preProcess_image(img):
    ## Crop the part of image that is not required for prediction 
        # - (Removed the sky and the bonnet of the car)
    belowSky = 50
    CarBonnet = 141 
    img = img[belowSky:CarBonnet]   
    
    ## Resize the image into INPUT_IMG_SHAPE
    img = cv2.resize(img,(IMG_WIDTH,IMG_HEIGHT))
    
    return img


# In[11]:


def get_image(paths,angle):
    '''Returns random chosen camera angle view after pre-processing it and the corresponding steering angle after
       correction'''
    # Randomly choosing between three camera angles available and doing the steering angle correction
    ind = np.random.randint(0,3)
    imgPath = paths[ind]
    if ind == 1:    # Case when the left camera's image is selected
        angle += 0.2  
    elif ind == 2:  # Case when the right camera's image is selected
        angle -= 0.2
    
    # Reading the image (By default, cv2 reads image in BGR format so converting it to RGB using cv2.cvtColor() )
    img = cv2.imread(imgPath)
    img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    
    img = preProcess_image(img)
    
    return img,angle


# In[12]:


def flip_image(img,angle):
    num = np.random.choice(2)
    if num == 0:
        img = cv2.flip(img,1)
        angle = -angle
    return img, angle


# In[13]:


def load_data(PathToCSV):
    ## Loads the data into the memory and preprocesses the data to make it suitable 
     # to be given as input to the Convolutional Neural Network (i.e. our model)
    df = pd.read_csv(PathToCSV,names=['center', 'left','right','steering','throttle','brake','speed'])
    X = df[['center','left','right']].values
    Y = df['steering']
    XData = np.empty([X.shape[0],IMG_HEIGHT,IMG_WIDTH,IMG_CHANNELS],dtype='uint8')
    YData = np.empty([Y.shape[0]])
    for ix in range(X.shape[0]):
        img,angle = get_image(X[ix],Y[ix])
        img,angle = flip_image(img,angle)
        XData[ix] = img
#         XData[X.shape[0]+ix] = flip_img
        YData[ix] = angle
#         YData[X.shape[0]+ix] = flip_angle
    shuffle(XData,YData,random_state=0)
    return XData,YData

