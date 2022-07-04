"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
import main.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('survey', main.views.survey, name='survey'),
    path('result1/', main.views.result1, name='result1'),
    path('result2/', main.views.result2, name='result2'),
    path('result3/', main.views.result3, name='result3'),
    path('result4/', main.views.result4, name='result4'),
    path('result5/', main.views.result5, name='result5'),
    path('result6/', main.views.result6, name='result6'),
    path('result7/', main.views.result7, name='result7'),
    path('result8/', main.views.result8, name='result8'),
    path('result9/', main.views.result9, name='result9'),
    path('result10/', main.views.result10, name='result10'),
]
