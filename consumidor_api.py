import requests


#Função que obtem dados da previsão
def obter_previsao():

    #endpoint
    url = "http://127.0.0.1:8000/v1/forecast"

    #parametros para consulta
    parametros = {
        "latitude": -26.4851,
        "longitude": -49.0713,
    }

    
    # realiza a requisição HTTP
    resposta = requests.get(
    url, 
    params=parametros, #envia os parâmetros de consulta
    timeout = 15 #estabelece um limite de espera pela resposta
    )

    #verifica se a resposta HTTP indica uma falha 
    resposta.raise_for_status()

    #converte o conteúdo recebido para uma estrutura de dados Python
    dados = resposta.json()

    #condições
    condicoes = dados["current"]

    temperature = condicoes["temperature_2m"]
    umidade = condicoes["relative_humidity_2m"]
    sensacao_termica = condicoes["apparent_temperature"]
    precipitacao = condicoes["precipitation"]
    vel_vento = condicoes["wind_speed_10m"]
   

    return{
        "Temperatura" : temperature,
        "Umidade" : umidade,
        "Sensação_Térmica" : sensacao_termica,
        "Precipitação" : precipitacao,
        "Velocidade_Vento" : vel_vento
    }
    

#teste de consumidor
if __name__ == "__main__":

    resultado = obter_previsao()

    print("PREVISÃO METEOROLÓGICA")
    print(f"Temperatura: {resultado['Temperatura']}°C")
    print(f"Umidade: {resultado['Umidade']}%")
    print(f"Sensação Térmica: {resultado['Sensação_Térmica']}°C")
    print(f"Precipitação: {resultado['Precipitação']}mm")
    print(f"Velocidade do Vento: {resultado['Velocidade_Vento']}km/h")
    
    