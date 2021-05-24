from stock_algorithms.stock_algorithm import StockAlgorithm


class StockSupply:
    def __init__(self, model):
        self.model = model

    def supply_stock(self, quantity, stock_pk):
        stock = self.model.objects.get(id=stock_pk)
        stock.quantity = StockAlgorithm.supply_stock_new(stock.quantity, quantity)
        stock.save()

    def return_stock(self, quantity, stock_pk):
        stock = self.model.objects.get(id=stock_pk)
        stock.quantity = StockAlgorithm.return_stock(stock.quantity, quantity)
        stock.save()

    def update_supply_stock(self, current_quantity, old_quantity, stock_pk):
        stock = self.model.objects.get(id=stock_pk)
        stock.quantity = StockAlgorithm.supply_stock_old(
            stock.quantity,
            current_quantity,
            old_quantity
        )
        stock.save()
