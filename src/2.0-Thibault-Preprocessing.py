### Plan de preprocessing : 
#* Ouvrir chaque image avec son masque associé
#* Convertir en Grayscale
#* Redimensionner les images à la taille des masques (256 * 256)
#* Appliquer les masques

#Import des bibliothèques
import pandas as pd
import numpy as np
import os, pathlib
from tqdm import tqdm
import cv2
import shutil #pour copier des fichiers vers les dossiers de preprocessing

#Sous-fonction qui ouvre une image à partir du filepath, la convertit en Grayscale et la redimensionne en 256*256
#En input : le filepath d'une image dans le dossier "image" => plutôt retravailler le masque
def load_and_resize(file):
    img = cv2.imread(file, cv2.IMREAD_GRAYSCALE)
    img_resized = cv2.resize(img, (256, 256))
    return img_resized

#Sous-fonction qui va chercher le masque et le convertit en Grayscale
#En input : le filepath d'une image dans le dossier "image" qui est l'input de la fonction finale
def load_mask(file):
    mask_path = file.replace("images","masks")
    mask = cv2.imread(mask_path, cv2.IMREAD_GRAYSCALE)
    return mask

#Fonction qui applique le masque et enregistre l'image ainsi préprocessée dans un nouveau dossier
#Input : image et masque (données d'origine), nom du fichier et chemin du dossier cible pour l'enregistrement
def get_masked_imgs(sourceimg, nom_cible, dossier_cible):
    img_resized = load_and_resize(sourceimg)
    mask = load_mask(sourceimg)
    img_masked = cv2.bitwise_and(img_resized, mask)
    cv2.imwrite(os.path.join(dossier_cible, nom_cible), img_masked)

#Définition des dossiers d'origine et cible, et lancement des fonctions => voir le script python dans SRC

dossiers_source_dict = {"TEST" : "../data/test/images/"}
dossier_cible = "..\\data\\Preprocessing_1"

#Itérer sur les dossiers pour récupérer les fichiers images 
for n,filepath in dossiers_source_dict.items():
    for f in tqdm(os.listdir(filepath)):
        nom_cible = f
        file = os.path.join(filepath, f)
        get_masked_imgs(file, nom_cible, dossier_cible)