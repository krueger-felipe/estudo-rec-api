
import streamlit as st

from consumidor_api import obter_dados_meteorologicos


# Configuração da página
st.set_page_config(
    page_title="Monitoramento Meteorológico",
    page_icon="🌤️",
    layout="wide"
)

# Título
st.title("Monitoramento Meteorológico")

st.caption("Jaraguá do Sul - SC")

# Busca os dados da API
try:

    dados = obter_dados_meteorologicos()

    st.subheader("Condições atuais")

    # Primeira linha de indicadores
    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Temperatura",
        f'{dados["temperatura"]} °C'
    )

    col2.metric(
        "Umidade",
        f'{dados["umidade"]} %'
    )

    col3.metric(
        "Sensação térmica",
        f'{dados["sensacao"]} °C'
    )

    # Segunda linha de indicadores
    col4, col5, col6 = st.columns(3)

    col4.metric(
        "Precipitação",
        f'{dados["precipitacao"]} mm'
    )

    col5.metric(
        "Velocidade do vento",
        f'{dados["vento"]} km/h'
    )

    col6.metric(
        "Horário",
        dados["horario"]
    )

    st.success("Dados carregados com sucesso!")

except Exception as erro:

    st.error(f"Erro ao consultar a API: {erro}")
    st.write("Verifique se a API está em funcionamento.")
