from django.shortcuts import render,redirect,HttpResponse
from app1.models import Cart,Product,SubCategory,Category,ProductImage,ProductDetails,Color,Size,Brand,Order
import random
from django.db.models import Q
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
catG=0
# color = 0
size1 = 'S'

def search(request,value):
    print('serch function call')
    type = Product.objects.filter(Q(subcategory__name__istartswith = value) | 
                                      Q(subcategory__category__name__icontains = value))
    print(type)
        
    brand = Brand.objects.all().values_list('name',flat=True)
    print(brand)
    context = {
               'type':type,
               "brand":brand,
               }
    return render(request,'second.html',context)

def home(request):
    obj = SubCategory.objects.get(name = 'T-shirts')
    obj2 = SubCategory.objects.get(name = 'hoodies')
    obj3 = SubCategory.objects.get(name = 'Sweaters')
    obj4 = SubCategory.objects.get(name = 'Shirts')
    obj5 = SubCategory.objects.get(name = 'Sweatshirts')
    print(obj5)
    # org = SubCategory.objects.get(name = 'Tops')
    obj6 = SubCategory.objects.filter(name__endswith = 'Tops').values_list('id',flat=True)
    obj7 = SubCategory.objects.get(name = 'Tube Tops')
    obj8 = SubCategory.objects.get(name = 'Off-shoulder Tops')
    tops = list(obj6)
    # tops.insert(0,org.id)
    if(request.method == 'GET'):
        val = request.GET.get('search')
        if val is not None:
            search_result = search(request, val)
            return search_result
        
    T_shirts = Product.objects.filter(subcategory = obj.id)
    hoodies = Product.objects.filter(subcategory = obj2.id)
    Sweaters = Product.objects.filter(subcategory = obj3.id)
    Shirts = Product.objects.filter(subcategory = obj4.id)
    Sweatshirts = Product.objects.filter(subcategory = obj5.id)
    allTops = Product.objects.filter(subcategory__in = tops)
    TubeTops = Product.objects.filter(subcategory = obj7)
    OffShoulderTops = Product.objects.filter(subcategory = obj8)
    context = {"T_shirts":T_shirts,
               "hoodies":hoodies,
               "Sweaters":Sweaters,
               "Shirts":Shirts,
               "Sweatshirts":Sweatshirts,
               "allTops":allTops,
               "TubeTops":TubeTops,
               "OffShoulderTops":OffShoulderTops,
               }
    print(T_shirts.first().subcategory.name)
    return render(request,'index.html',context)

def second(request,cat,id):
    global catG
    type = list(Product.objects.filter(gender=cat))
    if not type:
        type = list(Product.objects.filter(subcategory__name__icontains=cat))
        if not type:    
            type = list(Product.objects.filter(subcategory__name=cat))
            if not type:
                type = list(Product.objects.filter(subcategory__category__name = cat))
                if not type:
                    type = list(Product.objects.filter(brand__name = cat))
    random.shuffle(type)
    if id:
        obj = Product.objects.get(id=id)
        type.insert(0,obj)
    rDub = []
    if(request.method == 'GET'):
        val = request.GET.get('search')
        if val is not None:
            search_result = search(request, val)
            return search_result
    brand = Brand.objects.all().values_list('name',flat=True)
    product = [rDub.append(i) for i in type if i not in rDub]
    context = {
               'id':id,
               'type':rDub,
               "cat":cat,
               "brand":brand,
               }
    
    catG = cat
    return render(request , 'second.html' , context)


def priceSort(request,price):
    type = Product.objects.filter(gender=catG)
    print(type)
    if not type:
        type = Product.objects.filter(subcategory__name__icontains=catG)
        print(type)
        if not type:    
            type = Product.objects.filter(subcategory__name=catG)
            print(type)
            if not type:
                type = Product.objects.filter(subcategory__category__name = catG)
                print(type)
                if not type:
                    type = Product.objects.filter(brand__name = catG)
                    print(type)
    brand = Brand.objects.all().values_list('name',flat=True)

    if price == 'high':
        sort = type.order_by('-price')
    else:
        sort = type.order_by('price')
    
    if request.method == 'POST':
        Min = request.POST['min']
        Max = request.POST['max']
        g = Q(price__gte = Min)
        l = Q(price__lte = Max)
        sort = type.filter(g & l)
    context = {
        'type':sort,
        "brand":brand,
        "cat":catG,
    }    
    return render(request,'second.html',context)

def brandSort(request):
    pass

def detail(request,id):
    product = Product.objects.get(id=id)
    sort1 = product.subcategory
    sort = Product.objects.filter(Q(subcategory__name__icontains = sort1) & ~Q(id =id))
       
    if(request.method == 'POST'):
        # global color,size1
        global size1
        size1 = request.POST.get('size')
        # color = request.POST.get('color')
        print(f'color is {size1}')
        
    if(request.method == 'GET'):
        val = request.GET.get('search')
        if val is not None:
            search_result = search(request, val)
            return search_result
        
    context={
        'product':product,
        'sort':sort
    }
    return render(request,'detail.html',context)

def cart(request):
    obj = Cart.objects.filter(uid = request.user.id)
    if(request.method == 'GET'):
        val = request.GET.get('search')
        if val is not None:
            search_result = search(request, val)
            return search_result
    # for i in obj:
    #     print(i.pColor)

    context={
        'cloth':obj,
    }
    return render(request,'cart.html',context)

# def addCart(request, id):
#     user_instance = request.user
#     product_instance = Product.objects.get(id=id)
    
#     existing_cart_entry = Cart.objects.filter(uid=user_instance, product=product_instance).first()
#     if existing_cart_entry:
#         existing_cart_entry.qty += 1
#         existing_cart_entry.save()
#         print('product is alredy in cart')
#     else:
#         obj = Cart.objects.create(uid=user_instance, product=product_instance, pColor=color, size=size1)
#         obj.save()
#     return redirect('cart')

@login_required(login_url='loginBtn')
def addCart(request, id,color):
    user_instance = request.user
    product_instance = Product.objects.get(id=id)
    price1 = product_instance.price
    existing_cart_entry = Cart.objects.filter(uid=user_instance,pColor = color, product=product_instance).first()
    if existing_cart_entry:
        existing_cart_entry.qty += 1
        existing_cart_entry.save()
        print('product is alredy in cart')
    else:
        obj = Cart.objects.create(uid=user_instance, product=product_instance, pColor=color, size=size1,price = price1)
        obj.save()
    return redirect('cart')

def cartDelit(request,id):
    obj = Cart.objects.get(id=id)
    obj.delete()
    print(id)
    if(request.method == 'GET'):
        val = request.GET.get('search')
        if val is not None:
            search_result = search(request, val)
            return search_result
    return redirect('cart')

def cartModify(request,id):
    pass

def qtyUpdate(request,id,mode):
    c=Cart.objects.filter(id=id)
    q=c[0].qty
    if(request.method == 'GET'):
        val = request.GET.get('search')
        if val is not None:
            search_result = search(request, val)
            return search_result
    price1 = c[0].price
    print(q)
    if(mode == 1):
        q +=1
        price1 *=2
        print('1')
    elif(q > 1):
        q -=1
        price1 /= 2
        print(0)
    c.update(qty = q,price = price1)
    return redirect('cart')

import razorpay
from decimal import Decimal
import json
from django.core.serializers.json import DjangoJSONEncoder
from django.conf import settings
def Payment(request,id):
    amt = Cart.objects.get(id=id)
    total = int(amt.price) * 100 
    client = razorpay.Client(auth = (settings.RAZORPAY_API_KEY, settings.RAZORPAY_API_SECRET))
    payment = client.order.create({'amount':total,"currency": "INR","payment_capture":1})
    # payment_json = json.dumps(payment, cls=DjangoJSONEncoder)
    amt1=amt.product.images.all()
    for i in amt1:
        if amt.pColor == i.color.name:
            bgimage = i.image1
            print(bgimage)
            context = {'payment':payment,'amt':amt, 'bgimage':bgimage}
            return render(request,'payment.html',context)
    context = {'payment':payment,'amt':amt}
    return render(request,'payment.html',context)

def logoutBtn(request):
    logout(request)
    return redirect('home')

def loginBtn(request):
    if(request.method == 'POST'):
        un=request.POST['username']
        pass1=request.POST['password']
        obj = authenticate(request,username = un, password = pass1)
        if(obj is not None):
            login(request,obj)
            return redirect('home')
        else:
            msg = 'Invalid Username and Password'
            context = {'msg':msg}
            return render(request,'login.html',context)
    return render(request,'login.html')

def signUp(request):
    if(request.method == 'POST'):
        un=request.POST['username']
        mail=request.POST['email']
        pass1=request.POST['password']
        pass2=request.POST['password2']
        if(pass1 == pass2):
            obj = User.objects.create_user(username=un,email=mail,password=pass1)
            obj.save()
            return redirect('loginBtn')
        else:
            msg = 'Password and Confirm Password is not Same'
            context={'msg':msg}
        return render(request,'signup.html',context)
    return render(request,'signup.html')

def addInOrder(request,id):
    user_instance = request.user
    c_instace = Cart.objects.get(id = id)
    product_instance = Product.objects.get(id=c_instace.product.id)
    obj = Order.objects.create(uid = user_instance, product = product_instance, size = c_instace.size , qty = c_instace.qty , price = c_instace.price, pColor = c_instace.pColor)
    obj.save()
    c_instace.delete()
    return redirect('order')

def order(request):
    obj = Order.objects.filter(uid = request.user.id)
    context = {'obj':obj}
    if(request.method == 'GET'):
        val = request.GET.get('search')
        if val is not None:
            search_result = search(request, val)
            return search_result
    return render(request,'order.html',context)