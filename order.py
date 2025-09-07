class Order:
    def __init__(self,order_id,amount):
        self.order_id = order_id
        self.amount = amount
        self.status = "created"

    def process_payment(self,payment_processor):
        if payment_processor.process_payment(self.amount):
            self.status = "paid"
            return True
        return False

