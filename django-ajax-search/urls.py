from django.contrib import admin
from django.urls import path
from core import views as core_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("artists/", core_views.artists_view, name="artists"),
]
