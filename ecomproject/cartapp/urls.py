from django .urls import path
from . import views
app_name='cartapp'
urlpatterns =[
    path('add/<int:product_id>/',views.AddCart,name="addcart"),
    path('',views.cart_detail,name="cart_detail"),
    path('remove/<int:product_id>/',views.cart_remove,name="cart_remove"),
    path('clear/<int:product_id>/',views.all_clear,name="all_clear"),
]