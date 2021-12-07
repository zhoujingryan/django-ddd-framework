# import copy
# from django.test import TestCase
# from django_ddd_framework.factory import GenericFactory
# from django_ddd_framework.repository import GenericRepository
# from django_ddd_framework.exceptions import DataIntegrityError, DataAccessError
# from ..entity import Order
# from tests.ddd.models import (
#     OrderModel,
#     CommodityModel,
#     OrderDetailModel,
# )
#
#
# args = {
#     "id": 100,
#     "code": "123",
#     "order_details": [
#         {
#             "id": 1,
#             "order_id": 100,
#             "commodity": {
#                 "id": 1,
#                 "name": "phone",
#                 "sales_price": "1000",
#             },
#         },
#         {
#             "id": 2,
#             "order_id": 100,
#             "commodity": {
#                 "id": 20,
#                 "name": "book",
#                 "sales_price": 20,
#             },
#         },
#     ],
# }
#
#
# class GenericRepositoryCreateTestCase(TestCase):
#     def setUp(self) -> None:
#         self.order = GenericFactory(Order).load(**args)
#
#     def test_create_order_entity_success(self):
#         o = GenericRepository(Order).create(self.order)
#         # assert isinstance(o, Order)
#         assert OrderModel.objects.get(id=100).code == "123"
#         assert OrderModel.objects.count() == 1
#         assert CommodityModel.objects.count() == 0
#         assert OrderDetailModel.objects.count() == 2
#
#     def test_create_duplicate_entity_raise_error(self):
#         GenericRepository(Order).create(self.order)
#         with self.assertRaises(DataIntegrityError):
#             GenericRepository(Order).create(self.order)
#         assert OrderModel.objects.get(id=100).code == "123"
#         assert OrderModel.objects.count() == 1
#         assert CommodityModel.objects.count() == 0
#         assert OrderDetailModel.objects.count() == 2
#
#     def test_create_entity_without_pk_success(self):
#         GenericRepository(Order).create(self.order)
#         o = copy.deepcopy(self.order)
#         o.id = None
#         for od in o.order_details:
#             od.id = None
#         GenericRepository(Order).create(o)
#         new_order = OrderModel.objects.exclude(id=100).first()
#         assert new_order.code == "123"
#         assert OrderModel.objects.count() == 2
#         assert CommodityModel.objects.count() == 0
#         assert OrderDetailModel.objects.count() == 4
#         # assert OrderDetailModel.objects.filter(order_id=new_order.id).count() == 2
#
#
# class GenericRepositoryUpdateTestCase(TestCase):
#     def setUp(self) -> None:
#         self.order = GenericFactory(Order).load(**args)
#
#     def test_update_entity_without_pk_failed(self):
#         o = copy.deepcopy(self.order)
#         o.id = None
#         for od in o.order_details:
#             od.id = None
#         # with self.assertRaises(DataAccessError):
#         #     GenericRepository(Order).update(o)
#         assert OrderModel.objects.count() == 0
#         GenericRepository(Order).update(o)
#         assert OrderModel.objects.count() == 0
