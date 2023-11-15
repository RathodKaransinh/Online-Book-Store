import datetime
from django.shortcuts import redirect, render
from home.models import Order, Product
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login

# Create your views here.

def index(request):
    products = Product.objects.values().all()
    context = {
        'products' : products
    }
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')

def orders(request):
    orders = Order.objects.filter(uname=request.user.username).values()
    context = {
        'orders': orders
    }
    return render(request, 'orders.html', context)

def order(request, label):
    
    if request.method == "POST":
        name = request.POST.get('name')
        address = request.POST.get('address')
        order = Order(label=label, name=name, address=address, uname=request.user.username)
        order.save()
        return redirect('/')
    
    context = {
    'label': label,
    }
    return render(request, 'order.html', context)

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
    if request.method == "POST":
        name = request.POST.get('name')
        desc = request.POST.get('desc')
        price = request.POST.get('price')
        image = request.POST.get('image')
        product = Product(name=name, uname=request.user.username, desc=desc, price=price, image=image)
        product.save()
        return redirect('/')
    
    return render(request, 'addProduct.html')