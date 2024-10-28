import streamlit as st
import json
import requests

# Title
st.title('Predição de Salário')

# Inputs do usuário
st.write('Quantos meses o profissional está na empresa?')
tempo_na_empresa = st.slider("Meses", min_value=0, max_value=120, step=1, value=60)

st.write('Qual o nível do profissional na empresa?')
nivel_na_empresa = st.slider("Nível", min_value=1, max_value=10, step=1, value=5)

input_features = {
    'tempo_na_empresa': tempo_na_empresa,
    'nivel_na_empresa': nivel_na_empresa,
}

# Criar um botão para realizar a predição
if st.button('Estimar salário'):
    # Realizar a requisição POST para a API
    response = requests.post('http://127.0.0.1:8000/predict', data=json.dumps(input_features))
    
    # Verificar o status da resposta
    if response.status_code == 200:
        # Converter a resposta para JSON
        res_json = json.loads(response.text)
        salary_prediction = res_json['salario_em_reais']
        
        # Exibir a predição
        st.subheader('O sálario estimado é de R$ {:.2f}'.format(salary_prediction))
    else:
        # Exibir mensagem de erro
        st.error('Erro ao realizar a predição')
