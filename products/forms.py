from django.forms import ModelForm
from .models import Product


class CreateProductForm(ModelForm):
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]