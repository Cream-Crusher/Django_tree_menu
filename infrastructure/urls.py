from django.contrib import admin
from django.urls import path, include

from application import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.show_page, name='home_page'),
    path('<int:pk>/', views.show_page, name='show_page'),
    path('silk/', include('silk.urls', namespace='silk')),
]
