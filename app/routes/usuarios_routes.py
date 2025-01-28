from fastapi import APIRouter

from app.controllers.usuarios_controller import UsuarioController
from app.typings.usuariosTypes import UsuarioModel

usuarios_router = APIRouter(prefix="/usuarios")

USUARIO_CONTROLLER = UsuarioController()


@usuarios_router.post("/criar")
def criar_usuarios(data: UsuarioModel):
    return USUARIO_CONTROLLER.create(data)
