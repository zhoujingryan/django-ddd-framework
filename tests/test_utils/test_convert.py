# from django.test import TestCase
# from django_ddd_framework.factory import GenericFactory
# from ..entity import Order, Commodity, OrderDetail
# from django_ddd_framework.utils import entity_to_dict, entity_to_dao, aggregate_to_dao
#
#
# class ConvertTestCase(TestCase):
#     def setUp(self) -> None:
#         args = {
#             "id": 100,
#             "code": "123",
#             "order_details": [
#                 {
#                     "id": 1,
#                     "order_id": 100,
#                     "commodity": {
#                         "id": 1,
#                         "name": "phone",
#                         "sales_price": "1000",
#                     },
#                 },
#                 {
#                     "id": 2,
#                     "order_id": 100,
#                     "commodity": {
#                         "id": 20,
#                         "name": "book",
#                         "sales_price": 20,
#                     },
#                 },
#             ],
#         }
#         self.order = GenericFactory(Order).load(**args)
#
#     def test_entity_to_dict_success(self):
#         d = entity_to_dict(self.order)
#         assert d["id"] == 100
#         assert d["code"] == "123"
#         assert len(d["order_details"]) == 2
#         assert d["order_details"][0]["commodity"]["name"] == "phone"
#         assert d["order_details"][0]["commodity"]["sales_price"] == 1000
#
#     def test_entity_to_dao_success(self):
#         res = entity_to_dao([self.order])
#         assert len(res) == 3
#         assert Order in res
#         assert OrderDetail in res
#         assert Commodity in res
#         c = [e for e in res[Commodity] if e["id"] == 1][0]
#         assert c["price"] == 1000
#
#     def test_aggregate_to_dao_success(self):
#         res = aggregate_to_dao([self.order])
#         assert len(res) == 2
#         assert Order in res
#         assert OrderDetail in res
