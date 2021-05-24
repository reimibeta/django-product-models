from product_models.product_classes.stock_managements.stock_supply_condition import StockSupplyCondition
from product_models.product_stocks.models import ProductStock


class ProductStockSupply:
    product_stock_supply = None

    def __init__(self):
        self.product_stock_supply = StockSupplyCondition(ProductStock)

    def supply_stock(self, current_instance):
        self.product_stock_supply.set_current_condition(current_instance.is_transferred)
        self.product_stock_supply.set_current_pk(current_instance.stock.id)
        self.product_stock_supply.supply_stock(current_instance.quantity)

    def update_stock(self, current_instance, last_instance):
        self.product_stock_supply.set_current_condition(current_instance.is_transferred)
        self.product_stock_supply.set_last_condition(last_instance.is_transferred)
        self.product_stock_supply.set_current_pk(current_instance.stock.id)
        self.product_stock_supply.set_last_pk(last_instance.stock.id)
        self.product_stock_supply.update_stock(current_instance.quantity, last_instance.quantity)

    def return_stock(self, last_instance):
        self.product_stock_supply.set_last_condition(last_instance.is_transferred)
        self.product_stock_supply.set_last_pk(last_instance.stock.id)
        self.product_stock_supply.return_stock(last_instance.quantity)


product_stock_supply = ProductStockSupply()
