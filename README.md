# API Clima com Python

Este projeto é uma aplicação simples em Python que consulta a API do OpenWeatherMap para exibir as condições climáticas atuais de uma cidade informada pelo usuário.

## Tecnologias utilizadas

- Python 3.9+
- requests
- API do OpenWeatherMap

## Instalação

1. Clone o repositório:

git clone https://github.com/Antoniosn4/api-clima-python.git  
cd api-clima-python

2. (Opcional) Crie e ative um ambiente virtual:

python -m venv venv  
venv\Scripts\activate  (no Windows)

3. Instale as dependências:

pip install -r requirements.txt

## Como obter uma chave da API

1. Acesse o site https://openweathermap.org/api  
2. Crie uma conta gratuita  
3. Vá em API Keys no painel do usuário e gere uma chave  
4. Copie a chave e cole no campo `api_key` no arquivo `clima.py`

Exemplo:

api_key = "sua_chave_aqui"

## Como usar

1. Abra o terminal no diretório do projeto  
2. Execute o arquivo:

python clima.py

3. Digite o nome da cidade quando solicitado  
4. O terminal exibirá as informações de clima da cidade informada

