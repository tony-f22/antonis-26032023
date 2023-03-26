from djongo import models


class Image(models.Model):
    url = models.CharField(max_length=100, null=True, blank=True)
    path = models.CharField(max_length=100, null=True, blank=True)
    s3_url = models.CharField(max_length=100, null=True, blank=True)
    s3_url_resized = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        abstract = True


class Product(models.Model):
    _id = models.ObjectIdField()
    gender = models.CharField(max_length=100, blank=False, default='')
    product_id = models.CharField(max_length=100)
    product_title = models.CharField(db_index=True, max_length=100, null=False, blank=False, default='')
    product_description = models.TextField(max_length=500, null=False, blank=False, default='')
    brand = models.CharField(max_length=50, null=False, blank=False, default='')
    source = models.CharField(max_length=50, null=False, blank=False, default='')

    product_categories = models.JSONField()

    url = models.URLField(max_length=100, null=True, blank=True)
    price = models.DecimalField(max_digits=19, decimal_places=4)
    discount = models.DecimalField(max_digits=19, decimal_places=7)
    currency_code = models.CharField(max_length=100, blank=False, default='')
    stock = models.IntegerField(null=False, blank=False, default=1)
    stock_level = models.IntegerField(null=False, blank=False, default=1)

    additional_ids = models.JSONField(null=True, blank=True)
    image_urls = models.JSONField(null=True, blank=True)
    position = models.JSONField(null=True, blank=True)
    product_imgs_src = models.JSONField(null=True, blank=True)

    images = models.ArrayField(
        model_container=Image,
        blank=True,
        null=True
    )

    objects = models.DjongoManager()

    def __str__(self):
        return self.product_title

# from mongoengine import Document, EmbeddedDocument, fields
#
#
# class Image(EmbeddedDocument):
#     url = fields.URLField(max_length=100)
#     path = fields.URLField(max_length=100)
#     s3_url = fields.URLField(max_length=100)
#     s3_url_resized = fields.URLField(max_length=100)
#
#
# class Product(Document):
#     # _id = fields.ObjectIdField()
#     id = fields.StringField(required=True, primary_key=True)
#     gender = fields.StringField(max_length=100)
#     product_id = fields.StringField(max_length=100)
#     product_title = fields.StringField(max_length=100)
#     product_description = fields.StringField(max_length=100)
#     brand = fields.StringField(max_length=100)
#     source = fields.StringField(max_length=100)
#
#     product_categories = fields.ListField(fields.StringField(max_length=100))
#
#     url = fields.URLField(max_length=100)
#     price = fields.IntField()
#     discount = fields.FloatField()
#     currency_code = fields.StringField(max_length=100)
#     stock = fields.IntField(min_value=1)
#     stock_level = fields.IntField(min_value=1)
#
#     additional_ids = fields.ListField(fields.StringField(max_length=100))
#     image_urls = fields.ListField(fields.URLField(max_length=100))
#     position = fields.ListField(fields.StringField(max_length=100))
#     product_imgs_src = fields.ListField(fields.URLField(max_length=100))
#
#     images = fields.ListField(fields.EmbeddedDocumentField(Image))
