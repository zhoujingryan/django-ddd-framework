from django.test import TestCase
from django_ddd_framework.mapper import Join


class JoinTestCase(TestCase):
    def test_join_type_wrong_raises(self):
        with self.assertRaises(TypeError):
            Join(
                name="commodity",
                join_class="tests.entity.Commodity",
                join_key="commodity_id",
                join_type="oneToOne",
            )
