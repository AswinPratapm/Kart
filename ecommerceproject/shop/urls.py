from django.urls import path,include
from . import views
app_name='shop'
urlpatterns = [

    path('',views.allprodcat,name='allproductcat'),
    path('<slug:c_slug>/', views.allprodcat,name='productsbycategory'),
    path('<slug:c_slug>/<slug:product_slug>/',views.proDetail,name='prodcatdetail')


]