from product_models.product_classes.objects.object_base import SetObjectPk, SetObjectCondition
from product_models.product_classes.stock_managements.stock_outlet import StockOutlet


class StockOutletCondition(SetObjectPk, SetObjectCondition):
    stock_outlet = None

    def __init__(self, model):
        self.stock_outlet = StockOutlet(model)

    def outlet_stock(self, current_quantity):
        if self.current_condition:
            self.stock_outlet.outlet_stock(current_quantity, self.current_pk)

    def _update_stock_same_pk(self, current_quantity, last_quantity):
        if self.current_condition:
            if self.last_condition:
                self.stock_outlet.update_outlet_stock(
                    current_quantity, last_quantity,
                    self.current_pk
                )
            else:
                self.stock_outlet.outlet_stock(current_quantity, self.current_pk)
        else:
            if self.last_condition:
                self.stock_outlet.refund_stock(last_quantity, self.last_pk)

    def _update_stock_different_pk(self, current_quantity, last_quantity):
        # return old stock
        if self.current_condition:
            if self.last_condition:
                self.stock_outlet.refund_stock(last_quantity, self.last_pk)
                # add new stock
                self.stock_outlet.outlet_stock(current_quantity, self.current_pk)
            else:
                self.stock_outlet.outlet_stock(current_quantity, self.current_pk)
        else:
            if self.last_condition:
                self.stock_outlet.refund_stock(last_quantity, self.last_pk)

    def update_stock(self, current_quantity, last_quantity):
        if self.current_pk == self.last_pk:
            self._update_stock_same_pk(current_quantity, last_quantity)
        else:
            self._update_stock_different_pk(current_quantity, last_quantity)

    """ need set last value first and return stock later """

    def refund_stock(self, last_quantity):
        if self.last_condition:
            self.stock_outlet.refund_stock(last_quantity, self.last_pk)
