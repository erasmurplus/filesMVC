# Controller - İş mantığını yöneten sınıf

from models.model import DataModel
from views.view import display_data

class MainController:
    def __init__(self):
        self.model = DataModel()

    def add_item(self, item):
        self.model.add_data(item)

    def show_items(self):
        data = self.model.get_all_data()
        display_data(data)
