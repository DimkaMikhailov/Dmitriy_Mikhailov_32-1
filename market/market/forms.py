from django import forms
from goods.models import CatalogGroup, RATING_CHOICES


class AddProductForm(forms.Form):
    image = forms.FileField(label='Preview', required=False)
    title = forms.CharField(label='Title', min_length=3, max_length=64)
    price = forms.FloatField(label='Price')
    description = forms.CharField(label='Description', widget=forms.Textarea())
    count = forms.IntegerField(label='Amount', min_value=0)
    categories = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        choices=[(str(cat.id), cat.name) for cat in CatalogGroup.objects.all()]
    )


class AddProductReviewForm(forms.Form):
    rating = forms.ChoiceField(choices=RATING_CHOICES, widget=forms.RadioSelect(attrs={'class': 'rating'}))
    description = forms.CharField(label='Description', widget=forms.Textarea())

