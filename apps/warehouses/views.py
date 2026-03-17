from django.urls import reverse_lazy

from .models import Warehouse, StorageType, Cargo
from .forms import WarehouseForm, StorageTypeForm, CargoForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import render

import logging

logger = logging.getLogger(__name__)


def index_view(request):

    return render(
        request,
        "warehouses/index.html",
        # context,
    )


class WarehouseListView(ListView):
    model = Warehouse


class WarehouseDetailView(DetailView):
    model = Warehouse


class WarehouseCreateView(CreateView):
    model = Warehouse
    form_class = WarehouseForm
    success_url = reverse_lazy('warehouses:warehouse_list')

    def form_valid(self, form):
        data = form.cleaned_data
        return super().form_valid(form)


class WarehouseTypeUpdateView(UpdateView):
    model = Warehouse
    fields = ('name', 'description')
    success_url = reverse_lazy('warehouses:warehouse_list')


class WarehouseDeleteView(DeleteView):
    model = Warehouse
    success_url = reverse_lazy('warehouses:warehouse_list')


class StorageTypeListView(ListView):
    model = StorageType


class StorageTypeDetailView(DetailView):
    model = StorageType


class StorageTypeCreateView(CreateView):
    model = StorageType
    form_class = StorageTypeForm
    success_url = reverse_lazy('warehouses:storagetype_list')

    def form_valid(self, form):
        data = form.cleaned_data
        return super().form_valid(form)


class StorageTypeUpdateView(UpdateView):
    model = StorageType
    fields = ('name', 'description')
    success_url = reverse_lazy('warehouses:storagetype_list')


class StorageTypeDeleteView(DeleteView):
    model = StorageType
    success_url = reverse_lazy('warehouses:storagetype_list')


class CargoListView(ListView):
    model = Cargo


class CargoDetailView(DetailView):
    model = Cargo


class CargoCreateView(CreateView):
    model = Cargo
    form_class = CargoForm
    success_url = reverse_lazy('warehouses:cargo_list')

    def form_valid(self, form):
        data = form.cleaned_data
        return super().form_valid(form)


class CargoUpdateView(UpdateView):
    model = Cargo
    fields = ('name', 'description', 'cargo_value', 'cargo_weight')
    success_url = reverse_lazy('warehouses:cargo_list')


class CargoDeleteView(DeleteView):
    model = Cargo
    success_url = reverse_lazy('warehouses:cargo_list')
