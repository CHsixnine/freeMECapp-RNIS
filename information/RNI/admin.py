from django.contrib import admin
from RNI.models import RabInfo,S1bearerinfo,Layer2meas,Subscription
# Register your models here.
admin.site.register(RabInfo)
admin.site.register(S1bearerinfo)
admin.site.register(Layer2meas)
admin.site.register(Subscription)