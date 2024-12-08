from fastapi import FastAPI, HTTPException
import resquests


app = FastAPI()

@app.get("/hello")
def het_mesage():
    try:
        content = f"You're welcome in StudentApp"
        return content 
    except Exception as e:
        return f"Error {str(e)}"