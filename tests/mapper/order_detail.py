from django_ddd_framework.mapper import MetaDataMapper, Property, Join


class OrderDetailMapper(MetaDataMapper):
    class DBNotation:
        generic = "ddd.OrderDetailModel"

    entity = "OrderDetail"

    properties = [
        Property(name="id", column="id", primary_key=True),
        # Property(name="order_id", column="order_id"),
    ]
    joins = [
        Join(
            name="commodity",
            join_class="tests.entity.commodity.Commodity",
            join_key="commodity_id",
            join_type=Join.JoinType.OneToOne,
        ),
        Join(
            name="order",
            join_class="tests.entity.order.Order",
            join_key="order_id",
            join_type=Join.JoinType.ManyToOne,
        ),
    ]
