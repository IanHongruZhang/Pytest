class Inventory:
    def __init__(self):
        self.stock = {'item_1': 10}

    def update_stock(self, item_id, quantity):
        if self.stock[item_id] >= quantity:
            self.stock[item_id] -= quantity
            return True
        return False