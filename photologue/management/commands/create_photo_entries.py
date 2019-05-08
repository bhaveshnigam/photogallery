import datetime
import time
from itertools import chain

from django.contrib.sites.models import Site
from django.core.management import BaseCommand
import pathlib

from django.utils import timezone
from django.utils.text import slugify

from photologue.models import Gallery, Photo


class Command(BaseCommand):
    requires_model_validation = True
    can_import_settings = True

    def add_arguments(self, parser):
        parser.add_argument('dir_path',
                            type=str,
                            help='Directory path to iterate and create entries in the system')

    def handle(self, *args, **options):
      Photo.objects.all().delete()
      Gallery.objects.all().delete()

      dir_path = options['dir_path']

      dir_path = pathlib.Path(dir_path).expanduser()

      index = 0
      for file in chain(dir_path.glob('**/*.jpg'), dir_path.glob('**/*.jpeg')):
        index += 1
        if str(file.parent.name).startswith('.'):
          continue
        if str(file.parent.name).startswith('cache'):
          continue
        print(file)
        time_obj = time.localtime(file.stat().st_ctime)

        file_created_date = datetime.datetime(
          year=time_obj.tm_year, month=time_obj.tm_mon, day=time_obj.tm_mday,
          hour=time_obj.tm_hour, minute=time_obj.tm_min, second=time_obj.tm_sec,
          tzinfo=timezone.now().tzinfo
        )

        slug = slugify(file.name)
        if Photo.objects.filter(slug=slug).exists():
          slug += '-%s' % index

        photo, _ = Photo.objects.get_or_create(
          image_path=str(file),
          title=file.name,
          date_added=file_created_date,
          caption=str(file),
          slug=slug
        )
        photo.sites.add(Site.objects.get_current())

        time_obj = time.localtime(file.parent.stat().st_ctime)
        gallery_created_date = datetime.datetime(
          year=time_obj.tm_year, month=time_obj.tm_mon, day=time_obj.tm_mday,
          hour=time_obj.tm_hour, minute=time_obj.tm_min, second=time_obj.tm_sec,
          tzinfo=timezone.now().tzinfo
        )
        if gallery_created_date > file_created_date:
          gallery_created_date = file_created_date

        title = file.parent.name
        gallery = Gallery.objects.filter(title=title).first()
        if not gallery:
          slug = slugify(file.parent.name)
          if Gallery.objects.filter(slug=slug).exists():
            slug += '-%s' % index

          gallery, created = Gallery.objects.get_or_create(
            title=file.parent.name,
            slug=slug,
            defaults={
              'date_added': gallery_created_date,
              'description': str(file.parent),
            }
          )
          if not created:
            gallery.date_added = gallery_created_date
            gallery.save()

          gallery.sites.add(Site.objects.get_current())

        gallery.photos.add(photo)
