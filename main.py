from fastapi import FastAPI, Query # Importando a biblioteca FastAPI
import requests # Importando a biblioteca requests para realizar requisições HTTP

app = FastAPI()

@app.get('/api/hello')
def hello_world():
    '''
    Endpoint para retornar "Hello, World!" como resposta.

    '''
    return {'Hello': 'World!'}

@app.get('/api/restaurantes')
def get_restaurantes(restaurante: str = Query(None)):
    '''
    
    Endpoint para retornar os restaurantes com cardápio.
    
    '''
    url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
    response = requests.get(url)

    if response.status_code == 200:
        dados_json = response.json()
        if restaurante is None:
            return dados_json

        dados_restaurante = []
        for item in dados_json:
            if item['Company'] == restaurante:
                dados_restaurante.append({
                    "item": item['Item'],
                    "price": item['price'],
                    "description": item['description']
                })
        return {'Restaurante':restaurante, 'Cardápio': dados_restaurante}

    else:
        return {'Error': f'Erro ao acessar a API: {response.status_code} - {response.text}!'  }


