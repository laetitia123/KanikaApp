from __future__ import unicode_literals
from .forms import RegisterForm,ProfileForm
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render,redirect
from .models import SpareParts,CarCategory,Cart,User,Profile
from .forms import CartAddProductForm




# def cart_detail(request):
#     cart = Cart(request)
#     for item in cart:
#         item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'], 'update': True})
#     return render(request, 'cart/detail.html', {'cart': cart})


# Create your views here.

def aboutus(request):
    # categories=CarCategory.objects.all()
    # spareParts=SpareParts.objects.all()
    # context={
    #     'categories':categories,
    #     'spareParts':spareParts
    # }
    return render(request,'spare/aboutus.html')
def contactus(request):
    # categories=CarCategory.objects.all()
    # spareParts=SpareParts.objects.all()
    # context={
    #     'categories':categories,
    #     'spareParts':spareParts
    # }
    return render(request,'spare/contact.html')


def homePage(request):
    categories=CarCategory.objects.all()
    spareParts=SpareParts.objects.all()
    context={
        'categories':categories,
        'spareParts':spareParts
    }
    return render(request,'spare/spare.html',context)

def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
        return redirect('spareparts:login')
    else:
        form = RegisterForm()
    return render(response, "registration/register.html", {"form":form})

def login_view(request):
    if request.method=="POST":
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            return redirect('spareparts:welcome')
    else:
        form=AuthenticationForm()
    return render(request, 'registration/login.html',{"form":form})

def logout_view(request):
    if request.method=="POST":
        logout(request)
    return redirect('spareparts:login')



def carDetails(request,carId):
    category=CarCategory.objects.get(id=carId)
    spareParts=SpareParts.objects.filter(carCat=category)
    context={
        'carCats':spareParts
    }
    return render(request,'details.html',context)


def cart(request):
    sparePart=Cart.objects.all()[0]
    context={
        'spareParts':sparePart,
    }
    return render (request,'order.html',context)

def addToCart(request,spareId):
    spareParts=Cart.objects.all()[0]
    spa=SpareParts.objects.get(id=spareId)
    if not spa in spareParts.sparePart.all():
        spareParts.sparePart.add(spa )
    else:
        spareParts.sparePart.remove(spa )
    # return httpResponseRedirect(reverse("cart"))
    newTotal=0
    for spareP in spareParts.sparePart.all():
        newTotal += spareP.price
        spareParts.total = newTotal
        spareParts.save()
    return redirect('cart')

# def addToCart(request,slug):
#     spareParts=Cart.objects.all()[0]
#     try:

#        sparePart=SpareParts.objects.get(slug=slug)
#     except SpareParts.DoesNotExist:
#         pass
#     except:
#         pass
#     if not spareParts in spareParts.spareParts.all():
#       spareParts.spareParts.add(sparePart)
#     else:
#        cart.sparePart.remove(sparePart)
#     # return httpResponseRedirect(reverse("cart"))
#     newTotal=0.00
#     for spareP in cart.sparePart.all():
#         newTotal+=spareP.price
#         spareParts.total=newTotal
#         spareParts.save() 
#     return redirect('cart')


def delete(request, cartId):
    cart = Cart.objects.get(sparePart__id=cartId)
    cart.delete()
    return redirect('homePage')


def profile_view(request,user_id):
   current_user = request.user.username
   if request.method == 'POST':
       form = ProfileForm(request.POST, request.FILES)
       if form.is_valid():
           profile = form.save(commit=False)
           profile.user = current_user
           profile.save()
           return redirect('profile')
   else:
       form = ProfileForm()
   user=User.objects.all()
   profile = Profile.objects.filter(user__username = current_user)
   return render(request,"profile.html",{"user":user,"profile":profile})

def update_profile(request):
   current_user=request.user
   if request.method =='POST':
       if Profile.objects.filter(user_id=current_user).exists():
           form = ProfileForm(request.POST,request.FILES,instance=Profile.objects.get(user_id = current_user))
       else:
           form=ProfileForm(request.POST,request.FILES)
       if form.is_valid():
         profile=form.save(commit=False)
         profile.user=current_user
         profile.save()
         return redirect('profile',current_user.id)
   else:
       if Profile.objects.filter(user_id = current_user).exists():
          form=ProfileForm(instance =Profile.objects.get(user_id=current_user))
       else:
           form=ProfileForm()
   return render(request,'profile_form.html',{"form":form})