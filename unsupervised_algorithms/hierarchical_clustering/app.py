import streamlit as st
import pandas as pd

# Carregar o csv e colocar no cache do streamlit
@st.cache_data
def load_data():
    return pd.read_csv('./dataset/clusterizacao_laptops.csv')

df = load_data()

# Sidebar para os filtros
st.sidebar.header("Filtros")

# Selecionar os modelos
model = st.sidebar.selectbox("Selecionar Modelo", df['model'].unique())

# Filtrar modelo
df_laptops_model = df[df['model'] == model]

# Filtrar cluster do modelo escolhido
df_laptops_final = df[df['cluster'] == df_laptops_model.iloc[0]['cluster']]

# Visualizar os modelos
st.write("Recomendação de Modelos")
st.table(df_laptops_final)
