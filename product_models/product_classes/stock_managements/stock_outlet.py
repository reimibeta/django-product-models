from stock_algorithms.stock_algorithm import StockAlgorithm


class StockOutlet:
    def __init__(self, model):
        self.model = model

    # outlet stock
    def outlet_stock(self, quantity, stock_pk):
        stock = self.model.objects.get(id=stock_pk)
        stock.quantity = StockAlgorithm.outlet_stock_new(stock.quantity, quantity)
        stock.save()

    # update outlet stock
    def update_outlet_stock(self, current_quantity, old_quantity, stock_pk):
        stock = self.model.objects.get(id=stock_pk)
        stock.quantity = StockAlgorithm.outlet_stock_old(
            stock.quantity,
            current_quantity,
            old_quantity
        )
        stock.save()

    # refund stock
    def refund_stock(self, quantity, stock_pk):
        stock = self.model.objects.get(id=stock_pk)
        stock.quantity = StockAlgorithm.refund_stock(stock.quantity, quantity)
        stock.save()
