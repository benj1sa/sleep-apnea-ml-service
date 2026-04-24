# main.py
import joblib
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
pipeline = joblib.load("rf_100w_lda_1.joblib")

class PredictRequest(BaseModel):
    features: list[float]

@app.post("/predict")
def predict(req: PredictRequest):
    prediction = pipeline.predict([req.features])
    probability = pipeline.predict_proba([req.features])
    return {
        "prediction": int(prediction[0]),
        "probability": probability[0].tolist()
    }