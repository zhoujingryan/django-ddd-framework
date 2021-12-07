from django.test import TestCase
from ..entity import Commodity, Order, OrderDetail
from django_ddd_framework.factory import Factory
from django_ddd_framework.dao.entity_dao import EntityDAO
from django_ddd_framework.domain import Entity


class FactoryTestCase(TestCase):

    def test_factory_rebuild_from_dao_success(self):
        od = OrderDetail(id="1", order=Order(id="1"), commodity=Commodity(id="1"))
        dao = EntityDAO(OrderDetail).create(od)
        assert dao.id == "1"
        assert dao.order_id == "1"
        assert dao.commodity_id == "1"
        l = Factory(entity_cls=OrderDetail).rebuild([dao])
        entity = l[0]
        assert isinstance(entity, Entity)
        assert entity.id == '1'
        assert entity.order_id == '1'
        assert entity.commodity_id == '1'

    # def test_factory_get_entity_aggregates(self):
    #     od = OrderDetail(id=1, order=Order(id=1), commodity=Commodity(id=1))
    #     f = od.factory
    #     assert isinstance(f, Factory)
    #     aggrs = f.aggregates
    #     assert len(aggrs) == 1
    #     assert od == aggrs[0]
    #
    #     order = Order(
    #         id=1,
    #         order_details=[
    #             OrderDetail(id=1, commodity=Commodity(id=1), order=Order(id=1)),
    #             OrderDetail(id=2, commodity=Commodity(id=1), order=Order(id=1)),
    #             OrderDetail(id=2, commodity=Commodity(id=1), order=Order(id=1)),
    #         ],
    #     )
    #     f = order.factory
    #     aggrs = f.aggregates
    #     assert len(aggrs) == 4
    #     assert all([isinstance(e, OrderDetail) for e in aggrs[1:]])


#     def test_load_entity_success(self):
#         args = {
#             "name": "phone",
#             "sales_price": "1000",
#         }
#         c = GenericFactory(Commodity).load(**args)
#         assert isinstance(c, Commodity)
#         assert c.id is None
#         assert c.name == "phone"
#         assert c.sales_price == 1000
#
#     def test_load_entity_one_to_one_join_success(self):
#         args = {
#             "id": "1",
#             "commodity": {"id": 1, "name": "phone", "sales_price": "1000"},
#         }
#         od = GenericFactory(OrderDetail).load(**args)
#         assert isinstance(od, OrderDetail)
#         assert od.id == 1
#         c = od.commodity
#         assert isinstance(c, Commodity)
#         assert c.id == 1
#         assert c.name == "phone"
#         assert c.sales_price == 1000
#
#     def test_load_entity_one_to_many_join_success(self):
#         args = {
#             "id": 1,
#             "code": "123",
#             "order_details": [
#                 {
#                     "id": 1,
#                     "commodity": {
#                         "id": 1,
#                         "name": "phone",
#                         "sales_price": 1000,
#                     },
#                 },
#                 {
#                     "id": 2,
#                     "commodity": {
#                         "id": 20,
#                         "name": "book",
#                         "sales_price": 20,
#                     },
#                 },
#             ],
#         }
#         o = GenericFactory(Order).load(**args)
#         assert isinstance(o, Order)
#         ods = o.order_details
#         assert isinstance(ods, list) and len(ods) == 2
#         assert isinstance(ods[0], OrderDetail)
#         od2 = ods[1]
#         assert od2.id == 2
#         assert isinstance(od2.commodity, Commodity)
#         assert od2.commodity.id == 20
#
#     def test_load_entity_on_to_many_joins_wrong_data_raise_error(self):
#         args = {
#             "id": 1,
#             "code": "123",
#             "order_details": "123",
#         }
#         with self.assertRaises(ValueError):
#             GenericFactory(Order).load(**args)
