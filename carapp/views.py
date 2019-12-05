from __future__ import unicode_literals
# from .forms import RegisterForm,ProfileForm,ShareholderForm
from .forms import RegisterForm,ProfileForm,sparepartForm
from django.contrib.auth.forms import AuthenticationForm
# from django.contrib.auth import login,logout
from django.shortcuts import render,redirect
from django.contrib.auth import login,logout
from .models import SpareParts,CarCategory,Cart,User,Profile
# from __future__ import unicode_literals
from .forms import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout
from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import CarMerch
from .serializer import *
from rest_framework import status
from .permissions import IsAdminOrReadOnly
from django.contrib.auth.decorators import login_required


class MerchList(APIView):
    def get(self, request, format=None):
        all_merch = CarMerch.objects.all()
        serializers = MerchSerializer(all_merch, many=True)
        return Response(serializers.data)
        
    def post(self, request, format=None):
        serializers = MerchSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    # permission_classes = (IsAdminOrReadOnly,)
class SpareList(APIView):
    def get(self, request, format=None):
        all_spares =SpareParts.objects.all()
        serializers =SpareSerializer(all_spares, many=True)
        return Response(serializers.data)
        
    def post(self, request, format=None):
        serializers = SpareSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    # permission_classes = (IsAdminOrReadOnly,)
        
# from .forms import CustomAuthenticationForm
# from bootstrap_modal_forms.generic import BSModalLoginView
# from django.urls import reverse_lazy

# class CustomLoginView(BSModalLoginView):
#     authentication_form = CustomAuthenticationForm
#     template_name = 'examples/login.html'
#     success_message = 'Success: You were successfully logged in.'
#     extra_context = dict(success_url=reverse_lazy('index'))



# def cart_detail(request):
#     cart = Cart(request)
#     for item in cart:
#         item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'], 'update': True})
#     return render(request, 'cart/detail.html', {'cart': cart})




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
        return redirect('login')
    else:
        form = RegisterForm()
    return render(response, "registration/register.html", {"form":form})

def login_view(request):
    if request.method=="POST":
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            return redirect('homePage')
    else:
        form=AuthenticationForm()
    return render(request, 'registration/login.html',{"form":form})

def logout_view(request):
    if request.method=="POST":
        logout(request)
    return redirect('login')



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

#........API views function----------
# class MerchList(APIView):
#     def get(self, request, format=None):
#         all_merch = CarMerch.objects.all()
#         serializers = MerchSerializer(all_merch, many=True)
#         return Response(serializers.data)
    

@login_required(login_url='login/')
def upload(request,partner_id):
    shareholder=Partners.objects.filter(id=partner_id).first()
    current_user = request.user
    if request.method == 'POST':
        form = sparepartForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.nameChoose = current_user
            post.partner_name = shareholder 
            post.save()
        return redirect('homePage')

    else:
        form = sparepartForm()
    return render(request, 'upload.html', {"form": form,"partner_id":partner_id})

def filter_By_category(request,category_id):
    category=CarCategory.objects.filter(id=category_id)
    spareparts = SpareParts.objects.filter(id=category_id)
    return render (request,"spare/spare.html", {"spareparts":spareparts})

# def all_category(request):
#     category=CarCategory.objects.all()
#     return render (request,"homepage.html", {"categories":category})

    
    
# --------------------------map function-----------
def default_map(request):
    # TODO: move this token to Django settings from an environment variable
    # found in the Mapbox account settings and getting started instructions
    # see https://www.mapbox.com/account/ under the "Access tokens" section
    mapbox_access_token = 'pk.eyJ1IjoibWVkaWF0cmljZSIsImEiOiJjazMydzFnbW8wbWJjM25vMmIyaGVpb2dmIn0.iQ5LI4Rq3YM8xibnmAEuaw'
    return render(request, 'default.html', 
                  { 'mapbox_access_token': mapbox_access_token })


@login_required(login_url='login/')
def shareholder(request):
    current_user = request.user
    shareholder = Partners.objects.filter(user = current_user).first()
    print( shareholder)
    print(current_user)
    spareParts = SpareParts.objects.filter(partner_name = shareholder).all()
    # spareParts = SpareParts.objects.all()
    print(spareParts)
    message=None
    if shareholder is None:
        message= "you are not registered as a partner"
        print(message)
        # redirect(username_present)
        # if partner.approved == False:
        #     redirect("username_present")
    elif shareholder.approved == False:
        message= "please check in 24 hours  "
        print(message)
    else:
        message= "Welcome to Azapp Business View"
  
    # spa=SpareParts.objects.get(id=spareId)
    # if not spa in spareParts.sparePart.all():
    #     spareParts.sparePart.add(spa )
    # else:
    #     spareParts.sparePart.remove(spa )
    # # return httpResponseRedirect(reverse("cart"))
   
    # for sparepart in spareParts.sparePart.all():
        
    #     spareParts.save()
    
    return render(request,'spare/shareholder.html',{'spareParts':spareParts,'current_user':current_user,'message':message,'shareholder':shareholder})
def username_present(request):
    user=request.user
    # current_user = request.user
    if request.method == 'POST':
        form = UpdateParForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = user
            post.save()
            return redirect('shareholder')
    else:
        form = UpdateParForm()
    return render (request, 'parteform.html', {"form":form})


def search_results(request):
    if 'categoryName' in request.GET and request.GET['categoryName']:
        search_term = request.GET.get("categoryName")
        searched_category = SpareParts.search_by_categoryname(search_term).all()
        
        # message = f'{search_term}'
        
        return render(request,'search.html',{"message":message,"category":searched_category})
    
    else:
        message = "You haven't searched for any term"
        return render(request,'search.html',{"message":message,"category":searched_category})
