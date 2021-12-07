from django_ddd_framework.mapper import MetaDataMapper, Property


class CommodityMapper(MetaDataMapper):
    class DBNotation:
        generic = "ddd.CommodityModel"

    entity = "Commodity"

    properties = [
        Property(name="id", column="id", primary_key=True),
        Property(name="name", column="name"),
        Property(name="sales_price", column="price"),
    ]
