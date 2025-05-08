# Prédiction d'AVC (Stroke Prediction)

Ce projet vise à prédire la probabilité qu'un patient ait un accident vasculaire cérébral (AVC) en utilisant des données médicales et démographiques. Le projet utilise des techniques de machine learning pour analyser les facteurs de risque et développer un modèle prédictif fiable.

## 📋 Description du Projet

Ce projet est une implémentation d'un système de prédiction d'AVC basé sur des données médicales. Il utilise des algorithmes de machine learning pour identifier les patients à risque et aider les professionnels de santé dans leur prise de décision.

## 🏗️ Structure du Projet

```
kaggle-stroke-prediction/
├── data/                  # Dossier contenant les données
├── notebooks/            # Notebooks Jupyter
│   ├── data_preprocessing.ipynb
│   ├── eda.ipynb
│   └── model_training.ipynb
├── src/                  # Code source Python
│   ├── load_data.py
│   └── load_libs.py
├── requirements.txt      # Dépendances Python
└── README.md            # Documentation
```

## 📊 Données

Le jeu de données contient les informations suivantes pour chaque patient :

1. **id**: identifiant unique
2. **gender**: genre ("Male", "Female" ou "Other")
3. **age**: âge du patient
4. **hypertension**: présence d'hypertension (0: non, 1: oui)
5. **heart_disease**: présence de maladies cardiaques (0: non, 1: oui)
6. **ever_married**: statut marital ("No" ou "Yes")
7. **work_type**: type de travail ("children", "Govt_jov", "Never_worked", "Private" ou "Self-employed")
8. **Residence_type**: type de résidence ("Rural" ou "Urban")
9. **avg_glucose_level**: niveau moyen de glucose dans le sang
10. **bmi**: indice de masse corporelle
11. **smoking_status**: statut tabagique ("formerly smoked", "never smoked", "smokes" ou "Unknown")
12. **stroke**: présence d'AVC (1: oui, 0: non)

## 🛠️ Technologies Utilisées

- Python 3.x
- Pandas & NumPy pour la manipulation des données
- Scikit-learn pour le machine learning
- XGBoost pour le modèle de prédiction
- Matplotlib & Seaborn pour la visualisation
- Jupyter Notebooks pour l'analyse et le développement

## 🚀 Installation

1. Clonez le repository :
```bash
git clone https://github.com/votre-username/kaggle-stroke-prediction.git
cd kaggle-stroke-prediction
```

2. Créez un environnement virtuel et installez les dépendances :
```bash
python -m venv venv
source venv/bin/activate  # Sur Windows : venv\Scripts\activate
pip install -r requirements.txt
```

## 📝 Utilisation

1. Prétraitement des données :
```bash
jupyter notebook notebooks/data_preprocessing.ipynb
```

2. Analyse exploratoire des données :
```bash
jupyter notebook notebooks/eda.ipynb
```

3. Entraînement du modèle :
```bash
jupyter notebook notebooks/model_training.ipynb
```

## 📈 Fonctionnalités

- Prétraitement des données avec gestion des valeurs manquantes
- Analyse exploratoire des données (EDA)
- Entraînement de modèles de machine learning (XGBoost, Random Forest)
- Évaluation des performances du modèle
- Visualisation des résultats

## 🤝 Contribution

Les contributions sont les bienvenues ! N'hésitez pas à :
1. Fork le projet
2. Créer une branche pour votre fonctionnalité
3. Commiter vos changements
4. Pousser vers la branche
5. Ouvrir une Pull Request

## 📄 Licence

Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails.

## 👥 Auteurs

- Votre Nom - Développeur Principal

## 🙏 Remerciements

- Kaggle pour le jeu de données
- La communauté open source pour les outils et bibliothèques utilisés