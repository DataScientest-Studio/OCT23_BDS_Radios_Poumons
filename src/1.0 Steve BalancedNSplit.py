import pandas as pd
import numpy as np
from sklearn.utils import shuffle
import random
from progiter import ProgIter
import os, shutil

size = 1345
test_size = int(2* size // 10)

l_label = ["Normal", "Viral_Pneumonia","Lung_Opacity", "COVID"]
l_diag = [0,1,2,3]
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
            l_df[index] = l_df[index].loc[ random.sample(range(0,l_df[index].shape[0]),size) ].reset_index().drop(['index','Format','Size','URL'],axis=1)
            l_df[index].iloc[:test_size,3] = 'Test'      
            
for diag,label in zip(l_diag,l_label):
    
    if len(os.listdir(path='./Test/'+label)) != 0:
        for file in os.listdir(path='./Test/'+label):
            os.remove('./Test/'+ label +'/'+ file)
            
    if len(os.listdir(path='./Train/'+label)) != 0:
        for file in os.listdir(path='./Train/'+label):
            os.remove(path='./Train/'+ label +'/'+file)
            
    for i in ProgIter(range(len(l_df[diag]))):
        if l_df[diag]['Usage'].loc[i] == 'Test':
            shutil.copy('./Datasets PP/' + label +'/'+ l_df[diag].File.loc[i] + '.png', './Test/' + label +'/'+ l_df[diag].File.loc[i]+ '.png')
        else:
            shutil.copy('./Datasets PP/' + label +'/'+ l_df[diag].File.loc[i] + '.png', './Train/' + label +'/'+ l_df[diag].File.loc[i]+ '.png')