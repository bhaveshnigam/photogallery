from django.conf.urls import url
from django.views.decorators.cache import cache_page
from django.views.generic import RedirectView
from django.urls import reverse_lazy
from django.conf import settings

from .views import PhotoListView, PhotoDetailView, GalleryListView, \
    GalleryDetailView, PhotoArchiveIndexView, PhotoDateDetailView, PhotoDayArchiveView, \
    PhotoYearArchiveView, PhotoMonthArchiveView, GalleryArchiveIndexView, GalleryYearArchiveView, \
    GalleryDateDetailView, GalleryDayArchiveView, GalleryMonthArchiveView

"""NOTE: the url names are changing. In the long term, I want to remove the 'pl-'
prefix on all urls, and instead rely on an application namespace 'photologue'.

At the same time, I want to change some URL patterns, e.g. for pagination. Changing the urls
twice within a few releases, could be confusing, so instead I am updating URLs bit by bit.

The new style will coexist with the existing 'pl-' prefix for a couple of releases.

"""


app_name = 'photologue'
urlpatterns = [
    url(r'^gallery/(?P<year>\d{4})/(?P<month>[0-9]{2})/(?P<day>\w{1,2})/(?P<slug>[\-\d\w]+)/$',
        cache_page(settings.DEFAULT_CACHE_TIMEOUT)(GalleryDateDetailView.as_view(month_format='%m')),
        name='gallery-detail'),
    url(r'^gallery/(?P<year>\d{4})/(?P<month>[0-9]{2})/(?P<day>\w{1,2})/$',
        cache_page(settings.DEFAULT_CACHE_TIMEOUT)(GalleryDayArchiveView.as_view(month_format='%m')),
        name='gallery-archive-day'),
    url(r'^gallery/(?P<year>\d{4})/(?P<month>[0-9]{2})/$',
        cache_page(settings.DEFAULT_CACHE_TIMEOUT)(GalleryMonthArchiveView.as_view(month_format='%m')),
        name='gallery-archive-month'),
    url(r'^gallery/(?P<year>\d{4})/$',
        cache_page(settings.DEFAULT_CACHE_TIMEOUT)(GalleryYearArchiveView.as_view()),
        name='pl-gallery-archive-year'),
    url(r'^gallery/$',
        cache_page(settings.DEFAULT_CACHE_TIMEOUT)(GalleryArchiveIndexView.as_view()),
        name='pl-gallery-archive'),
    url(r'^$',
        RedirectView.as_view(
            url=reverse_lazy('photologue:pl-gallery-archive'), permanent=True),
        name='pl-photologue-root'),
    url(r'^gallery/(?P<slug>[\-\d\w]+)/$',
        cache_page(settings.DEFAULT_CACHE_TIMEOUT)(GalleryDetailView.as_view()), name='pl-gallery'),
    url(r'^gallerylist/$',
        cache_page(settings.DEFAULT_CACHE_TIMEOUT)(GalleryListView.as_view()),
        name='gallery-list'),

    url(r'^photo/(?P<year>\d{4})/(?P<month>[0-9]{2})/(?P<day>\w{1,2})/(?P<slug>[\-\d\w]+)/$',
        cache_page(settings.DEFAULT_CACHE_TIMEOUT)(PhotoDateDetailView.as_view(month_format='%m')),
        name='photo-detail'),
    url(r'^photo/(?P<year>\d{4})/(?P<month>[0-9]{2})/(?P<day>\w{1,2})/$',
        cache_page(settings.DEFAULT_CACHE_TIMEOUT)(PhotoDayArchiveView.as_view(month_format='%m')),
        name='photo-archive-day'),
    url(r'^photo/(?P<year>\d{4})/(?P<month>[0-9]{2})/$',
        cache_page(settings.DEFAULT_CACHE_TIMEOUT)(PhotoMonthArchiveView.as_view(month_format='%m')),
        name='photo-archive-month'),
    url(r'^photo/(?P<year>\d{4})/$',
        cache_page(settings.DEFAULT_CACHE_TIMEOUT)(PhotoYearArchiveView.as_view()),
        name='pl-photo-archive-year'),
    url(r'^photo/$',
        cache_page(settings.DEFAULT_CACHE_TIMEOUT)(PhotoArchiveIndexView.as_view()),
        name='pl-photo-archive'),

    url(r'^photo/(?P<slug>[\-\d\w]+)/$',
        cache_page(settings.DEFAULT_CACHE_TIMEOUT)(PhotoDetailView.as_view()),
        name='pl-photo'),
    url(r'^photolist/$',
        cache_page(settings.DEFAULT_CACHE_TIMEOUT)(PhotoListView.as_view()),
        name='photo-list'),
]
