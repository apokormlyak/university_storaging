from django.test import TestCase
from rest_framework import status
from ..models import Warehouse, StorageType, Cargo
import logging

logger = logging.getLogger(__name__)


class WarehouseListViewTestCase(TestCase):

    def setUp(self):
        self.url = '/warehouses/warehouse_list/'

    def tearDown(self):
        logger.info('Test WarehouseListView finished')

    def test_status_code(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_warehouse_list_is_not_empty(self):
        warehouse = Warehouse.objects.create(
            name='test',
            address='test',
            useful_value=100
        )
        response = self.client.get(self.url)
        context = response.context['warehouse_list']
        assert len(context) == 1

    def test_warehouse_list_is_empty(self):
        response = self.client.get(self.url)
        context = response.context['warehouse_list']
        assert len(context) == 0


class WarehouseDetailViewTestCase(TestCase):

    def setUp(self):
        self.url = '/warehouses/warehouse_detail/'

    def tearDown(self):
        logger.info('Test WarehouseDetailView finished')

    def test_status_code_not_found(self):
        wh_id = 'test'
        response = self.client.get(self.url + f'{wh_id}/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_status_code(self):
        warehouse = Warehouse.objects.create(
            name='test',
            address='test',
            useful_value=100
        )
        wh_id = warehouse.pk
        response = self.client.get(self.url + f'{wh_id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_warehouse_list_context(self):
        warehouse = Warehouse.objects.create(
            name='test',
            address='test',
            useful_value=100
        )
        wh_id = warehouse.pk
        response = self.client.get(self.url + f'{wh_id}/')
        context = response.context
        self.assertIn('warehouse', context)


class StorageTypeListViewTestCase(TestCase):

    def setUp(self):
        self.url = '/warehouses/storagetype_list/'

    def tearDown(self):
        logger.info('Test StorageTypeListView finished')

    def test_status_code(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_storagetype_list_is_not_empty(self):
        warehouse = Warehouse.objects.create(
            name='test',
            address='test',
            useful_value=100
        )
        storage_type = StorageType.objects.create(
            name='st_test',
            storage_value=100,
        )
        storage_type.warehouse.add(warehouse)
        response = self.client.get(self.url)
        context = response.context['storagetype_list']
        assert len(context) == 1

    def test_storagetype_list_is_empty(self):
        response = self.client.get(self.url)
        context = response.context['storagetype_list']
        assert len(context) == 0


class StorageTypeDetailViewTestCase(TestCase):

    def setUp(self):
        self.url = '/warehouses/storagetype_detail/'

    def tearDown(self):
        logger.info('Test StorageTypeDetailView finished')

    def test_status_code_not_found(self):
        storage_id = 'test'
        response = self.client.get(self.url + f'{storage_id}/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_status_code(self):
        warehouse = Warehouse.objects.create(
            name='test',
            address='test',
            useful_value=100
        )
        storage_type = StorageType.objects.create(
            name='st_test',
            storage_value=100,
        )
        storage_type.warehouse.add(warehouse)
        storage_id = storage_type.pk
        response = self.client.get(self.url + f'{storage_id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_storagetype_context(self):
        warehouse = Warehouse.objects.create(
            name='test',
            address='test',
            useful_value=100
        )
        storage_type = StorageType.objects.create(
            name='st_test',
            storage_value=100,
        )
        storage_type.warehouse.add(warehouse)
        storage_id = storage_type.pk
        response = self.client.get(self.url + f'{storage_id}/')
        context = response.context
        self.assertIn('storagetype', context)


class CargoListViewTestCase(TestCase):

    def setUp(self):
        self.url = '/warehouses/cargo_list/'

    def tearDown(self):
        logger.info('Test CargoListView finished')

    def test_status_code(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cargo_list_is_not_empty(self):
        warehouse = Warehouse.objects.create(
            name='test',
            address='test',
            useful_value=100
        )
        storage_type = StorageType.objects.create(
            name='st_test',
            storage_value=100,
        )
        storage_type.warehouse.add(warehouse)
        cargo = Cargo.objects.create(
            name='test',
            cargo_value=100,
            cargo_weight=100,
            storage_type=storage_type,
            warehouse=warehouse
        )
        response = self.client.get(self.url)
        context = response.context['cargo_list']
        assert len(context) == 1

    def test_cargo_list_is_empty(self):
        response = self.client.get(self.url)
        context = response.context['cargo_list']
        assert len(context) == 0


class CargoDetailViewTestCase(TestCase):

    def setUp(self):
        self.url = '/warehouses/cargo_detail/'

    def tearDown(self):
        logger.info('Test CargoTypeDetailView finished')

    def test_status_code_not_found(self):
        cargo_id = 'test'
        response = self.client.get(self.url + f'{cargo_id}/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_status_code(self):
        warehouse = Warehouse.objects.create(
            name='test',
            address='test',
            useful_value=100
        )
        storage_type = StorageType.objects.create(
            name='st_test',
            storage_value=100,
        )
        storage_type.warehouse.add(warehouse)
        cargo = Cargo.objects.create(
            name='test',
            cargo_value=100,
            cargo_weight=100,
            storage_type=storage_type,
            warehouse=warehouse
        )
        cargo_id = cargo.pk
        response = self.client.get(self.url + f'{cargo_id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cargo_context(self):
        warehouse = Warehouse.objects.create(
            name='test',
            address='test',
            useful_value=100
        )
        storage_type = StorageType.objects.create(
            name='st_test',
            storage_value=100,
        )
        storage_type.warehouse.add(warehouse)
        cargo = Cargo.objects.create(
            name='test',
            cargo_value=100,
            cargo_weight=100,
            storage_type=storage_type,
            warehouse=warehouse
        )
        cargo_id = cargo.pk
        response = self.client.get(self.url + f'{cargo_id}/')
        context = response.context
        self.assertIn('cargo', context)
