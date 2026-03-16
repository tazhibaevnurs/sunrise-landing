"""
Представления лендинга Sunrise Family.
"""
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_protect

from .models import SiteImage, FAQItem, Story, ContactInfo
from .forms import DonationApplicationForm, SurrogacyApplicationForm


def get_images_dict():
    """Возвращает словарь изображений по slug для шаблона."""
    images = {}
    for obj in SiteImage.objects.all():
        url = obj.get_url()
        if url:
            images[obj.slug] = {'url': url, 'alt': obj.alt or ''}
    return images


@require_http_methods(['GET', 'POST'])
@csrf_protect
def home(request):
    """Главная страница с формами заявок и динамическими данными (фото, FAQ)."""
    images = get_images_dict()
    faq_list = list(FAQItem.objects.all())
    story_list = list(Story.objects.all())
    contact = ContactInfo.get_default()

    donation_form = DonationApplicationForm(request.POST or None, prefix='donation')
    surrogacy_form = SurrogacyApplicationForm(request.POST or None, prefix='surrogacy')

    if request.method == 'POST':
        form_id = request.POST.get('form_id', '')
        if form_id == 'donation':
            if donation_form.is_valid():
                donation_form.save()
                messages.success(request, 'Заявка на консультацию по донорству отправлена. Мы свяжемся с вами.')
                return redirect(request.path + '#donation')
            messages.error(request, 'Проверьте поля формы и попробуйте снова.')
        elif form_id == 'surrogacy':
            if surrogacy_form.is_valid():
                surrogacy_form.save()
                messages.success(request, 'Заявка на консультацию по суррогатному материнству отправлена. Мы свяжемся с вами.')
                return redirect(request.path + '#surrogacy')
            messages.error(request, 'Проверьте поля формы и попробуйте снова.')

    return render(request, 'main/home.html', {
        'images': images,
        'faq_list': faq_list,
        'story_list': story_list,
        'contact': contact,
        'donation_form': donation_form,
        'surrogacy_form': surrogacy_form,
    })


@require_http_methods(['GET', 'POST'])
@csrf_protect
def donation_page(request):
    """Страница «Донорство яйцеклеток» с формой заявки."""
    images = get_images_dict()
    contact = ContactInfo.get_default()
    donation_form = DonationApplicationForm(request.POST or None)

    if request.method == 'POST' and donation_form.is_valid():
        donation_form.save()
        messages.success(request, 'Заявка на консультацию по донорству отправлена. Мы свяжемся с вами.')
        return redirect('donation')

    return render(request, 'main/donation.html', {
        'images': images,
        'contact': contact,
        'donation_form': donation_form,
    })


@require_http_methods(['GET', 'POST'])
@csrf_protect
def surrogacy_page(request):
    """Страница «Суррогатное материнство» с формой заявки."""
    images = get_images_dict()
    contact = ContactInfo.get_default()
    surrogacy_form = SurrogacyApplicationForm(request.POST or None)

    if request.method == 'POST' and surrogacy_form.is_valid():
        surrogacy_form.save()
        messages.success(request, 'Заявка на консультацию по суррогатному материнству отправлена. Мы свяжемся с вами.')
        return redirect('surrogacy')

    return render(request, 'main/surrogacy.html', {
        'images': images,
        'contact': contact,
        'surrogacy_form': surrogacy_form,
    })
