from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
import joblib

app = FastAPI()

class request_body(BaseModel):
    A_id: int
    Size: float
    Weight: float
    Sweetness: float
    Crunchiness: float
    Juiciness: float
    Ripeness: float
    Acidity: float

model_quality = joblib.load('./model_fruit_quality.pkl')

@app.post("/classify")
def predict(data: request_body):
    input_features = [[data.Size, data.Weight, data.Sweetness, data.Crunchiness, data.Juiciness, data.Ripeness, data.Acidity]]

    y_pred = model_quality.predict(input_features)[0].astype(int)
    y_prob = model_quality.predict_proba(input_features)[0].astype(float)

    response = 'Boa' if y_pred == 1 else 'Ruim'
    probability = y_prob[y_pred]

    return {"qualidade": response, 'probabilidade': probability}
