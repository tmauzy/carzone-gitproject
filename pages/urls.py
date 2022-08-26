from django.urls import path
from . import views # Need to import views like this to 'define' views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', views.home, name='home'),
]
