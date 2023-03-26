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
