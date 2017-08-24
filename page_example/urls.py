from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^connector_product/', views.connector_product, name='connector'),
    url(r'^converter_product/', views.converter_product, name='converter'),
    url(r'^cable_product/', views.cable_product, name="cable"),
    url(r'^cable_combo_product_vna/', views.cable_combo_product_vna, name="cable_combo_vna"),
    url(r'^cable_combo_product_normal/', views.cable_combo_product_normal, name="cable_combo_normal"),
    url(r'^cable_combo_product_bg/', views.cable_combo_product_gb, name="cable_combo_bg"),
    url(r'^instrument_product/', views.instrument_product, name="instrument"),
    url(r'^tool_product/', views.tool_product, name='tool'),
    url(r'^admin_login/', views.admin_login, name='admin_login'),
    url(r'^notifytest/', views.notify_test, name='notify')

]