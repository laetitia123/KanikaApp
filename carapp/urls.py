from . import views
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^about/$',views.aboutus,name='about'),
    url(r'^contact/$',views.contactus,name='contact'),
    url(r'^upload/$',views.upload,name='upload'),
    url(r'^$',views.homePage,name='homePage'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^upload/$',views.upload,name='upload'),
    url(r'register/',views.register,name = 'register'),
    url(r'login/',views.login_view,name='login'),
    url(r'logout/',views.logout_view,name='logout'),
    url(r'^carDetails/(\d+)$',views.carDetails,name='carDetails'),
    url(r'^cart/$',views.cart,name='cart'),
    url(r'^addToCart/(\d+)/$', views.addToCart, name="addToCart"),
    url(r'profile/(\d+)', views.profile_view, name = 'profile'),
    url(r'update_profile/', views.update_profile, name = 'update_profile'),
    # url(r'^api/merch/$', views.MerchList.as_view()),
    url(r'category/(\d+)',views.filter_By_category, name='category'),
    url(r'^category/$',views.all_category, name='all_category'),
    url(r'', views.default_map, name="default"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)