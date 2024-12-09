
            from sklearn.base import BaseEstimator, TransformerMixin
from datetime import datetime

class HeureCoursTransformer(BaseEstimator, TransformerMixin):
    def __init__(self):
        pass
    def fit(self, X, y=None):
        return self
    
    def transform(self, X, y=None):
        durees = []
        for heure_cours in X['Heure_cours']:
            debut, fin = heure_cours.split('-')
            debut = datetime.strptime(debut, '%H:%M')
            fin = datetime.strptime(fin, '%H:%M')
            duree = (fin-debut).seconds/3600
            durees.append(duree)
        return pd.DataFrame({'Duree_cours': durees})
        