from django.contrib import admin

from .models import Device,Sensor
# Register your models here.

class DeviceAdmin(admin.ModelAdmin):
        list_display = ('name', 'on', 'signal_on', 'signal_off')

class SensorAdmin(admin.ModelAdmin):
	list_display = ('name', 'signal')

admin.site.register(Device, DeviceAdmin)
admin.site.register(Sensor, SensorAdmin)
