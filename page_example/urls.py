from django.conf.urls import url
from . import views
import admin_user_login

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
    url(r'^notifytest/', views.notify_test, name='notify'),
    url(r'^try_to_login/', admin_user_login.user_login, name='try_login'),
    url(r'^try_to_logout/', admin_user_login.user_logout, name='try_logout'),
    url(r'^admin/home/', views.admin_home, name="admin_home"),
    url(r'^admin/connector_product/', views.admin_connector_product, name='admin_connector'),
    url(r'^goto_modify_connector/', views.admin_modify_connector, name='goto_modify_connector'),
    url(r'^admin/converter_product/', views.admin_converter_product, name='admin_converter'),
    url(r'^admin/cable_product/', views.admin_cable_product, name="admin_cable"),
    url(r'^admin/cable_combo_product_vna/', views.admin_cable_combo_product_vna, name="admin_cable_combo_vna"),
    url(r'^admin/cable_combo_product_normal/', views.admin_cable_combo_product_normal, name="admin_cable_combo_normal"),
    url(r'^admin/cable_combo_product_bg/', views.admin_cable_combo_product_gb, name="admin_cable_combo_bg"),
    url(r'^admin/instrument_product/', views.admin_instrument_product, name="admin_instrument"),
    url(r'^admin/tool_product/', views.admin_tool_product, name='admin_tool'),
    url(r'^admin/product_others_install_type/', views.admin_others_install_type, name='admin_others_install_type'),
    url(r'^admin/add_install_type/', views.admin_add_install_type, name="admin_add_install_type"),
    url('^admin/mod_install_type/', views.admin_modify_install_type, name='admin_modify_install_type')
]