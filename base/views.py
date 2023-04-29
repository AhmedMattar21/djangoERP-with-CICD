from django.shortcuts import render, redirect, get_object_or_404 
#<<<<<<< HEAD
from .models import products, specs, sizes, com_category, companies,contacts,payments, warehouses, goods
from django.http import JsonResponse
#====


#>>>>>>> e020aa0fcfd6c99c8789781f8f2423c6e25204ff


def homePage(request):
    return render(request, 'index.html') 


#       Products 
#===========================
def productsPage(request):
    if request.method == 'POST':
        try:
            if request.POST:
                products.objects.get( product_internal_id=request.POST['prod_intern'])
            return redirect('/products')
        except:
            size = sizes.objects.get(id=request.POST['size_id'])
            spec = specs.objects.get(id=request.POST['spec_id'])
            product = products.objects.create(
            product_internal_id=request.POST['prod_intern'],
            product_name=request.POST['prod_name'],
            product_cost_price=request.POST['prod_cost'],
            product_sell_price=request.POST['prod_price'],
            product_discount=request.POST['prod_dis'],
            product_line=request.POST['prod_line'],
            product_barcode=request.POST['prod_barcode'],
            product_tax_num=request.POST['prod_tax'],
            fk_size_id=size,
            fk_specs_id=spec
            )
            product.save()
            return redirect('/products')

    data = products.objects.all()
    all_sizes = sizes.objects.all()
    all_specs = specs.objects.all()
    context = {'products':data, 'sizes': all_sizes, 'specs': all_specs}
    return render(request, 'products.html', context)

def product_update(request, pk):
    if request.method == 'POST':
        size = sizes.objects.get(id=request.POST['size_id'])
        spec = specs.objects.get(id=request.POST['spec_id'])
        product = products.objects.get(id=pk)
        product.product_name = request.POST['prod_name']
        product.product_cost_price = request.POST['prod_cost']
        product.product_sell_price = request.POST['prod_price']
        product.product_discount = request.POST['prod_dis']
        product.product_line = request.POST['prod_line']
        product.product_barcode = request.POST['prod_barcode']
        product.product_tax_num = request.POST['prod_tax']
        product.fk_size_id = size
        product.fk_specs_id = spec
        try:
             products.objects.get( product_internal_id=request.POST['prod_intern'])
        except:
            product.product_internal_id = request.POST['prod_intern']
        product.save()
        return redirect('/products')
    product = products.objects.get(id=pk)
    all_sizes = sizes.objects.all()
    all_specs = specs.objects.all()
    context = {'p':product, 'sizes': all_sizes, 'specs': all_specs}
    return render(request, 'product_update.html', context)

def product_delete(request, pk):
    product = products.objects.get(id=pk)
    product.delete()
    return redirect('/products')



#       Warehouses 
#===========================
def warehousePage(request):
    if request.method == 'POST':
            warehouse = warehouses.objects.create(
                warehouse_name=request.POST['warehouse_name'],
                warehouse_desc=request.POST['warehouse_desc'],
                )
            warehouse.save()
            return redirect('/warehouses')
    warehouse = warehouses.objects.all()
    context = {'warehouses': warehouse}
    return render(request, 'warehouses.html', context)


def warehouses_update(request, pk):
    if request.method == 'POST':
        warehouse = warehouses.objects.get(id=pk)
        warehouse.warehouse_name = request.POST['warehouse_name']
        warehouse.warehouse_desc = request.POST['warehouse_desc']
        warehouse.save()
        return redirect('/warehouses')
    warehouse = warehouses.objects.get(id=pk)
    context = {'s':warehouse}
    return render(request, 'warehouses_update.html', context)


def warehouses_delete(request, pk):
    warehouse = warehouses.objects.get(id=pk)
    warehouse.delete()
    return redirect('/warehouses')



#       Inventory - WH 
#===========================
def inventoryPage(request):
    warehouse = warehouses.objects.all()
    context = {'warehouses': warehouse}
    return render(request, 'inventory.html', context)


#       Inventory
#===========================
def inventory(request, pk):
    inv = goods.objects.filter(fk_warehouse_id=pk)
    wh = warehouses.objects.get(id=pk)
    context = {'inventory': inv, 'warehouse': wh}
    return render(request, 'inventory_items.html', context)



#       Specs 
#===========================
def specsPage(request):
    if request.method == 'POST':
            spec = specs.objects.create(specs_name=request.POST['specs_name'])
            spec.save()
            return redirect('/specs')
    spec= specs.objects.all()
    context = {'specs': spec}
    return render(request, 'specs.html', context)
def specs_update(request, pk):
    if request.method == 'POST':
        spec = specs.objects.get(id=pk)
        spec.specs_name = request.POST['specs_name']
        spec.save()
        return redirect('/specs')
    spec = specs.objects.get(id=pk)
    context = {'s':spec}
    return render(request, 'specs_update.html', context)
def specs_delete(request, pk):
    spec = specs.objects.get(id=pk)
    spec.delete()
    return redirect('/specs')


#       Sizes 
#===========================
def sizesPage(request):
    if request.method == 'POST':
            size = sizes.objects.create(size_name=request.POST['size_name'])
            size.save()
            return redirect('/sizes')
    size = sizes.objects.all()
    context = {'sizes': size}
    return render(request, 'sizes.html', context)


def sizes_update(request, pk):
    if request.method == 'POST':
        size = sizes.objects.get(id=pk)
        size.size_name = request.POST['size_name']
        size.save()
        return redirect('/sizes')
    size = sizes.objects.get(id=pk)
    context = {'s': size}
    return render(request, 'sizes_update.html', context)


def sizes_delete(request, pk):
    size = sizes.objects.get(id=pk)
    size.delete()
    return redirect('/sizes')


#Company Categories Functions
def com_cat_Page(request):
    if request.method == 'POST':
        try:
            if request.POST:
                com_category.objects.get( com_category_id=request.POST['com_cat_id'])
            return redirect('/company_category')
        except:
            com_category_= com_category.objects.create(
            com_category_id=request.POST['com_cat_id'],
            com_category_name=request.POST['com_cat_name']
            )
            com_category_.save()
            return redirect('/company_category')

    data = com_category.objects.all()
    context = {'company_category':data}
    return render(request, 'company_category.html', context)
def company_category_delete(request, pk):
    com = com_category.objects.get(id=pk)
    com.delete()
    return redirect('/company_category')
def company_category_update(request, pk):
    if request.method == 'POST':
        company_category_ = com_category.objects.get(id=pk)
        company_category_.com_category_id = request.POST['com_cat_id']
        company_category_.com_category_name = request.POST['com_cat_name']
        try:
             com_category.objects.get( com_category_id=request.POST['com_cat_id'])
        except:
            company_category_.com_category_id = request.POST['com_cat_id']
        company_category_.save()
        return redirect('/company_category')
    com_category_ = com_category.objects.get(id=pk)
    context = {'c':com_category_}
    return render(request,'company_category_update.html', context)

#Companies Functions
def company_page(request):
    if request.method == 'POST':
        try:
            if request.POST:
                companies.objects.get( com_id=request.POST['com_id_'])
            return redirect('/companies')
        except:
            com= companies.objects.create(
            com_id      		=request.POST['com_id_'],
            com_name    		=request.POST['com_name_'],
            com_address 		=request.POST['com_address_'],
            com_phone   		=request.POST['com_phone_'],
            com_email   		=request.POST['com_email_'],
            com_tax_reg 		=request.POST['com_tax_reg_'],
            com_desc            =request.POST['com_desc_'],
            com_notes 			=request.POST['com_notes_'],
            com_business_type   =request.POST['com_business_type_'],
            FK_com_category_id  =get_object_or_404(com_category, id=request.POST['FK_com_category_id_'])
            )
            com.save()
            return redirect('/companies')
    data = companies.objects.all()
    data2 = com_category.objects.all()
    context = {'companies':data,'com_categories':data2}
    return render(request, 'companies.html', context)
def company_delete(request, pk):
    com = companies.objects.get(id=pk)
    com.delete()
    return redirect('/companies')
def company_update(request, pk):
    if request.method == 'POST':
        com_ = companies.objects.get(id=pk)
        com_.com_id      		 =request.POST['com_id_']
        com_.com_name    		 =request.POST['com_name_']
        com_.com_address 		 =request.POST['com_address_']
        com_.com_phone   		 =request.POST['com_phone_']
        com_.com_email   		 =request.POST['com_email_']
        com_.com_tax_reg 		 =request.POST['com_tax_reg_']
        com_.com_desc            =request.POST['com_desc_']
        com_.com_notes 			 =request.POST['com_notes_']
        com_.com_business_type   =request.POST['com_business_type_']
        com_.FK_com_category_id  =get_object_or_404(com_category, id=request.POST['FK_com_category_id_'])# ناقصة حتة انه يختار الاساية اللى كان مختارها قبل كده
        
        try:
             companies.objects.get( com_id=request.POST['com_id_'])
        except:
            com_.com_id = request.POST['com_id_']
        com_.save()
        return redirect('/companies')
    com_data = companies.objects.get(id=pk)
    data2 = com_category.objects.all()

    context = {'c':com_data,'categories':data2}
    return render(request,'companies_update.html', context)



#Contacts Functions 
def contacts_page(request):
    if request.method == 'POST':
        try:
            if request.POST:
                contacts.objects.get( contacts_name=request.POST['contact_name_'])
            return redirect('/contacts')
        except:
            com= contacts.objects.create(
            contact_name   =request.POST['contact_name_'],
            contact_phone   =request.POST['contact_phone_'],
            contact_position   =request.POST['contact_position_'],
            contact_notes    =request.POST['contact_notes_'],
            contact_email   =request.POST['contact_email_'],
            FK_com_category_id  =get_object_or_404(com_category, id=request.POST['FK_com_category_id_']),
            FK_com_id  =get_object_or_404(companies, id=request.POST['FK_com_id_'])
            )
            com.save()
            return redirect('/contacts')
    data = contacts.objects.all()
    data_categories = com_category.objects.all()
    data_companies = companies.objects.all()
    context = {'contacts':data,'categories':data_categories,'companies':data_companies}
    return render(request, 'contacts.html', context)
def contact_delete(request, pk):
    con = contacts.objects.get(id=pk)
    con.delete()
    return redirect('/contacts')
def contact_update(request, pk):
    if request.method == 'POST':
        con_ = contacts.objects.get(id=pk)
        con_.contact_name            =request.POST['contact_name_']
        con_.contact_email    		 =request.POST['contact_email_']
        con_.contact_notes		     =request.POST['contact_notes_']
        con_.contact_phone   		 =request.POST['contact_phone_']
        con_.contact_position   	 =request.POST['contact_position_']
        con_.FK_com_category_id      =get_object_or_404(com_category, id=request.POST['FK_com_category_id_'])# ناقصة حتة انه يختار الاساية اللى كان مختارها قبل كده
        con_.FK_com_id               =get_object_or_404(companies, id=request.POST['FK_com_id_'])# ناقصة حتة انه يختار الاساية اللى كان مختارها قبل كده
        try:
             contacts.objects.get(id=pk)
        except:
            con_.id = request.POST[pk]
        con_.save()
        return redirect('/contacts')
    
    data = contacts.objects.get(id=pk)
    data_categories = com_category.objects.all()
    data_companies = companies.objects.all()
    context = {'c':data,'categories':data_categories,'companies':data_companies}
    return render(request, 'contact_update.html', context)

#Payment Functions
def payment_page(request):
    if request.method == 'POST':
        try:
            if request.POST:
                payments.objects.get( payment_id=request.POST['payment_id_'])
            return redirect('/payments')
        except:
            pay= payments.objects.create(
            payment_id      		=request.POST['payment_id_'],
            payment_name    		=request.POST['payment_name_'],
            payment_username 		=request.POST['payment_username_'],
            payment_paid     		=request.POST['payment_paid_'],
            payment_method   		=request.POST['payment_method_'],
            payment_comments 		=request.POST['payment_comments_'],
            payment_date            =request.POST['payment_date_'],
            payment_tot_require     =request.POST['payment_tot_require_'],
            payment_tot_remind   =request.POST['payment_tot_remind_'],
            FK_com_id  =get_object_or_404(companies, id=request.POST['FK_com_id_'])
            )
            pay.save()
            return redirect('/payments')
    data = companies.objects.all()
    data2 = com_category.objects.all()
    pay_data= payments.objects.all()
    context = {'companies':data,'categories':data2,'payments':pay_data}
    return render(request, 'payments.html', context)
def payment_delete(request, pk):
    pay = payments.objects.get(id=pk)
    pay.delete()
    return redirect('/payments')
def payment_update(request, pk):
    if request.method == 'POST':
        pay_ = payments.objects.get(id=pk)
        pay_.payment_id            =request.POST['payment_id_']
        pay_.payment_name  		   =request.POST['payment_name_']
        pay_.payment_username	   =request.POST['payment_username_']
        pay_.payment_paid  		   =request.POST['payment_paid_']
        pay_.payment_method   	   =request.POST['payment_method_']
        pay_.payment_comments  	   =request.POST['payment_comments_']
        pay_.payment_date          =request.POST['payment_date_']
        pay_.payment_tot_require   =request.POST['payment_tot_require_']
        pay_.payment_tot_remind    =request.POST['payment_tot_remind_']
        pay_.FK_com_id             =get_object_or_404(companies, id=request.POST['FK_com_id_'])# ناقصة حتة انه يختار الاساية اللى كان مختارها قبل كده
        try:
             payments.objects.get(id=pk)
        except:
            pay_.id = request.POST[pk]
        pay_.save()
        return redirect('/payments')
    data = payments.objects.get(id=pk)
    data_categories = com_category.objects.all()
    data_companies = companies.objects.all()
    context = {'p':data,'categories':data_categories,'companies':data_companies}
    return render(request, 'payment_update.html', context)

#Combo Box Views
def get_json_category_data(request):
    qs_val =list(com_category.objects.values())
    return JsonResponse({'data':qs_val})

def get_json_companies_data_by_id(request,pk):
    obj_dependancy_companies = list(companies.objects.filter(FK_com_category_id = pk).values())    
    return JsonResponse({'data':obj_dependancy_companies})







