from django.conf.urls import url

import converter_views
import connector_views
import cable_views
import page_example.other_product_views
import vna_combo_cable_views
import normal_combo_cable_views
import frequency_standing_wave_views
import frequency_views
import other_product_views
from . import views
import admin_user_login

urlpatterns = [
    url('^test/', views.test, name='test'),
    url(r'^$', views.index, name='index'),
    url(r'^connector_product/', connector_views.connector_product, name='connector'),
    url(r'^converter_product/', converter_views.converter_product, name='converter'),
    url(r'^cable_product/', cable_views.cable_product, name="cable"),
    url(r'^cable_combo_product_vna/', vna_combo_cable_views.cable_combo_product_vna, name="cable_combo_vna"),
    url(r'^cable_combo_product_normal/', normal_combo_cable_views.normal_combo_cable_product, name="cable_combo_normal"),
    url(r'^cable_combo_product_bg/', views.cable_combo_product_gb, name="cable_combo_bg"),
    url(r'^instrument_product/', page_example.other_product_views.instrument_product, name="instrument"),
    url(r'^tool_product/', page_example.other_product_views.tool_product, name='tool'),
    url(r'^admin_login/', views.admin_login, name='admin_login'),
    url(r'^notifytest/', views.notify_test, name='notify'),
    url(r'^try_to_login/', admin_user_login.user_login, name='try_login'),
    url(r'^try_to_logout/', admin_user_login.user_logout, name='try_logout'),
    url(r'^admin/home/', views.admin_home, name="admin_home"),
    url(r'^admin/connector_product/', connector_views.admin_connector_product, name='admin_connector'),
    url(r'admin/admin_bg_combo_cable/', views.admin_cable_combo_product_gb, name='admin_cable_combo_bg'),


    url(r'^admin/product_others_install_type/', views.admin_others_install_type, name='admin_others_install_type'),
    url(r'^admin/add_install_type/', views.admin_add_install_type, name="admin_add_install_type"),
    url('^admin/mod_install_type/', views.admin_modify_install_type, name='admin_modify_install_type'),
    url('^admin/delete_install_type/', views.admin_delete_install_type, name='admin_delete_install_type'),
    url('^admin/product_others_out_look/', views.admin_others_outlook, name='admin_others_out_look'),
    url(r'^admin/add_out_look/', views.admin_add_outlook, name="admin_add_out_look"),
    url('^admin/mod_out_look/', views.admin_modify_outlook, name='admin_modify_out_look'),
    url('^admin/delete_out_look/', views.admin_delete_outlook, name='admin_delete_out_look'),
    url('^admin/product_others_category/', views.admin_others_category, name='admin_others_category'),
    url(r'^admin/add_category/', views.admin_add_category, name="admin_add_category"),
    url('^admin/mod_category/', views.admin_modify_category, name='admin_modify_category'),
    url('^admin/delete_category/', views.admin_delete_category, name='admin_delete_category'),
    url(r'^admin/product_others_combo_type/', views.admin_others_combo_type, name='admin_others_combo_type'),
    url(r'^admin/add_combo_type/', views.admin_add_combo_type, name="admin_add_combo_type"),
    url('^admin/mod_combo_type/', views.admin_modify_combo_type, name='admin_modify_combo_type'),
    url('^admin/delete_combo_type/', views.admin_delete_combo_type, name='admin_delete_combo_type'),

    url('^admin/add_connector_pcb/', connector_views.admin_add_pcb_connector, name='admin_add_pcb_connector'),
    url('^admin/add_connector_cable/', connector_views.admin_add_cable_connector, name='admin_add_cable_connector'),
    url('^admin/admin_filter_pcb_connector', connector_views.admin_filter_connector_pcb, name="admin_filter_connector_pcb"),
    url('^admin/admin_filter_cable_connector', connector_views.admin_filter_connector_cable, name="admin_filter_connector_cable"),
    url('^admin/admin_load_pcb_connector', connector_views.admin_load_connector_pcb_mod_form, name="admin_load_connector_pcb_form"),
    url('^admin/admin_load_cable_connector', connector_views.admin_load_connector_cable_mod_form, name="admin_load_connector_cable_form"),
    url('^admin/admin_delete_pcb_connector', connector_views.admin_delete_pcb_connector, name="admin_delete_pcb_connector"),
    url('^admin/admin_delete_cable_connector', connector_views.admin_delete_cable_connector, name="admin_delete_cable_connector"),
    url(r'^goto_modify_pcb_connector/', connector_views.admin_modify_connector_pcb, name='admin_modify_connector_pcb'),
    url(r'^goto_modify_cable_connector/', connector_views.admin_modify_connector_cable, name='admin_modify_connector_cable'),

    url(r'^admin/converter_product/', converter_views.admin_converter_product, name='admin_converter'),
    url('^admin/add_converter/', converter_views.admin_add_converter, name='admin_add_converter'),
    url('^admin/admin_filter_converter', converter_views.admin_filter_converter, name="admin_filter_converter"),
    url('^admin/admin_load_converter', converter_views.admin_load_converter_mod_form, name="admin_load_converter_form"),
    url('^admin/admin_delete_converter', converter_views.admin_delete_converter, name="admin_delete_converter"),
    url(r'^goto_modify_converter/', converter_views.admin_modify_converter, name='admin_modify_converter'),

    url(r'^admin/cable_product/', cable_views.admin_cable_product, name="admin_cable"),
    url('^admin/add_cable/', cable_views.admin_add_cable, name='admin_add_cable'),
    url('^admin/admin_filter_cable', cable_views.admin_filter_cable, name="admin_filter_cable"),
    url('^admin/admin_load_cable', cable_views.admin_load_cable_mod_form, name="admin_load_cable_form"),
    url('^admin/admin_delete_cable', cable_views.admin_delete_cable, name="admin_delete_cable"),
    url(r'^admin/modify_cable/', cable_views.admin_modify_cable, name='admin_modify_cable'),

    url(r'^admin/vna_combo_cable_product/', vna_combo_cable_views.admin_vna_combo_cable_product, name='admin_vna_combo_cable'),
    url('^admin/add_vna_combo_cable/', vna_combo_cable_views.admin_add_vna_combo_cable, name='admin_add_vna_combo_cable'),
    url('^admin/admin_filter_vna_combo_cable', vna_combo_cable_views.admin_filter_vna_combo_cable, name="admin_filter_vna_combo_cable"),
    url('^admin/admin_load_vna_combo_cable', vna_combo_cable_views.admin_load_vna_combo_cable_mod_form, name="admin_load_vna_combo_cable_form"),
    url('^admin/admin_delete_vna_combo_cable', vna_combo_cable_views.admin_delete_vna_combo_cable, name="admin_delete_vna_combo_cable"),
    url(r'^goto_modify_vna_combo_cable/', vna_combo_cable_views.admin_modify_vna_combo_cable, name='admin_modify_vna_combo_cable'),

    url('^admin/admin_filter_normal_combo_cable', normal_combo_cable_views.admin_filter_normal_combo_cable, name="admin_filter_normal_combo_cable"),

    url('^admin/admin_frequency_standing_wave', frequency_standing_wave_views.admin_frequency_standing_wave,
        name="admin_others_frequency_standing_wave"),

    url('^admin/admin_filter_frequency_standing_wave', frequency_standing_wave_views.admin_filter_frequency_standing_wave,
        name="admin_filter_frequency_standing_wave"),

    url('^admin/admin_insert_frequency_standing_wave',
        frequency_standing_wave_views.admin_insert_frequency_standing_wave,
        name="admin_insert_frequency_standing_wave"),

    url('^admin/admin_frequency',
        frequency_views.admin_frequency,
        name="admin_frequency"),

    url('^admin/admin_modify_frequency',
        frequency_views.admin_modify_frequency,
        name="admin_modify_frequency"),

    url('^admin/admin_add_frequency',
        frequency_views.admin_add_frequency,
        name="admin_add_frequency"),

    url('^admin/admin_delete_frequency',
        frequency_views.admin_delete_frequency,
        name="admin_delete_frequency"),

    url(r'^admin/other_product/', other_product_views.admin_other_product_product, name="admin_other_product"),
    url('^admin/add_other_product/', other_product_views.admin_add_other_product, name='admin_add_other_product'),
    url('^admin/admin_filter_other_product', other_product_views.admin_filter_other_product, name="admin_filter_other_product"),
    url('^admin/admin_load_other_product', other_product_views.admin_load_other_product_mod_form, name="admin_load_other_product_form"),
    url('^admin/admin_delete_other_product', other_product_views.admin_delete_other_product, name="admin_delete_other_product"),
    url(r'^admin/modify_other_product/', other_product_views.admin_modify_other_product, name='admin_modify_other_product'),

]