from typings import ServicesType


class BaseController:
    def __init__(self, service: ServicesType):
        self.service = service

    def create(self, data):
        try:
            return self.service.create(data)
        except TimeoutError as e:
            return {"error": "Erro ao criar usuário", "message": str(e)}
        except Exception as e:
            return {"error": "Erro ao criar usuário", "message": str(e)}

    def read(self, id):
        try:
            return self.service.read(id)
        except TimeoutError as e:
            return {"error": "Erro ao criar usuário", "message": str(e)}
        except Exception as e:
            return {"error": "Erro ao criar usuário", "message": str(e)}

    def update(self, id, data):
        try:
            return self.service.update(id, data)
        except TimeoutError as e:
            return {"error": "Erro ao criar usuário", "message": str(e)}
        except Exception as e:
            return {"error": "Erro ao criar usuário", "message": str(e)}

    def delete(self, id):
        try:
            return self.service.delete(id)
        except TimeoutError as e:
            return {"error": "Erro ao criar usuário", "message": str(e)}
        except Exception as e:
            return {"error": "Erro ao criar usuário", "message": str(e)}
