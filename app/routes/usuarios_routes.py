from fastapi import APIRouter

usuarios_router = APIRouter(prefix="/usuarios")


@usuarios_router.post("/criar")
def criar_usuarios():
    return {"mensagem": "Usuário criado com sucesso!"}
