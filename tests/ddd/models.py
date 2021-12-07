from django.db import models
from .utils import current_timestamp


class ModelBase(models.Model):
    class Meta:
        abstract = True

    id = models.CharField("id", max_length=32, primary_key=True)
    create_time = models.IntegerField(
        "create_time",
        help_text="model instance created timestamp",
        default=current_timestamp,
    )


class UserModel(models.Model):
    name = models.CharField("name", max_length=32, null=True)
    username = models.CharField("username", max_length=32, db_index=True)
    password = models.CharField("password", max_length=32)


class OrderModel(models.Model):
    code = models.CharField("code", max_length=32, db_index=True)
    customer_id = models.CharField(
        "customer_id",
        null=True,
        db_index=True,
        max_length=32,
        help_text="the buyer's id",
    )


class OrderDetailModel(models.Model):
    order_id = models.CharField("order_id", max_length=32, null=True, db_index=True)
    commodity_id = models.CharField(
        "commodity_id", max_length=32, null=True, db_index=True
    )


class CommodityModel(models.Model):
    name = models.CharField("name", max_length=32, db_index=True)
    price = models.IntegerField("price")
