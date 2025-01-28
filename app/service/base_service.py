class BaseService:
    def __init__(self, model):
        self.model = model

    def get(self, id):
        return self.model.get(id)

    def create(self, data):
        return self.model.create(data)

    def update(self, id, data):
        return self.model.update(id, data)

    def delete(self, id):
        return self.model.delete(id)

    def list(self):
        return self.model.list()
