from pydantic import BaseModel
from fastapi import FastAPI

import joblib

# Criar uma instância do FastAPI
app = FastAPI()

# Criar uma classe para receber os dados de entrada
class request_body(BaseModel):
    horas_estudo: float

# Carregar o modelo
model = joblib.load('./reg_model.pkl')

# Criar uma rota para receber os dados de entrada e retornar a previsão
@app.post('/predict')
def predict(body: request_body):
    # Extrair os dados de entrada
    horas_estudo = [[body.horas_estudo]]
    
    # Fazer a previsão
    y_pred = model.predict(horas_estudo)[0].round(0).astype(int)
    
    # Retornar a previsão
    return {'predicao': y_pred.tolist()}
