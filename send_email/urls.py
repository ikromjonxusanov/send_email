from django.contrib import admin
from django.urls import path

from main.views import ContactView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ContactView.as_view(), name="contact")
]
