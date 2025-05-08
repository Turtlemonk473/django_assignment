
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("polls/", include("polls.urls")),
    path('admin/', admin.site.urls),

    urlpatterns = [
    path('', views.index, name='index'),  # maps to the index view
]
]
