oct23_bds_radios_pulmonaires
==============================

Répertoire du projet Radios Pulmonaires dans le cadre du bootcamp Data Scientist d'octobre 2023 (Datascientest).
Equipe projet : Steve Costalat, Nicolas Gorgol, Thibaut Gazagnes

Project Organization
------------

    ├── LICENSE
    ├── README.md          <- The top-level README for developers using this project.
    ├── data               
    |   ├── raw            le fichier RAW info.txt contient les infos sur la composition et les origines des données brutes.
    │   │                  le notebook 1.0-steve-data-exploration s'appuie sur ce jeu
    │   │
    │   └── preprocess     un fichier Preprocessing_1.zip contients les images brutes transformées en images masquée de 256*256 'Grayscale'.
    │                      il a été crée sur la base du Norebook 
        │<- The original, immutable data dump.
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          1.0-steve-data-exploration
    |                      1.0 Thibaut data exploration
    |                      2.0 Thibaut preprocessing
    |                      <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's name, and a short `-` delimited description, e.g.
    │                         `1.0-alban-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, links, and all other explanatory materials.
    │
    ├── reports            <- The reports that you'll make during this project as PDF
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   ├── visualization  <- Scripts to create exploratory and results oriented visualizations
    │   │   └── visualize.py

------------------------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
