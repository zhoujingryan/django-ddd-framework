from .base import Field


class Ref(Field):
    def __init__(self, *, name: str):
        super(Ref, self).__init__(name)
