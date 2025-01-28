class BaseController:
    def __init__(self, service):
        self.service = service

    def create(self, data):
        return self.service.create(data)

    def read(self, id):
        return self.service.read(id)

    def update(self, id, data):
        return self.service.update(id, data)

    def delete(self, id):
        return self.service.delete(id)
