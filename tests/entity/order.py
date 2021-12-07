from django_ddd_framework.domain import fields, Entity
from ..mapper.order import OrderMapper


class Order(Entity):
    id = fields.IntegerField()
    code = fields.CharField()
    order_details = fields.EntityField(many=True)
    customer_id = fields.CharField()

    class Meta:
        mapper = OrderMapper
