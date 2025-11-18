from fastapi import FastAPI, HTTPException
from datetime import datetime, timedelta
import jwt

app = FastAPI()

SECRET_KEY = "chave_super_segura"  # chave secreta usada no token

# Função para gerar token JWT válido por 30 minutos
def gerar_token():
    payload = {"exp": datetime.utcnow() + timedelta(minutes=30), "user": "api_cliente"}
    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")

@app.get("/token")
def obter_token():
    token = gerar_token()
    return {"token": token}

@app.get("/usuarios")
def listar_usuarios(token: str):
    try:
        jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expirado")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=403, detail="Token inválido")

    # Dados fictícios simulando um banco de dados
    return {
        "usuarios": [
            {"id": 1, "nome": "João"},
            {"id": 2, "nome": "Maria"},
            {"id": 3, "nome": "Leonardo"},
        ]
    }