"""fancy_cars URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Cars.models import Cars
from Cars.views import PostDetailView, PostListView, PostCreateView, PostUpdateView, PostDeleteView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", PostListView.as_view(), name="CarListView"),
    path("cars/<int:pk>/", PostDetailView.as_view(), name="CarDetailView"),
    path("create/", PostCreateView.as_view(), name="CarCreate"),
    path("update/<int:pk>/", PostUpdateView.as_view(), name="CarUpdate"),
    path("delete/<int:pk>/", PostDeleteView.as_view(), name="CarDelete"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)