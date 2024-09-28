from django.contrib import admin
from django.urls import path
from legislators.views import legislators_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('legislators/', legislators_view, name='legislators'),
]
