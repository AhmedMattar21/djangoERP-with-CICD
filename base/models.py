from django.db import models



class warehouses(models.Model):
    warehouse_name = models.TextField(unique=True)
    warehouse_desc = models.TextField(default="None")

    def __str__(self) -> str:
        return self.warehouse_name


class specs(models.Model):
    specs_name = models.TextField()

    def __str__(self) -> str:
        return self.specs_name


class sizes(models.Model):
    size_name = models.TextField()

    def __str__(self) -> str:
        return self.size_name


class products(models.Model):
    product_internal_id = models.TextField(unique=True)
    product_name = models.TextField()
    product_cost_price = models.DecimalField(decimal_places=2, max_digits=10)
    product_sell_price = models.DecimalField(decimal_places=2, max_digits=10)
    product_discount = models.DecimalField(decimal_places=2, max_digits=10)
    product_line = models.TextField()
    product_barcode = models.TextField()
    product_tax_num = models.TextField()

    #fk_customer_id = models.ForeignKey(vendor, on_delete=set)
    fk_specs_id = models.ForeignKey(specs, on_delete=models.SET_NULL, null=True, blank=True)
    fk_size_id = models.ForeignKey(sizes, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self) -> str:
        return self.product_name


class goods(models.Model):
    quantity = models.IntegerField()
    fk_product_id = models.ForeignKey(products, on_delete=models.CASCADE)
    fk_warehouse_id = models.ForeignKey(warehouses, on_delete=models.SET_NULL, null=True, blank=True)
  # fk_invoice_id = models.ForeignKey(invoices , on_delete=models.SET_NULL, null=True, blank=True)
 

class com_category(models.Model):
    com_category_id     =models.TextField(unique=True)
    com_category_name   =models.TextField()
    

class companies(models.Model):
    com_id      		=models.TextField(unique=True)
    com_name    		=models.TextField()
    com_address 		=models.TextField()
    com_phone   		=models.TextField()
    com_email   		=models.TextField()
    com_tax_reg 		=models.TextField()
    com_desc            =models.TextField()
    com_notes 			=models.TextField()
    com_business_type   =models.TextField()
    FK_com_category_id  =models.ForeignKey(com_category, on_delete=set)


class contacts(models.Model):
    contact_name      	=models.TextField()
    contact_phone       =models.TextField()
    contact_position    =models.TextField()
    contact_notes       =models.TextField()
    contact_email       =models.TextField()
    FK_com_id           =models.ForeignKey(companies,on_delete=set)
    FK_com_category_id  =models.ForeignKey(com_category, on_delete=set)

class payments(models.Model):
    payment_id          =models.TextField()
    payment_name      	=models.TextField()
    payment_username    =models.TextField()
    payment_paid        =models.TextField()
    payment_method      =models.TextField()
    payment_comments    =models.TextField()
    payment_date        =models.DateField()
    payment_tot_require =models.DecimalField(decimal_places=2,max_digits=25)
    payment_tot_remind  =models.DecimalField(decimal_places=2,max_digits=25)
    FK_com_id           =models.ForeignKey(companies, on_delete=set)



class groupRols(models.Model):
    group_name = models.TextField()
    group_desc = models.TextField()
    FK_UserCreatedid = models.TextField();

    def __str__(self) -> str:
        return self.group_name


class users(models.Model):
    username = models.TextField()
    user_password = models.TextField()
    FK_group_rol_id = models.ForeignKey(groupRols, on_delete=models.SET_NULL, null=True)
    user_created_id = models.IntegerField(default='None')
