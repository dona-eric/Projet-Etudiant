from fastapi import FastAPI, HTTPException
import joblib
import pandas as pd
from Data_python import heure_cours_transformer
import sys


sys.path.append('/home/dona-erick/Projet-Etudiant') 

# laod the model
model_etudiant = joblib.load('/home/dona-erick/Projet-Etudiant/Data_Health_Student/Analyse_health_student/model_etudiant.pkl', mmap_mode='r')

app = FastAPI()

@app.get("/hello")
def get_mesage():
    try:
        content = f"You're welcome in StudentApp"
        return content 
    except Exception as e:
        return f"Error {str(e)}"
    

@app.post("/risque_level_student")
def risque_etudiant(data: dict):
    ## code pour la request api
    try:
        df = pd.DataFrame(data)
        ## predictions en faisant passer les données df au modèle
        predictions = model_etudiant.predict(df)
        prediction = predictions[0]
        if prediction == 2:
           return {"niveau_risque": "High", "message": "Le niveau de risque de l'étudiant est élevé."}
        elif prediction == 1:
            return {"niveau_risque": "Medium", "message": "Le niveau de risque de l'étudiant est moyen."}
        else:
            return {"niveau_risque": "Low", "message": "Le niveau de risque de l'étudiant est faible."}
    except Exception as e:
        return HTTPException(status_code=500, detail= {str(e)})
    
        
        
        