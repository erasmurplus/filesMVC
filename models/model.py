# Model - Veri işlemlerini yöneten sınıf

class DataModel:
    def __init__(self):
        self.data = []

    def add_data(self, item):
        self.data.append(item)

    def get_all_data(self):
        return self.data
