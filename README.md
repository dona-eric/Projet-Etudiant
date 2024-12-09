# API de prédiction des risques pour la santé des étudiants
## Description
Ce projet consiste à développer une API capable de prédire le niveau de risque de santé des étudiants en fonction de données liées à leur stress, sommeil, présence en cours, et autres facteurs. L'application repose sur un modèle de machine learning intégré dans un pipeline avec des transformations personnalisées pour traiter les données spécifiques, telles que la durée des cours.
## Structure du projet


Projet_Etudiant/
├── Data_Health_Student/
│   ├── Analyse_health/
│   │   ├── analyse_student.ipynb  # Notebook contenant l'analyse et la préparation des données
│   │   ├── model_etudiant.pkl     # Modèle de machine learning sauvegardé
│   └── Student_app/
│       ├── app_health.py          # Code FastAPI pour déployer le modèle
│       └── utils/
│           └── heure_cours_transformer.py  # Classe personnalisée pour transformer les heures de cours
├── requirements.txt               # Fichier contenant les dépendances
└── README.md                      # Documentation du projet

## Fonctionnalités
     *** Points de terminaison de l'API :

      GET /hello : Retourne un message de bienvenue.
      POST /risque_level_student : Prend en entrée les données d'un étudiant et retourne son niveau de risque ( Low, Medium, High).
      Pipeline de Machine Learning :

  #### Prend en charge les données catégorielles et numériques.
  #### Intégrez une transformation personnalisée ( HeureCoursTransformer) pour calculer la durée du cours.
  #### Modèle :
  
  Le modèle utilisé est un RandomForestClassifierentraînement sur un jeu de données simulé de 15 000 étudiants.
 ## Étapes de développement
        1. Préparation des données
        Les données incluent des colonnes comme Stress Level (GSR), Temps_sommeil, Niveau_anxiety, et Heure_cours.
        Une transformation personnalisée a été implémentée pour extraire la durée des cours ( HeureCoursTransformer).
    2. Entraînement du modèle
    Le pipeline comprend :
    StandardScalerpour les données numériques.
    OneHotEncoderpour les données catégorielles.
    Le transformateur HeureCoursTransformerpour les heures de cours.
    Modèle adapté : RandomForestClassifier.
    Sauvegarde du modèle avec joblib: joblib.dump(filename, "filename.pkl')

    3. Développement de l'API avec FastAPI
    Le modèle sauvegardé est chargé dans le fichier app_health.py.
## Points finaux principaux :
    GET /hello : Vérifie que l'API fonctionne correctement.
    POST /risque_level_student : Acceptez une requête contenant les données d'un étudiant au format JSON et retournez le niveau de risque.

### Exécution du projet
    Lancer l'API : uvicorn app_health:app --reload


## Auteur
    Nom : KOULODJI D. Eric - Data Scientist & Développeur Python-DJango, Physicien Théoricien


## Licence
Ce projet est sous licence MIT. Vous êtes libre de l'utiliser, de le modifier et de le distribuer tant que les mentions d'origine sont respectées.






