from django.urls import path
from .views import CategoryView, AddProductViewSet
urlpatterns = [
    path('category', CategoryView.as_view(), name='category'),
    path('add-product', AddProductViewSet.as_view({'post': 'create'}), name='add-product'),

]
