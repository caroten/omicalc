from django.contrib import admin
from .models import PrintFormat, CirculationLimit, InkFaceBack, WasteRatio


admin.site.register(PrintFormat)
admin.site.register(CirculationLimit)
admin.site.register(InkFaceBack)
admin.site.register(WasteRatio)
