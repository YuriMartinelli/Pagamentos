from fastapi import APIRouter
from app.controllers.usuarios_controller import UsuarioController
from app.typings.usuariosTypes import UsuarioModel

USUARIOS_ROUTER = APIRouter(prefix="/usuarios")

USUARIO_CONTROLLER = UsuarioController()


@USUARIOS_ROUTER.post("/criar")
def criar_usuarios(data):
    return USUARIO_CONTROLLER.create(data)
