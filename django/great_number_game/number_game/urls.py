from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index),  
    path('result', views.result),  
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# urlpatterns = [
#     path('', views.index),
#     path('plus2', views.plus2),
#     path('destroy_session', views.destroy_session),
# ]