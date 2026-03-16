"""
Модели для лендинга Sunrise Family.
"""
from django.db import models


class Application(models.Model):
    """Заявка с сайта (донорство или суррогатное материнство)."""
    TYPE_DONATION = 'donation'
    TYPE_SURROGACY = 'surrogacy'
    TYPE_CHOICES = [
        (TYPE_DONATION, 'Донорство яйцеклеток'),
        (TYPE_SURROGACY, 'Суррогатное материнство'),
    ]

    application_type = models.CharField(
        'Тип заявки',
        max_length=20,
        choices=TYPE_CHOICES,
    )
    name = models.CharField('Имя', max_length=255)
    phone = models.CharField('Телефон', max_length=50)
    age = models.PositiveSmallIntegerField('Возраст', null=True, blank=True)
    city = models.CharField('Город', max_length=100, blank=True)
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
    is_processed = models.BooleanField('Обработана', default=False)

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.get_application_type_display()} — {self.name} ({self.phone})'


class SiteImage(models.Model):
    """Фотографии/изображения сайта, управляемые из админки."""
    SLUG_HERO = 'hero'
    SLUG_ABOUT = 'about'
    SLUG_DONATION = 'donation'
    SLUG_SURROGACY = 'surrogacy'
    SLUG_STORY_1 = 'story_1'
    SLUG_STORY_2 = 'story_2'
    SLUG_CHOICES = [
        (SLUG_HERO, 'Главный баннер (Hero)'),
        (SLUG_ABOUT, 'Блок «О нас»'),
        (SLUG_DONATION, 'Блок «Донорство»'),
        (SLUG_SURROGACY, 'Блок «Суррогатное материнство»'),
        (SLUG_STORY_1, 'История 1 (Елена)'),
        (SLUG_STORY_2, 'История 2 (Мария)'),
    ]

    slug = models.SlugField(
        'Код',
        max_length=50,
        unique=True,
        choices=SLUG_CHOICES,
        help_text='Уникальный код изображения на сайте',
    )
    image = models.ImageField('Изображение', upload_to='site_images/', blank=True, null=True)
    alt = models.CharField('Подпись (alt)', max_length=255, blank=True)
    url_override = models.URLField(
        'Внешняя ссылка (если не загружать файл)',
        max_length=500,
        blank=True,
        help_text='Если указано, будет использоваться вместо загруженного файла',
    )

    class Meta:
        verbose_name = 'Изображение сайта'
        verbose_name_plural = 'Изображения сайта'

    def __str__(self):
        return self.get_slug_display()

    def get_url(self):
        """Возвращает URL изображения: либо url_override, либо загруженный файл."""
        if self.url_override:
            return self.url_override
        if self.image:
            return self.image.url
        return None


class Story(models.Model):
    """История участника программы (отзыв) для блока «Личные истории»."""
    name = models.CharField('Имя', max_length=255)
    role = models.CharField('Роль', max_length=100, help_text='Например: донор, сурмама')
    tagline = models.CharField('Краткая цитата', max_length=300, help_text='Короткая фраза в кавычках')
    testimonial = models.TextField('Текст отзыва')
    photo = models.ImageField('Фото', upload_to='stories/', blank=True, null=True)
    order = models.PositiveIntegerField('Порядок', default=0)

    class Meta:
        verbose_name = 'История'
        verbose_name_plural = 'Истории'
        ordering = ['order']

    def __str__(self):
        return f'{self.name}, {self.role}'


class ContactInfo(models.Model):
    """Контактные данные сайта (футер, один набор на сайт)."""
    phone = models.CharField('Телефон', max_length=50, blank=True)
    address_1 = models.CharField('Адрес 1', max_length=255, blank=True, help_text='Например: Тбилиси, Грузия')
    address_2 = models.CharField('Адрес 2', max_length=255, blank=True, help_text='Например: Бишкек, Кыргызстан')
    email = models.EmailField('Email', blank=True)
    footer_description = models.TextField(
        'Описание в футере',
        blank=True,
        help_text='Текст под логотипом в подвале',
    )
    copyright_text = models.CharField(
        'Текст копирайта',
        max_length=255,
        blank=True,
        help_text='Например: © 2016 - 2026 Sunrise Family • Сделано с любовью и заботой о жизни',
    )

    class Meta:
        verbose_name = 'Контактные данные'
        verbose_name_plural = 'Контактные данные'

    def __str__(self):
        return self.phone or 'Контактные данные'

    @classmethod
    def get_default(cls):
        """Возвращает единственную запись или None (для шаблонных данных)."""
        return cls.objects.first()


class FAQItem(models.Model):
    """Вопрос-ответ для блока FAQ."""
    question = models.CharField('Вопрос', max_length=500)
    answer = models.TextField('Ответ')
    order = models.PositiveIntegerField('Порядок', default=0)

    class Meta:
        verbose_name = 'Вопрос FAQ'
        verbose_name_plural = 'FAQ'
        ordering = ['order']

    def __str__(self):
        return self.question[:80] + ('…' if len(self.question) > 80 else '')
