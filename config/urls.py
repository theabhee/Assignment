from django.contrib import admin
from django.urls import path
from warehouse.views import recommend_box

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/recommend/', recommend_box),
]