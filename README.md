oct23_bds_radios_pulmonaires
==============================
Répertoire du projet Radios Pulmonaires dans le cadre du bootcamp Data Scientist d'octobre 2023 (Datascientest).
Equipe projet : Steve Costalat, Nicolas Gorgol, Thibaut Gazagnes

Project Organization
------------

    ├── LICENSE
    ├── README.md          <- The top-level README for developers using this project.
    
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    
    ├── data               ######       LES .ZIP et les Images NE SONT PAS STOCKEE SUR CE GITHUB
    |   ├── raw            le fichier RAW info.txt contient les infos sur la composition et les origines des données brutes.
    │   │                  ~/notebook/1.0-steve-data-exploration et 1.0-Thibault-data-exploration, s'appuient sur ce jeu
    │   │
    │   ├── preprocess     <- un fichier Preprocessing_1.zip contenant toutes les images transformées en images masquées de 256*256, 
    │   │                  en mode 'Grayscale' a été géneré avec le programme suivant: ~/src/2.0-Thibault-Preprocessing.py
    │   │
    │   ├── split_balanced <- un fichier TestTrain. zip a été crée avec le programme  ~/src/1.0-Steve-BalanceNSplit.py.
    │   │                  il contient 4304 images masquées équilibré sur 4 classes dans un jeu TRAIN
    │   │                  il contient 4304 images masquées équilibré sur 4 classes dans un jeu TEST
    │   │
    │   └── reduites    <- jeux de donnée des images masquée reduites à leur distribution d'intensité avec: ~/src/1.0-Steve-Reduce-BalanceNSplit.py
    │        └── Train_Intensite_H.json   <- Jeu d'entrainement equilibrées sur deux classes de 6458 images reduites 
    │        └── Test_Intensite_H.json   <- Jeu d'entrainement equilibrées sur deux classes de 6458 images reduites 

    │
    ├── notebooks          
    |   └── 1.0-steve-data-exploration  
    |   └── 1.0 Thibaut data exploration                   

    
    │
    ├── references         <- Data dictionaries, manuals, links, and all other explanatory materials.
    │
    ├── reports            <- The reports that you'll make during this project as PDF
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │

    │
    ├── src                <- Source code for use in this project.
    │   ├── 2.0 Thibault Preprocessing       <- Source code pour l'application du preprocessing sur l'intégralité du jeu de données brute
    │   ├── 1.0 Steve BalanceNSplit          <- Source code pour la création des jeux TRAIN et TEST equilibrés
    │   ├── 1.0 Steve Reduce-BalanceNSplit          <- Source code pour la création des jeux TRAIN et TEST equilibrés│pour l'approche REDUITE


    
    │   ├── visualization  <- Scripts to create exploratory and results oriented visualizations
    │   │   └── visualize.py

------------------------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
