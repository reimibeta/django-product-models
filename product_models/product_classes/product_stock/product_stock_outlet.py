from product_models.product_classes.stock_managements.stock_outlet_condition import StockOutletCondition
from product_models.product_stocks.models import ProductStock


class ProductStockOutlet:
    product_stock_outlet = None

    def __init__(self):
        self.product_stock_outlet = StockOutletCondition(model=ProductStock)

    def new_outlet(self, current_instance):
        self.product_stock_outlet.set_current_condition(current_instance.is_transferred)
        self.product_stock_outlet.set_current_pk(current_instance.stock.id)
        self.product_stock_outlet.outlet_stock(current_instance.quantity)

    def update_outlet(self, current_instance, last_instance):
        self.product_stock_outlet.set_current_condition(current_instance.is_transferred)
        self.product_stock_outlet.set_last_condition(last_instance.is_transferred)
        self.product_stock_outlet.set_current_pk(current_instance.stock.id)
        self.product_stock_outlet.set_last_pk(last_instance.stock.id)
        self.product_stock_outlet.update_stock(current_instance.quantity, last_instance.quantity)

    def refund_outlet(self, last_instance):
        self.product_stock_outlet.set_last_condition(last_instance.is_transferred)
        self.product_stock_outlet.set_last_pk(last_instance.stock.id)
        self.product_stock_outlet.refund_stock(last_instance.quantity)


product_stock_outlet = ProductStockOutlet()
