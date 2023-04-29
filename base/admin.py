from django.contrib import admin

from .models import products, specs, sizes, com_category,companies,contacts, warehouses, goods,payments

admin.site.register(products)
admin.site.register(specs)
admin.site.register(sizes)
admin.site.register(com_category)

admin.site.register(companies)
admin.site.register(contacts)
admin.site.register(payments)

admin.site.register(warehouses)
admin.site.register(goods)

