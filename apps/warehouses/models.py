from django.db import models


class Warehouse(models.Model):
    name = models.CharField('Наименование склада', max_length=64, db_index=True)
    address = models.CharField('Адрес', max_length=150, null=False)
    description = models.CharField('Описание', max_length=150, null=True, blank=True)
    useful_value = models.FloatField('Площадь', null=False)

    class Meta:
        # app_label = 'warehouses'
        verbose_name = 'Склад'
        verbose_name_plural = 'Склады'


class StorageType(models.Model):
    name = models.CharField('Наименование типа хранения', max_length=64, db_index=True)
    description = models.CharField('Описание', max_length=150, null=True, blank=True)
    storage_value = models.FloatField('Вместимость')
    warehouse = models.ManyToManyField('Warehouse', verbose_name='Склад')

    class Meta:
        # app_label = 'storage_type'
        verbose_name = 'Тип хранения'
        verbose_name_plural = 'Типы хранения'


class Cargo(models.Model):
    name = models.CharField('Наименование груза', max_length=64, db_index=True)
    description = models.CharField('Описание', max_length=150, null=True, blank=True)
    cargo_value = models.FloatField('Объем груза')
    cargo_weight = models.FloatField('Вес груза')
    storage_type = models.ForeignKey(StorageType, verbose_name='Тип хранения', on_delete=models.CASCADE)
    warehouse = models.ForeignKey(Warehouse, verbose_name='Склад', on_delete=models.CASCADE, null=True)

    class Meta:
        # app_label = 'cargo'
        verbose_name = 'Груз'
        verbose_name_plural = 'Грузы'


class Quotes(models.Model):
    author = models.CharField('Автор', max_length=150, db_index=True)
    quote = models.CharField('Описание', max_length=1000, null=True, blank=True)

    class Meta:
        # app_label = 'quotes'
        verbose_name = 'Цитата'
        verbose_name_plural = 'Цитаты'
