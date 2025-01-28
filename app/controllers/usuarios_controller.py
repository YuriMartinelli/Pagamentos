from app.controllers.base_controller import BaseController
from app.service.usuarios_service import UsuarioService


class UsuarioController(BaseController):
    def __init__(self) -> None:
        super().__init__(UsuarioService)
