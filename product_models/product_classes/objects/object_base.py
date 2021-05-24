class ObjectCondition:
    def __init__(self, condition):
        self.condition = condition

    @property
    def condition(self):
        return self._condition

    @condition.setter
    def condition(self, value):
        self._condition = value


class SetObjectCondition:
    """"""
    current_condition = None
    """"""
    last_condition = None

    # current condition
    def set_current_condition(self, current_condition):
        obj = ObjectCondition(current_condition)
        self.current_condition = obj.condition

    # last condition
    def set_last_condition(self, last_condition):
        obj = ObjectCondition(last_condition)
        self.last_condition = obj.condition


class ObjectPk:
    def __init__(self, pk):
        self.pk = pk

    @property
    def pk(self):
        return self._pk

    @pk.setter
    def pk(self, value):
        self._pk = value


class SetObjectPk:
    current_pk = None
    last_pk = None

    def set_current_pk(self, pk):
        obj = ObjectPk(pk)
        self.current_pk = obj.pk

    def set_last_pk(self, pk):
        obj = ObjectPk(pk)
        self.last_pk = obj.pk
