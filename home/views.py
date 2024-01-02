from django.shortcuts import redirect, render
from home.models import *
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages

# Create your views here.

def index(request):
    if request.user.is_anonymous:
        return redirect("/login")
    
    products = None
    categories = Category.get_all_categories()
    categoryID = request.GET.get('category')
    # print(categoryID)
    if categoryID:
        products = Product.get_all_products_by_categoryid(categoryID)
    else:
        products = Product.get_all_products()
        
    context = {
        'products' : products,
        'categories': categories,
        'categoryID': categoryID
    }
    cart = request.session.get('cart')
    if not cart:
        request.session['cart'] = {}
        
        
    
    if request.method == "POST":
        product = request.POST.get('product')
        prod = Product.objects.get(id=product)
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity<=1:
                        cart.pop(product)
                    else:
                        cart[product]  = quantity-1
                else:
                    if prod.stock > quantity:
                        cart[product]  = quantity+1
                    else:
                        messages.error(request, 'Product out of Stock!')

            else:
                if prod.stock >= 1:
                    cart[product] = 1
                else:
                    messages.error(request, 'Product out of Stock!')
        else:
            cart = {}
            if prod.stock >= 1:
                cart[product] = 1
            else:
                messages.error(request, 'Product out of Stock!')

        request.session['cart'] = cart
        print('cart' , request.session['cart'])
        return redirect('/')
    
    return render(request, 'index.html', context)




def about(request):
    return render(request, 'about.html')





def orders(request):
    orders = Order.objects.filter(customer=request.user)
    context = {
        'orders': orders
    }
    return render(request, 'orders.html', context)






def order(request):
    if request.method == "POST":
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        customer = request.user
        cart = request.session['cart']
        for key in cart:
            product = Product.objects.get(id=key)
            quantity = cart[key]
            price = product.price * quantity
            order = Order(product=product, customer=customer, quantity=quantity, price=price, address=address, phone=phone)
            order.save()
            product.stock = product.stock - quantity
            product.save()
        del request.session['cart']
        return redirect('/')

    return render(request, 'order.html')






def loginUser(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)

        # check if user has entered correct credentials
        user = authenticate(username=username, password=password)

        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            return redirect("/")

        else:
            # No backend authenticated the credentials
            return render(request, 'login.html')

    return render(request, 'login.html')






def logoutUser(request):
    logout(request)
    return redirect("/login")






def registerUser(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.create_user(username=username, password=password)
        user.save()
        
        user = authenticate(username=username, password=password)
        
        if user is not None:
            return redirect('/login')
        else:
            pass
        
    return render(request, "register.html")







def addProduct(request):
    product = None
    if request.GET.get('id'):
        product = Product.objects.get(id=request.GET.get('id'))
    
    if request.method == "POST":
        name = request.POST.get('name')
        cat = Category.objects.get(id=request.POST.get('cat'))
        desc = request.POST.get('desc')
        price = request.POST.get('price')
        stock = request.POST.get('stock')
        if request.POST.get('id') == '0':
            image = request.FILES.get('image')
            product = Product(name=name, category=cat, selled_by=request.user, desc=desc, price=price, stock=stock, image=image)
            product.save()
            return redirect('/')
        else:
            product=Product.objects.get(id=request.POST.get('id'))
            product.name = name
            product.category = cat
            product.desc = desc
            product.price = price
            product.stock = stock
            if request.FILES.get('image'):
                product.image = request.FILES.get('image')
            product.save()
            return redirect('/myproducts')
    
    categories = Category.get_all_categories()
    
    return render(request, 'addProduct.html', {'categories':categories,'product': product})






def myproducts(request):
    context = {
        'products': Product.get_all_products_by_userid(request.user)
    }
    # print(request.GET.get('action'))
    # print(request.GET.get('id'))
    if request.GET.get('action') == '0':
        product = Product.objects.get(id=request.GET.get('id'))
        product.delete()
        return redirect('/myproducts')
    
    elif request.GET.get('action') == '1':
        id=request.GET.get('id')
        product = Product.objects.get(id=id)
        return redirect("/add?id="+id)
    else:
        return render(request, 'myproducts.html', context)
    
    
    
    
    
    
def cart(request):
    ids = list(request.session.get('cart').keys())
    products = Product.get_product_by_ids(ids)
    # print(products)
    return render(request , 'cart.html' , {'products' : products} )
    