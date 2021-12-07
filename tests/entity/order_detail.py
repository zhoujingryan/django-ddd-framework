from django_ddd_framework.domain import fields, Entity
from ..mapper.order_detail import OrderDetailMapper


class OrderDetail(Entity):
    id = fields.IntegerField()
    commodity = fields.EntityField()
    order = fields.EntityField()

    class Meta:
        mapper = OrderDetailMapper
