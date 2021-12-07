from django.test import TestCase
from ..entity import OrderDetail, Commodity, Order
from django_ddd_framework.dao.entity_dao import EntityDAO


class EntityDaoTestCase(TestCase):
    def test_entity_dao_fields(self):
        od = OrderDetail(id="1", order=Order(id="1"), commodity=Commodity(id="1"))
        dao = EntityDAO(OrderDetail).create(od)
        assert isinstance(dao, EntityDAO)
        assert dao.id == "1"
        assert dao.order_id == "1"
        assert dao.commodity_id == "1"
