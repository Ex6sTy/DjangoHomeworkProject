from django import forms
from .models import Product, Category, ProductImage

# Константа для переиспользования в любых проверках
BANNED_WORDS = (
    'казино', 'криптовалюта', 'крипта', 'биржа',
    'дешево', 'бесплатно', 'обман', 'полиция', 'радар',
)

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'description', 'price', 'image', 'category')

    # Стилизация всех полей через __init__
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            css_class = 'form-control'
            if isinstance(field.widget, (forms.CheckboxInput, forms.ClearableFileInput)):
                css_class = 'form-check-input' if isinstance(field.widget, forms.CheckboxInput) else 'form-control-file'
            field.widget.attrs.update({'class': css_class})

    # Валидация на запрещённые слова
    def _contains_banned(self, value: str) -> bool:
        low = value.lower()
        return any(word in low for word in BANNED_WORDS)

    def clean_name(self):
        name = self.cleaned_data['name']
        if self._contains_banned(name):
            raise forms.ValidationError('Название содержит запрещённые слова.')
        return name

    def clean_description(self):
        desc = self.cleaned_data['description']
        if self._contains_banned(desc):
            raise forms.ValidationError('Описание содержит запрещённые слова.')
        return desc

    # Кастомная проверка цены
    def clean_price(self):
        price = self.cleaned_data['price']
        if price < 0:
            raise forms.ValidationError('Цена не может быть отрицательной.')
        return price

    # Проверка изображения
    def clean_image(self):
        image = self.cleaned_data.get('image')
        if image:
            if image.size > 5 * 1024 * 1024:
                raise forms.ValidationError('Размер изображения не должен превышать 5 МБ.')
            if image.content_type not in ('image/jpeg', 'image/png'):
                raise forms.ValidationError('Разрешены только файлы JPEG или PNG.')
        return image


class ProductImageForm(forms.ModelForm):
    class Meta:
        model  = ProductImage
        fields = ('image', 'alt')
        widgets = {
            'image': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'alt':   forms.TextInput(attrs={'class': 'form-control'}),
        }

ProductImageFormSet = forms.inlineformset_factory(
    Product, ProductImage, form=ProductImageForm,
    extra=1, can_delete=True
)