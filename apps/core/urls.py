from django.urls import path
from apps.core.views import Home

urlpatterns = [
    path('', Home.as_view(), name="core"),

]
