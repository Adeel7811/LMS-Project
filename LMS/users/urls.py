from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    # path('', Register_view, name='register'),
    # path('login/', Login_view, name='login'),
    # path('dashboard/', Dashboard_view, name='dashboard'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)