"""
URL configuration for information project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from RNI.views import *
URI = {
    "rab_info" : "rni/v2/queries/rab_info",
    "plmn_info" : "rni/v2/queries/plmn_info",
    "s1_bearer_info" : "rni/v2/queries/s1_bearer_info",
    "layer2_meas" : "rni/v2/queries/layer2_meas",
    "subscription" : "rni/v2/subscriptions",
    "test" : "rni/v2/test/<str:subscriptionId>",
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path(URI["rab_info"], rab_info),
    path(URI["plmn_info"], plmn_info),
    path(URI["s1_bearer_info"],s1_bearer_info),
    path(URI["layer2_meas"],layer2_meas),
    path(URI["subscription"],subscription),
    path('subscriptions/<str:content>',subscription_get),
    path(URI["test"],test)
]
