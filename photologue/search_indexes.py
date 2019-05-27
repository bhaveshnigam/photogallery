from haystack import indexes

from photologue.models import Photopath


class PhotopathIndexes(indexes.SearchIndex, indexes.Indexable):
  text = indexes.CharField(document=True, use_template=True)
  name = indexes.CharField(model_attr='name')
  path = indexes.CharField(model_attr='path')
  content_auto = indexes.EdgeNgramField()

  def get_model(self):
    return Photopath

  def prepare_content_auto(self, obj):
    return '%s' % obj.path

  def get_result_json(self, obj):
    return {
        'path': obj.path,
        'name': obj.name,
        'id': obj.pk,
    }

  def index_queryset(self, using=None):
    return self.get_model().objects.filter()
