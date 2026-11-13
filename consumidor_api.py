
import requests


def obter_dados_meteorologicos():

    # Endereço da API
    url = "http://127.0.0.1:8000/v1/forecast"

    # Coordenadas de Jaraguá do Sul
    parametros = {
        "latitude": -26.4851,
        "longitude": -49.0713
    }

    # Faz a requisição GET
    resposta = requests.get(url, params=parametros, timeout=10)

    # Verifica se ocorreu algum erro
    resposta.raise_for_status()

    # Converte a resposta para JSON
    dados = resposta.json()

    # Pega as informações meteorológicas atuais
    atual = dados["current"]

    # Organiza as informações
    return {
        "temperatura": atual["temperature_2m"],
        "umidade": atual["relative_humidity_2m"],
        "sensacao": atual["apparent_temperature"],
        "precipitacao": atual["precipitation"],
        "vento": atual["wind_speed_10m"],
        "horario": atual["time"]
    }
