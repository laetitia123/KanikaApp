from . import views
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^about/$',views.aboutus,name='about'),
    url(r'^contact/$',views.contactus,name='contact'),
    url(r'^$',views.homePage,name='homePage'),
    url(r'register/',views.register,name = 'register'),
    url(r'login/',views.login_view,name='login'),
    url(r'logout/',views.logout_view,name='logout'),
    url(r'^carDetails/(\d+)$',views.carDetails,name='carDetails'),
    url(r'^cart/$',views.cart,name='cart'),
    url(r'^addToCart/(\d+)/$', views.addToCart, name="addToCart"),
    url(r'profile/(\d+)', views.profile_view, name = 'profile'),
    url(r'update_profile/', views.update_profile, name = 'update_profile'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)