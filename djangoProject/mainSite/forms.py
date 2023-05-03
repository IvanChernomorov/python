from .models import Songs,Artists,Albums
from django.forms import ModelForm,TextInput,NumberInput,DateInput,	ModelChoiceField

class ArtistsForm(ModelForm):
    class Meta:
        model=Artists
        fields=["pseudonym","genre","formed_in","country"]
        widgets={
            "pseudonym": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите псевдоним'
            }),
            "genre": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите жанр'
            }),
            "formed_in": DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите дату начала карьеры'
            }),
			"country": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите страну исполнителя'
            }),
        }

class AlbumsForm(ModelForm):
    class Meta:
        model=Albums
        id_ar = ModelChoiceField(queryset=Artists.objects.all())
        fields=["title","id_ar", "release_date","label"]
        widgets={
             "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название альбома'
            }),
            "release_date": DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите дату выхода альбома'
            }),
			"label": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите лейбл'
            })}

class SongsForm(ModelForm):
    class Meta:
        model=Songs

        id_al = ModelChoiceField(queryset=Albums.objects.all())
        id_ar = ModelChoiceField(queryset=Artists.objects.all())
        fields=["title","id_al","id_ar","length"]
        widgets={
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название песни'
            }),
            "length": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите продолжительность песни в секундах'
            })}


