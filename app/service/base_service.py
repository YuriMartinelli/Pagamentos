class BaseService:
    def __init__(self, service):
        self.service = service

    def get(self, id):
        return self.service.get(id)

    def create(self, data):
        return self.service.create(data)

    def update(self, id, data):
        return self.service.update(id, data)

    def delete(self, id):
        return self.service.delete(id)

    def list(self):
        return self.service.list()
