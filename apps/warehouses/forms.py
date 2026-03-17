from django import forms
from .models import Warehouse, StorageType, Cargo
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class WarehouseForm(forms.ModelForm):
    class Meta:
        model = Warehouse
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save warehouse'))


class StorageTypeForm(forms.ModelForm):
    class Meta:
        model = StorageType
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save storage type'))


class CargoForm(forms.ModelForm):
    class Meta:
        model = Cargo
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save cargo'))
