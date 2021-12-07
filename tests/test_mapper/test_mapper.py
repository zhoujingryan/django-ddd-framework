from django.test import TestCase
from django_ddd_framework.mapper import MetaDataMapper, Property, Ref
from django_ddd_framework.types import MapType


class MapperTestCase(TestCase):
    pass
    # def test_mapper_class_properties_with_other_type_error(self):
    #     with self.assertRaises(ValueError):
    #
    #         class TestMetaDataMapping(MetaDataMapping):  # noqa
    #             class Meta:
    #                 dao_mapper = {MapType.GENERIC: "ddd"}
    #
    #             properties = [
    #                 Ref(name="a"),
    #             ]
    #
    # def test_mapper_class_joins_with_other_type_error(self):
    #     with self.assertRaises(ValueError):
    #
    #         class TestMetaDataMapping(MetaDataMapping):  # noqa
    #             class Meta:
    #                 dao_mapper = {MapType.GENERIC: "ddd"}
    #
    #             properties = [
    #                 Property(name="a", column="a", primary_key=True),
    #             ]
    #             joins = [
    #                 Property(name="a", column="a"),
    #             ]
    #
    # def test_mapper_class_refs_with_other_type_error(self):
    #     with self.assertRaises(ValueError):
    #
    #         class TestMetaDataMapping(MetaDataMapping):  # noqa
    #             class Meta:
    #                 dao_mapper = {MapType.GENERIC: "ddd"}
    #
    #             properties = [
    #                 Property(name="a", column="a", primary_key=True),
    #             ]
    #             refs = [
    #                 Property(name="a", column="a"),
    #             ]
    #
    # def test_mapper_read_only_fields(self):
    #     class TestMetaDataMapping(MetaDataMapping):
    #         class Meta:
    #             dao_mapper = {MapType.GENERIC: "ddd"}
    #
    #         properties = [
    #             Property(name="a", column="a", primary_key=True),
    #             Property(name="b", column="b", read_only=True),
    #         ]
    #
    #     ro = TestMetaDataMapping.get_read_only_fields()
    #     assert len(ro) == 1 and ro[0] == "b"
