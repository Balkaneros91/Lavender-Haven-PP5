from django import forms
from .models import Category, Article


class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        self.fields['image'].label = False
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
