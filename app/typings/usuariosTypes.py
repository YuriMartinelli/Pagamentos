from datetime import datetime


class UsuarioModel:
    nome: str
    cpf: str
    email: str
    senha: str
    id: int = 0
    nascimento: datetime
    criado_em: datetime
