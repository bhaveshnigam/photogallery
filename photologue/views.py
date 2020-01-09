from django.http import JsonResponse, HttpResponseRedirect, Http404
from django.views.generic.base import View
from django.views.generic.dates import ArchiveIndexView, DateDetailView, DayArchiveView, MonthArchiveView, \
    YearArchiveView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from haystack.query import SearchQuerySet

from .models import Photo, Gallery, Photopath


# Gallery views.


class GalleryListView(ListView):
    queryset = Gallery.objects.is_public()
    paginate_by = 20


class GalleryDetailView(DetailView):
    queryset = Gallery.objects.is_public()


class GalleryDateView(object):
    queryset = Gallery.objects.is_public()
    date_field = 'date_added'
    allow_empty = True


class GalleryDateDetailView(GalleryDateView, DateDetailView):
    pass


class GalleryArchiveIndexView(GalleryDateView, ArchiveIndexView):
    pass


class GalleryDayArchiveView(GalleryDateView, DayArchiveView):
    pass


class GalleryMonthArchiveView(GalleryDateView, MonthArchiveView):
    pass


class GalleryYearArchiveView(GalleryDateView, YearArchiveView):
    make_object_list = True

# Photo views.


class PhotoListView(ListView):
    queryset = Photo.objects.is_public()
    paginate_by = 1000


class PhotoDetailView(DetailView):
    queryset = Photo.objects.is_public()


class PhotoDateView(object):
    queryset = Photo.objects.is_public()
    date_field = 'date_added'
    allow_empty = True


class PhotoDateDetailView(PhotoDateView, DateDetailView):
    pass


class PhotoArchiveIndexView(PhotoDateView, ArchiveIndexView):
    pass


class PhotoDayArchiveView(PhotoDateView, DayArchiveView):
    pass


class PhotoMonthArchiveView(PhotoDateView, MonthArchiveView):
    pass


class PhotoYearArchiveView(PhotoDateView, YearArchiveView):
    make_object_list = True



class AutocompleteQuery(View):
  http_method_names = ['get']

  def get(self, request, *args, **kwargs):
    query = request.GET.get('q', '')
    if not query:
      return JsonResponse(list(), safe=False)

    query = query.strip().split('.')
    if query:
      query = query[0]

    sqs = SearchQuerySet().autocomplete(
        content_auto__icontains=query.strip(),
    )
    sqs = sqs[:100]

    suggestions = []
    for result in sqs:
        suggestions.append(result.searchindex.get_result_json(result))

    return JsonResponse(list(suggestions), safe=False)


class DownloadPhoto(View):
  http_method_names = ['get']

  def get(self, request, *args, **kwargs):
      photopath = Photopath.objects.filter(id=self.kwargs.get('pk')).first()
      if not photopath:
          raise Http404
      return HttpResponseRedirect(
          '/media' + photopath.path
      )
