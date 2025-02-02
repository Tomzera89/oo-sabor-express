import requests # Importando a biblioteca requests para realizar requisições HTTP
import json # Importando a biblioteca json para manipular dados JSON


url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'

response = requests.get(url)

print(response.status_code) # Mostra o código de status da resposta HTTP

if response.status_code == 200:
    dados_json = response.json()
    dados_restaurante = {}
    for item in dados_json:
        nome_restaurante = item['Company']
        if nome_restaurante not in dados_restaurante:
            dados_restaurante[nome_restaurante] = []

        dados_restaurante[nome_restaurante].append({
            "item": item['Item'],
            "price": item['price'],
            "description": item['description']
        })


else:
    print(f'Erro ao acessar a API: {response.status_code} - {response.reason}!')


for nome_restaurante, item in dados_restaurante.items():
    nome_do_arquivo = f'{nome_restaurante}.json'
    with open(nome_do_arquivo, 'w') as arquivo_restaurante:
        json.dump(item, dados_restaurante, indent=4)