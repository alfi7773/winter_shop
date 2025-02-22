from importlib.metadata import requires

from django import forms

from board.models import *
from django.db.models.fields import DecimalField



class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 
                  'decription', 
                #   'image', 
                  'price', 
                  'category',
                  'type',
                  'tags',
                  'price',
                  'at_category',
                  'author'
                  )