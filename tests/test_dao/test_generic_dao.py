from django.test import TestCase
from ..entity import OrderDetail, Commodity, Order
from django_ddd_framework.dao import GenericDao
from ..ddd.models import OrderDetailModel


class GenericDaoTestCase(TestCase):

    def test_generic_dao_insert_an_entity_success(self):
        od = OrderDetail(id=1, order=Order(id=1), commodity=Commodity(id=1))
        GenericDao.create(od)
        assert OrderDetailModel.objects.count() == 1
        instance = OrderDetailModel.objects.get(id="1")
        assert instance.order_id == "1"
        assert instance.commodity_id == "1"

    def test_generic_dao_update_an_entity_success(self):
        OrderDetailModel.objects.create(id="1", order_id='1', commodity_id="1")
        od = OrderDetail(id=1, order=Order(id=2), commodity=Commodity(id=3))
        GenericDao.update(od)
        assert OrderDetailModel.objects.count() == 1
        instance = OrderDetailModel.objects.get(id="1")
        assert instance.order_id == "2"
        assert instance.commodity_id == "3"

    def test_generic_dao_delete_an_entity_success(self):
        OrderDetailModel.objects.create(id="1", order_id='1', commodity_id="1")
        od = OrderDetail(id=1, order=Order(id=2), commodity=Commodity(id=3))
        GenericDao.delete(od)
        assert OrderDetailModel.objects.count() == 0

    def test_generic_dao_bulk_create_entity_success(self):
        assert OrderDetailModel.objects.count() == 0
        od1 = OrderDetail(id=1, order=Order(id=1), commodity=Commodity(id=1))
        od2 = OrderDetail(id=2, order=Order(id=2), commodity=Commodity(id=3))
        od3 = OrderDetail(id=3, order=Order(id=3), commodity=Commodity(id=3))
        l = [od1, od2, od3]
        GenericDao.bulk_create(l)
        assert OrderDetailModel.objects.count() == 3
        od = OrderDetailModel.objects.get(id='1')
        assert od.order_id == '1'
        assert od.commodity_id == '1'
        od = OrderDetailModel.objects.get(id='2')
        assert od.order_id == '2'
        assert od.commodity_id == '3'
        od = OrderDetailModel.objects.get(id='3')
        assert od.order_id == '3'
        assert od.commodity_id == '3'

    def test_generic_dao_bulk_update_entity_success(self):
        OrderDetailModel.objects.create(id="1", order_id='1', commodity_id="1")
        OrderDetailModel.objects.create(id="2", order_id='2', commodity_id="3")
        OrderDetailModel.objects.create(id="3", order_id='3', commodity_id="3")
        assert OrderDetailModel.objects.count() == 3
        od1 = OrderDetail(id=1, order=Order(id=4), commodity=Commodity(id=5))
        od2 = OrderDetail(id=2, order=Order(id=2), commodity=Commodity(id=5))
        od3 = OrderDetail(id=3, order=Order(id=4), commodity=Commodity(id=3))
        l = [od1, od2, od3]
        GenericDao.bulk_update(l)
        assert OrderDetailModel.objects.count() == 3
        od = OrderDetailModel.objects.get(id='1')
        assert od.order_id == '4'
        assert od.commodity_id == '5'
        od = OrderDetailModel.objects.get(id='2')
        assert od.order_id == '2'
        assert od.commodity_id == '5'
        od = OrderDetailModel.objects.get(id='3')
        assert od.order_id == '4'
        assert od.commodity_id == '3'

    def test_generic_dao_bulk_delete_entity_success(self):
        OrderDetailModel.objects.create(id="1", order_id='1', commodity_id="1")
        OrderDetailModel.objects.create(id="2", order_id='2', commodity_id="3")
        OrderDetailModel.objects.create(id="3", order_id='3', commodity_id="3")
        assert OrderDetailModel.objects.count() == 3
        od1 = OrderDetail(id=1, order=Order(id=4), commodity=Commodity(id=5))
        od2 = OrderDetail(id=2, order=Order(id=2), commodity=Commodity(id=5))
        od3 = OrderDetail(id=3, order=Order(id=4), commodity=Commodity(id=3))
        l = [od1, od2]
        GenericDao.bulk_delete(l)
        assert OrderDetailModel.objects.count() == 1
        GenericDao.bulk_delete([od3])
        assert OrderDetailModel.objects.count() == 0
