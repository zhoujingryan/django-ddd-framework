class Field:
    def __init__(self):
        pass

    def to_representation(self, value):
        raise NotImplementedError

    def to_internal_value(self, value):
        raise NotImplementedError


class IntegerField(Field):
    def to_internal_value(self, value):
        return int(value)

    def to_representation(self, value):
        return int(value)


class CharField(Field):
    def to_internal_value(self, value):
        return str(value)

    def to_representation(self, value):
        return str(value)


class EntityField(Field):
    def __init__(self, many=False):
        self.many = many
        super(EntityField, self).__init__()
