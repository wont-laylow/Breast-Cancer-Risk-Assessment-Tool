import joblib
from pathlib import Path
import pandas as pd
from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from app.schemas import PatientData
import time


app = FastAPI(title="Breast Cancer Prediction API",
              version="1.0.0",
              description="API for predicting breast cancer using a pre-trained weighted voting classifier.")

model_path = Path(__file__).resolve().parent.parent / "model_files" / "weighted_voting_pipeline.pkl"
model = joblib.load(model_path)

# Mount static folder and templates
app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/predict", response_class=HTMLResponse)
def predict(
    request: Request,
    Age: str = Form(...),
    Education: str = Form(...),
    Family_History: str = Form(...),
    Parity: str = Form(...),
    Menarche_Age: str = Form(...),
    Menopause_Age: str = Form(...),
    Body_Size: str = Form(...)
):
    try:
        input_data = pd.DataFrame([{
            "Age": Age,
            "Education": Education,
            "Family_History": Family_History,
            "Parity": Parity,
            "Age_at_Menarche": Menarche_Age,
            "Age_at_Menopause": Menopause_Age,
            "Body_Size": Body_Size
        }])
        
        pred = model.predict(input_data)
        proba = model.predict_proba(input_data)

        result = {
            "prediction": int(pred[0]),
            "positivity_score": round(float(proba[0][1]) * 100, 2),
            "negativity_score": round(float(proba[0][0]) * 100, 2),
            "interpretation": "High risk" if pred[0] == 1 else "Low risk"
        }

        time.sleep(1.5)

        return templates.TemplateResponse(
            "index.html",
            {"request": request, "result": result}
        )
    except Exception as e:
        return templates.TemplateResponse(
            "index.html",
            {"request": request, "error": str(e)}
        )