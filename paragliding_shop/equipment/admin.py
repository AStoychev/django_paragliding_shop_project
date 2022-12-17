from django.contrib import admin

from paragliding_shop.equipment.models import Wings, Harness, Reserves, Instruments, Helmets


@admin.register(Wings, Harness, Reserves, Instruments, Helmets)
class UnitAdmin(admin.ModelAdmin):
    list_display = ("manufacturer", "price", "condition", "image_url", "user",)
    list_filter = ["manufacturer"]
    
