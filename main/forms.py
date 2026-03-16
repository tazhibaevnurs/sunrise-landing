"""
Формы для заявок и админки.
"""
from django import forms
from .models import Application, SiteImage, FAQItem, Story, ContactInfo


class DonationApplicationForm(forms.ModelForm):
    """Форма заявки «Узнать о донорстве» (имя, телефон, возраст)."""
    class Meta:
        model = Application
        fields = ('name', 'phone', 'age')
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'interest-form-input',
                'placeholder': 'Ваше имя',
            }),
            'phone': forms.TextInput(attrs={
                'class': 'interest-form-input',
                'placeholder': 'Телефон',
                'type': 'tel',
            }),
            'age': forms.NumberInput(attrs={
                'class': 'interest-form-input',
                'placeholder': 'Возраст',
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.instance.application_type = Application.TYPE_DONATION


class SurrogacyApplicationForm(forms.ModelForm):
    """Форма заявки «Стать частью чуда» (имя, телефон, город)."""
    CITY_CHOICES = [
        ('', 'Ваш город'),
        ('tbilisi', 'Тбилиси'),
        ('bishkek', 'Бишкек'),
        ('other', 'Другой'),
    ]

    city = forms.ChoiceField(
        choices=CITY_CHOICES,
        required=False,
        widget=forms.Select(attrs={'class': 'interest-form-input appearance-none'}),
    )

    class Meta:
        model = Application
        fields = ('name', 'phone', 'city')
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'interest-form-input',
                'placeholder': 'Ваше имя',
            }),
            'phone': forms.TextInput(attrs={
                'class': 'interest-form-input',
                'placeholder': 'Телефон',
                'type': 'tel',
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.instance.application_type = Application.TYPE_SURROGACY


class StoryForm(forms.ModelForm):
    """Форма для создания/редактирования истории (админка и при необходимости на сайте)."""
    class Meta:
        model = Story
        fields = ('name', 'role', 'tagline', 'testimonial', 'photo', 'order')
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Имя'}),
            'role': forms.TextInput(attrs={'placeholder': 'донор, сурмама'}),
            'tagline': forms.TextInput(attrs={'placeholder': 'Краткая цитата в кавычках'}),
            'testimonial': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Полный текст отзыва'}),
        }


class ContactInfoForm(forms.ModelForm):
    """Форма редактирования контактных данных."""
    class Meta:
        model = ContactInfo
        fields = ('phone', 'address_1', 'address_2', 'email', 'footer_description', 'copyright_text')
        widgets = {
            'phone': forms.TextInput(attrs={'placeholder': '+7 (900) 000-00-00'}),
            'address_1': forms.TextInput(attrs={'placeholder': 'Тбилиси, Грузия'}),
            'address_2': forms.TextInput(attrs={'placeholder': 'Бишкек, Кыргызстан'}),
            'footer_description': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Лицензированное агентство...'}),
            'copyright_text': forms.TextInput(attrs={'placeholder': '© 2016 - 2026 Sunrise Family'}),
        }


class SiteImageForm(forms.ModelForm):
    """Форма редактирования изображения сайта (для админки/кастомных вью)."""
    class Meta:
        model = SiteImage
        fields = ('slug', 'image', 'alt', 'url_override')


class FAQItemForm(forms.ModelForm):
    """Форма для вопроса FAQ."""
    class Meta:
        model = FAQItem
        fields = ('question', 'answer', 'order')
