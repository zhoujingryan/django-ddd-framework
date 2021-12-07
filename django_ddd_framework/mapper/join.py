from django.utils.module_loading import import_string
from .base import Field
from enum import Enum
from functools import cached_property


class Join(Field):
    class JoinType(Enum):
        OneToOne = 1
        OneToMany = 2
        ManyToOne = 3
        ManyToMany = 4

    def __init__(
        self,
        *,
        name: str,
        join_type: JoinType,
        join_key: str,
        join_class: str,
        is_reverse: bool = False,
        is_aggregation: bool = False
    ):
        self.join_type = join_type
        self.join_key = join_key
        self._join_class = join_class
        self.is_aggregation = is_aggregation
        self.is_reverse = is_reverse
        super(Join, self).__init__(name)

    def validate(self):
        if not isinstance(self.join_type, self.JoinType):
            raise TypeError(
                "wrong join type of join {}, got {}, expect one of Join.JoinType".format(
                    self.name, type(self.join_type)
                )
            )
        if self.join_type == self.JoinType.ManyToMany:
            raise ValueError("many to many type join is not allowed")
        if self.is_reverse and self.join_type != self.JoinType.OneToOne:
            raise ValueError(
                "is reversed join is only apply to oneToOne join relations"
            )
        if self.is_aggregation and self.join_type == self.JoinType.ManyToOne:
            raise ValueError("ManyToOne join type cannot be aggregation")

    @cached_property
    def join_class(self):
        return import_string(self._join_class)
