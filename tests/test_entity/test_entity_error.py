from django.test import TestCase
from django_ddd_framework.domain import Entity


class EntityErrorTestCase(TestCase):
    def test_create_duplicate_entity_class_error(self):
        pass
        # with self.assertRaises(ValueError):
        #     class CommodityMapper:
        #         pass
        #
        #     class Commodity(Entity):  # noqa
        #         class Meta:
        #             mapper_class = CommodityMapper

    # def test_create_concrete_entity_class_without_mapper_error(self):
    #     with self.assertRaises(TypeError):
    #
    #         class User(Entity):  # noqa
    #             class Meta:
    #                 mapper_class = None
