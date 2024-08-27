import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Dicionário de faturamento
dict_faturamento = {
    'data_ref': [
        '2023-01-01', 
        '2020-02-01', 
        '2021-03-01', 
        '2022-04-01', 
        '2023-05-01',
        '2023-06-01', 
        '2020-07-01', 
        '2021-08-01', 
        '2022-09-01', 
        '2023-10-01',
        '2022-11-01', 
        '2023-12-01',
        ],
    'valor': [
        400000, 
        890000, 
        760000, 
        430000, 
        920000,
        340000, 
        800000, 
        500000, 
        200000, 
        900000,
        570000, 
        995000,
        ]
}

df_faturamento = pd.DataFrame.from_dict(dict_faturamento)

media_vendas = df_faturamento['valor'].mean()
print(f"Média: {media_vendas}")

df_faturamento['data_ref'] = pd.to_datetime(df_faturamento['data_ref'])

df_faturamento = df_faturamento.sort_values(by='data_ref')

fig, ax = plt.subplots(figsize=(12, 6))
ax.bar(df_faturamento['data_ref'], df_faturamento['valor'], color='blue', width=24)

ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))

plt.xlabel('Data de Referência')
plt.ylabel('Valor de Faturamento')
plt.title('Faturamento Mensal')

df_faturamento.plot.line(x='data_ref', y='valor')

plt.show()
