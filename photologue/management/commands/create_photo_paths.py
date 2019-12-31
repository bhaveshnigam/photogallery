import datetime
import time
from itertools import chain

from django.contrib.sites.models import Site
from django.core.management import BaseCommand, call_command
import pathlib

from django.utils import timezone
from django.utils.text import slugify

from photologue.models import Gallery, Photo, Photopath


class Command(BaseCommand):
    requires_model_validation = True
    can_import_settings = True

    def add_arguments(self, parser):
        parser.add_argument('dir_path',
                            type=str,
                            help='Directory path to iterate and create entries in the system')

    def handle(self, *args, **options):

      dir_path = options['dir_path']

      dir_path = pathlib.Path(dir_path).expanduser()

      for file in chain(
        dir_path.glob('**/*.NEF'),
        dir_path.glob('**/*.nef'),
        dir_path.glob('**/*.DNG'),
        dir_path.glob('**/*.dng'),
        dir_path.glob('**/*.ARW'),
        dir_path.glob('**/*.arw')
      ):
        if '.AppleDouble' in str(file):
          continue
        if '.cache' in str(file).lower():
          continue

        if str(file.parent.name).startswith('.'):
          continue
        if str(file.parent.name).startswith('cache'):
          continue

        print(str(file))
        Photopath.objects.get_or_create(
          name=file.name,
          path=str(file)
        )

      call_command('rebuild_index', '--noinput', interactive=False, verbosity=1)
