from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
import joblib
import pandas as pd

# Criar uma instância do FastAPI
app = FastAPI()

# Criar uma classe com os dados de entrada com os campos que serão utilizados
class request_body(BaseModel):
  tempo_na_empresa: int
  nivel_na_empresa: int

# Carregar modelo para realizar a predição
modelo_poly = joblib.load('./model_salary.pkl')

# Criar uma rota para realizar a predição
@app.post('/predict')
def predict(data: request_body):
    # Criar um dicionário com os dados de entrada
    input_feature = {
        'tempo_na_empresa': [data.tempo_na_empresa],
        'nivel_na_empresa': [data.nivel_na_empresa]
    }
    
    # Criar um DataFrame com os dados de entrada
    df = pd.DataFrame(input_feature, index=[1])
    
    # Realizar a predição
    prediction = modelo_poly.predict(df)[0].astype(float).round(2)
    
    # Retornar a predição
    return {'salario_em_reais': prediction.tolist()}
