from django_ddd_framework.mapper import MetaDataMapper, Property, Join


class OrderMapper(MetaDataMapper):
    class DBNotation:
        generic = "ddd.OrderModel"

    entity = "Order"

    properties = [
        Property(name="id", column="id", primary_key=True),
        Property(name="code", column="code"),
    ]
    joins = [
        Join(
            name="order_details",
            join_class="tests.entity.order_detail.OrderDetail",
            join_key="order_id",
            join_type=Join.JoinType.OneToMany,
            is_aggregation=True,
        ),
        # Join(
        #     name="customer",
        #     join_class="tests.entity.user.User",
        #     join_key="customer_id",
        #     join_type=Join.JoinType.ManyToOne,
        # ),
    ]
