from django import forms
from .models import BlogPost

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'content', 'preview', 'is_published']
        help_texts = {
            'title': 'Заголовок статьи',
            'content': 'Основной текст',
            'preview': 'Картинка для статьи',
            'is_published': 'Если не выбрано — статья не видна'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
        self.fields['title'].widget.attrs.update({
            'placeholder': 'Например: Как выбрать квартиру',
            'autofocus': 'autofocus'
        })
