import pandas as pd
import numpy as np
from sklearn.utils import shuffle
import random
import matplotlib.pyplot as plt
from progiter import ProgIter
import os, shutil
import cv2
import warnings
warnings.simplefilter('ignore')

def get_intensite(data : pd.core.frame.DataFrame = None, index : int=0):
    
    img = cv2.imread( data.Path_images.loc[index][:10] + ' PP' + data.Path_images.loc[index][10:] + data['File'].loc[index]+'.png', cv2.IMREAD_GRAYSCALE)
    
    image_l = img.tolist()
    image_fl = []
    image_flze = []
    
    for i in range(0,len(image_l)):  # transfromation de l'array en liste de d'intensité de 0 à 255
        image_fl += image_l[i]
    
    for i in np.flatnonzero(image_fl): # liste d'intensité de 1 à 255
        image_flze.append(image_fl[i])
        
    data['Intensite'].loc[index] = [image_flze.count(i) for i in range(0,256)] # liste representant la distribution d'intensité non normalisé de l'image 
    
    return None


############# MAIN#################
size = 1345
test_size = int(2* size // 10)

l_label = ["Normal", "Viral_Pneumonia","Lung_Opacity", "COVID"]
dict_label = {'Normal':'Normal', 'Viral_Pneumonia':'Malade', 'Lung_Opacity':'Malade', 'COVID':'Malade'}
l_diag = [0,1,1,1]                       # Creation d'une liste pour uniformiser les codes couleurs
l_path = ['./Datasets/Normal/','./Datasets/Viral_Pneumonia/','./Datasets/Lung_Opacity/','./Datasets/COVID/']

col_name = {'FILE NAME' : 'File',
            'FORMAT' : 'Format',
            'SIZE' : 'Size',
            }
l_count = []
l_df = []
        
for index, diag in ProgIter(zip(range(0,4), l_diag)):
            l_df.append(pd.read_excel('./Datasets/'+l_label[index]+ ".metadata.xlsx"))   # Enlister les dataframe    
            l_df[index] = l_df[index].rename(col_name, axis=1)         # Renommer les colonnes des dataframes
            l_df[index]['Diagnostic'] = diag                           # Creation d'une colonne 'Diagnostic'
            l_df[index]['Path_images'] = l_path[index]                 # Creation d'une colonne contenant le chemin des fichiers images
            l_df[index]['Usage'] = 'Trainning'
            if diag == 0:
                l_df[index] = l_df[index].loc[ random.sample(range(0,l_df[index].shape[0]),3*size) ].reset_index().drop(['index','Format','Size','URL'],axis=1)
                l_df[index].iloc[:3*test_size,3] = 'Test'
            else:
                l_df[index] = l_df[index].loc[ random.sample(range(0,l_df[index].shape[0]),size) ].reset_index().drop(['index','Format','Size','URL'],axis=1)
                l_df[index].iloc[:test_size,3] = 'Test'         
            
df_radios = pd.concat([l_df[index] for index in range(0,4)], axis = 0, ignore_index=True)
df_radios = shuffle(df_radios, random_state = 69).reset_index()
df_radios = df_radios.drop(['index'],axis=1)
df_radios.insert(2,'Intensite', [[] for i in range(len(df_radios))])



from progiter import ProgIter


for index in ProgIter(range(0,len(df_radios),1)):
    get_intensite(df_radios,index)

df_radios = df_radios.drop(['Path_images'],axis=1)
df_test = df_radios[df_radios.Usage == 'Test'].drop(['Usage','File'],axis=1)
df_train = df_radios[df_radios.Usage == 'Trainning'].drop(['Usage','File'],axis=1)
df_test.to_json('./Test_Intensite_H.json')
df_train.to_json('./Train_Intensite_H.json')