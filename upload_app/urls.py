from django.urls import path
from . import views
urlpatterns=[
    path('set_cookies',views.set_cookies),
    path('get_cookies',views.get_cookies),
    path('set_session',views.set_session),
    path('get_session',views.get_session),
    path('model/',views.model),

]
