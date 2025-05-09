import requests

def obter_dados_clima(cidade, api_key):
    """
    Consulta a API do OpenWeatherMap com base na cidade informada.
    Retorna os dados em JSON ou None se houver erro.
    """
    url = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={api_key}&lang=pt_br&units=metric"
    resposta = requests.get(url)

    if resposta.status_code == 200:
        return resposta.json()
    else:
        print("Erro ao buscar dados. Verifique o nome da cidade ou a chave da API.")
        return None

def exibir_dados(dados):
    """
    Exibe de forma legível os principais dados retornados pela API.
    """
    nome = dados["name"]
    clima = dados["weather"][0]["description"]
    temperatura = dados["main"]["temp"]
    sensacao = dados["main"]["feels_like"]
    umidade = dados["main"]["humidity"]

    print(f"\nCidade: {nome}")
    print(f"Clima: {clima.capitalize()}")
    print(f"Temperatura: {temperatura}°C")
    print(f"Sensação térmica: {sensacao}°C")
    print(f"Umidade: {umidade}%\n")

def main():
    """
    Função principal que executa a lógica do programa.
    """
    api_key = "SUA API AQUI !" # Substitua pela sua chave do OpenWeather
    cidade = input("Digite o nome da cidade: ")

    dados = obter_dados_clima(cidade, api_key)
    if dados:
        exibir_dados(dados)

if __name__ == "__main__":
    main()
