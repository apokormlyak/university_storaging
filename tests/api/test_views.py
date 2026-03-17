import pytest
import logging
from rest_framework.test import APIClient
from rest_framework import status
from apps.warehouses.models import Warehouse, StorageType, Cargo

logger = logging.getLogger(__name__)


class TestWarehouseListView:
    URL = '/warehouses/warehouse_list/'

    @pytest.mark.django_db
    def test_status_code(self, authenticated_client: APIClient):
        response = authenticated_client.get(self.URL)
        assert response.status_code == status.HTTP_200_OK

    @pytest.mark.django_db
    def test_warehouse_list_is_not_empty(self, authenticated_client: APIClient):
        warehouse = Warehouse.objects.create(
            name='test',
            address='test',
            useful_value=100
        )
        response = authenticated_client.get(self.URL)
        context = response.context['warehouse_list']
        assert len(context) == 1

    @pytest.mark.django_db
    def test_warehouse_list_is_empty(self, authenticated_client: APIClient):
        response = authenticated_client.get(self.URL)
        context = response.context['warehouse_list']
        assert len(context) == 0


class TestWarehouseDetailView:
    URL = '/warehouses/warehouse_detail/'

    @pytest.mark.django_db
    def test_status_code_not_found(self, authenticated_client: APIClient):
        wh_id = 'test'
        response = authenticated_client.get(self.URL + f'{wh_id}/')
        assert response.status_code == status.HTTP_404_NOT_FOUND

    @pytest.mark.django_db
    def test_status_code(self, authenticated_client: APIClient):
        warehouse = Warehouse.objects.create(
            name='test',
            address='test',
            useful_value=100
        )
        wh_id = warehouse.pk
        response = authenticated_client.get(self.URL + f'{wh_id}/')
        assert response.status_code == status.HTTP_200_OK

    @pytest.mark.django_db
    def test_warehouse_list_context(self, authenticated_client: APIClient):
        warehouse = Warehouse.objects.create(
            name='test',
            address='test',
            useful_value=100
        )
        wh_id = warehouse.pk
        response = authenticated_client.get(self.URL + f'{wh_id}/')
        context = response.context
        assert 'warehouse' in context


class TestStorageTypeListView:
    URL = '/warehouses/storagetype_list/'

    @pytest.mark.django_db
    def test_status_code(self, authenticated_client: APIClient):
        response = authenticated_client.get(self.URL)
        assert response.status_code == status.HTTP_200_OK

    @pytest.mark.django_db
    def test_storagetype_list_is_not_empty(self, authenticated_client: APIClient):
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
        response = authenticated_client.get(self.URL)
        context = response.context['storagetype_list']
        assert len(context) == 1

    @pytest.mark.django_db
    def test_storagetype_list_is_empty(self, authenticated_client: APIClient):
        response = authenticated_client.get(self.URL)
        context = response.context['storagetype_list']
        assert len(context) == 0


class TestStorageTypeDetailView:
    URL = '/warehouses/storagetype_detail/'

    def tearDown(self):
        logger.info('Test StorageTypeDetailView finished')

    @pytest.mark.django_db
    def test_status_code_not_found(self, authenticated_client: APIClient):
        storage_id = 'test'
        response = authenticated_client.get(self.URL + f'{storage_id}/')
        assert response.status_code == status.HTTP_404_NOT_FOUND

    @pytest.mark.django_db
    def test_status_code(self, authenticated_client: APIClient):
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
        response = authenticated_client.get(self.URL + f'{storage_id}/')
        assert response.status_code == status.HTTP_200_OK

    @pytest.mark.django_db
    def test_storagetype_context(self, authenticated_client: APIClient):
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
        response = authenticated_client.get(self.URL + f'{storage_id}/')
        context = response.context
        assert 'storagetype' in context


class TestCargoListView:
    URL = '/warehouses/cargo_list/'

    @pytest.mark.django_db
    def test_status_code(self, authenticated_client: APIClient):
        response = authenticated_client.get(self.URL)
        assert response.status_code == status.HTTP_200_OK

    @pytest.mark.django_db
    def test_cargo_list_is_not_empty(self, authenticated_client: APIClient):
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
        response = authenticated_client.get(self.URL)
        context = response.context['cargo_list']
        assert len(context) == 1

    @pytest.mark.django_db
    def test_cargo_list_is_empty(self, authenticated_client: APIClient):
        response = authenticated_client.get(self.URL)
        context = response.context['cargo_list']
        assert len(context) == 0


class TestCargoDetailView:
    URL = '/warehouses/cargo_detail/'

    @pytest.mark.django_db
    def test_status_code_not_found(self, authenticated_client: APIClient):
        cargo_id = 'test'
        response = authenticated_client.get(self.URL + f'{cargo_id}/')
        assert response.status_code == status.HTTP_404_NOT_FOUND

    @pytest.mark.django_db
    def test_status_code(self, authenticated_client: APIClient):
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
        response = authenticated_client.get(self.URL + f'{cargo_id}/')
        assert response.status_code == status.HTTP_200_OK

    @pytest.mark.django_db
    def test_cargo_context(self, authenticated_client: APIClient):
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
        response = authenticated_client.get(self.URL + f'{cargo_id}/')
        context = response.context
        assert 'cargo' in context

