from django.contrib import admin
from .models import Warehouse, StorageType, Cargo


@admin.register(Warehouse)
class WarehouseAdmin(admin.ModelAdmin):
    pass


@admin.register(StorageType)
class StorageTypeLineAdmin(admin.ModelAdmin):
    pass


@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    pass
