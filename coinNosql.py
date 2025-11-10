import requests
from tinydb import TinyDB, Query
from datetime import datetime

db = TinyDB('bitcoin_data.json')

def extrair():
    
    url = "https://api.coinbase.com/v2/prices/spot"
    response = requests.get(url)
    return response.json()

def tranformar(dados_json):
    
    valor = dados_json['data'],['amount']
    criptomoeda = dados_json['data']['base']
    moeda = dados_json['data']['currency']
    
    dados_tratados = {"valor": valor, "cripto": criptomoeda, "moeda": moeda, "data_hora": datetime.now().isoformat()}
    
    return dados_tratados


def load(dados_tratados):
    db.insert(dados_tratados)
    print("Dados inseridos no TinyDB com sucesso.")
    
    
if __name__ == "__main__":
    dados_json = extrair()
    dados_tratados = tranformar(dados_json)
    load(dados_tratados)
    