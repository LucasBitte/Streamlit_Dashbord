import streamlit as st
import requests
import pandas as pd
import plotly.express as px


def formata_numero(valor,prefixo = ''):
    for unidade in ['','K']:
        if valor < 1000 :
            return f'{prefixo}{valor:.2f} {unidade}'
        valor/= 1000
    return f'{prefixo} {valor:.2f} M'

st.title('DASHBOARD DE VENDAS :shopping_trolley:')

url = 'https://labdados.com/produtos'
response = requests.get(url)
dados = pd.DataFrame.from_dict(response.json())

##Tabelas
git add .


## Visualização 
coluna1, coluna2 = st.columns(2)
with coluna1 :
    st.metric('Receita', formata_numero(dados['Preço'].sum(), 'R$'))

with coluna2 :
    st.metric('Qtd de vendas', formata_numero(dados.shape[0]))

st.dataframe(dados)

