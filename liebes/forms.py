from django import forms
from .models import WardrobeItem

class LayerForm(forms.Form):
    top = forms.ModelChoiceField(queryset=WardrobeItem.objects.filter(category='top'), required=False)
    pants = forms.ModelChoiceField(queryset=WardrobeItem.objects.filter(category='pants'), required=False)
    shoes = forms.ModelChoiceField(queryset=WardrobeItem.objects.filter(category='shoes'), required=False)

class WardrobeItemForm(forms.ModelForm):
    class Meta:
        model = WardrobeItem
        fields = ['image', 'category']  # user will upload