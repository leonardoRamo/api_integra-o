
import requests

app = FastAPI()

API_PROVIDER_URL = "http://127.0.0.1:8000"  # endereço da API principal

@app.get("/integracao")
from fastapi import FastAPI
import requests

app = FastAPI()

API_PROVIDER_URL = "http://127.0.0.1:8000"  # endereço da API principal


@app.get("/integracao")
def integrar():
    # Obtém token da API principal
    token_response = requests.get(f"{API_PROVIDER_URL}/token")
    token = token_response.json().get("token")

    # Faz a requisição de usuários com o token
    usuarios_response = requests.get(f"{API_PROVIDER_URL}/usuarios", params={"token": token})

    if usuarios_response.status_code == 200:
        return {"mensagem": "Integração bem-sucedida!", "dados": usuarios_response.json()}
    else:
        return {"erro": "Falha na integração", "detalhes": usuarios_response.text}