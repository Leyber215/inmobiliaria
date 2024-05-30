from django.urls import path, include
from .views import PropertyView, property_detail, buy_property

urlpatterns = [
    path('form/', PropertyView, name="form-property"),
    path('detail/<int:property_id>/', property_detail, name='property_detail'),
    path('<int:property_id>/buy/', buy_property, name='buy_property'),
    # path('properties/', PropertyAPIClient.create_property, name='property-create'),
]