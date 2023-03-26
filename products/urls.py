from django.urls import path

from products import views

urlpatterns = [
    path('', views.products, name='products'),
]

# from rest_framework_mongoengine import routers
#
# from products.views import ProductViewSet
#
# router = routers.SimpleRouter()
# router.register(r'products', ProductViewSet, basename='products')
#
# urlpatterns = router.urls

