import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.utils import shuffle
from progiter import ProgIter
import cv2

import os, pathlib
import shutil #pour copier des fichiers vers les dossiers de preprocessing

l_label = ["Normal", "Viral_Pneumonia","Lung_Opacity", "COVID"]
l_diag = [0,1,2,3]
l_path=['./Datasets/Normal/','./Datasets/Viral_Pneumonia/','./Datasets/Lung_Opacity/','./Datasets/COVID/']


def init_raw_dataset():


  col_name = {'FILE NAME' : 'File',
            'FORMAT' : 'Format',
            'SIZE' : 'Size',
            }
  l_count = []
  l_df = []
        
  for index, diag in zip(range(0,4), l_diag):
    l_df.append(pd.read_excel('./Datasets/'+l_label[index]+ ".metadata.xlsx"))   
    l_count.append(l_df[index].shape[0])   
    l_df[index] = l_df[index].rename(col_name, axis=1)         
    l_df[index]['Diagnostic'] = diag                           
    l_df[index]['Path_images'] = l_path[index]

  return l_df


def load(file):
  return cv2.imread(file, cv2.IMREAD_GRAYSCALE)

def load_and_resize(file):
  return cv2.imread(file, cv2.IMREAD_GRAYSCALE).resize(img, (256, 256))

def load_mask(file):
  return cv2.imread(file.replace("images","masks"), cv2.IMREAD_GRAYSCALE)

def apply_mask(file):
  return cv2.bitwise_and(load_and_resize(file), load_mask(file))
    
def any_random_file(l_df):
  selected_class = np.random.choice(range(4))
  return l_path[selected_class] + 'images/'+ np.random.choice(l_df[selected_class].File)+'.png'

  
  