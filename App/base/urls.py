from django.urls import path
from . import views


urlpatterns = [
   
    path('',views.homePage, name='home'),
    path('products',views.productsPage, name='products'),
    path('product-delete/<str:pk>',views.product_delete, name='delete-product'),
    path('product-update/<str:pk>',views.product_update, name='update-product'),

    path('warehouses',views.warehousePage, name='warehouses'),
    path('warehouses-update/<str:pk>',views.warehouses_update, name='update-warehouses'),
    path('warehouses-delete/<str:pk>',views.warehouses_delete, name='delete-warehouses'),

    path('specs',views.specsPage, name='specs'),
    path('specs-update/<str:pk>',views.specs_update, name='update-specs'),
    path('specs-delete/<str:pk>',views.specs_delete, name='delete-specs'),

    path('sizes',views.sizesPage, name='specs'),
    path('sizes-update/<str:pk>',views.sizes_update, name='update-sizes'),
    path('sizes-delete/<str:pk>',views.sizes_delete, name='delete-sizes'),


    path('company_category',views.com_cat_Page, name='company_category'),
    path('company-category-delete/<str:pk>',views.company_category_delete, name='company-category-delete'),
    path('company-category-update/<str:pk>',views.company_category_update, name='company-category-update'),

    path('companies',views.company_page, name='companies'),
    path('company-delete/<str:pk>',views.company_delete, name='company-delete'),
    path('company-update/<str:pk>',views.company_update, name='company-update'),

    path('inventory',views.inventoryPage, name='inventory'),
    path('inventory/<str:pk>',views.inventory, name='warehouse-inventory'),




    path('contacts',views.contacts_page, name='contacts'),
    path('contact-delete/<str:pk>',views.contact_delete, name='contact-delete'),
    path('contact-update/<str:pk>',views.contact_update, name='contact-update'),

    path('payments',views.payment_page, name='payments'),
    path('payment-delete/<str:pk>',views.payment_delete, name='payment-delete'),
    path('payment-update/<str:pk>',views.payment_update, name='payment-update'),


    path('category-json/',views.get_json_category_data, name='category-json'),
    path('comapnies-json/<str:pk>',views.get_json_companies_data_by_id, name='comapnies-json'),



]